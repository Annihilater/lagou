#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019/10/15 09:45
# @Author: yanmiexingkong
# @email : yanmiexingkong@gmail.com
# @File  : lagou.py
import os

import csv
import queue
import pymongo
import requests

from lxml import etree
from faker import Faker
from tqdm import tqdm


class LaGou(object):

    def __init__(self, keyword, city, path=os.getcwd()):
        self.num = 0
        self.city = city
        self.csv_header = ['职位名称', '详细链接', '工作地点', '薪资', '公司名称', '经验要求', '学历', '福利', '职位信息']
        self.ajax_url = 'https://www.lagou.com/jobs/positionAjax.json'
        self.path = path

        self.header = {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Referer': 'https://www.lagou.com/jobs/list_%E8%BF%90%E7%BB%B4?city=%E6%88%90%E9%83%BD&cl=false&fromSearch=true&labelWords=&suginput=',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
        }
        self.cookies1 = {}
        self.cookies2 = {}
        self.keyword = keyword
        self.query_data = {'first': True, 'pn': 1, 'kd': self.keyword}
        self.params = {'px': 'default', 'city': self.city, 'needAddtionalResult': 'false'}
        self.data = queue.Queue()

    @staticmethod
    def get_header():
        """
        随机生成 User-Agent
        :return:
        """
        user_agent = Faker('zh-CN').user_agent()
        return {
            'User-Agent': user_agent
        }

    def gen_cookies(self):
        """
        生成新的 cookies
        :return: 新 cookies
        """
        s = requests.Session()
        url = 'https://www.lagou.com/jobs/list_java/p-city_3?&cl=false&fromSearch=true&labelWords=&suginput='
        s.get(url=url, headers=self.get_header(), timeout=3)
        return s.cookies

    @staticmethod
    def save_to_mongo(data):
        if data:
            if not mongo_col.find_one(data):
                mongo_col.insert_one(data)
                print('单个数据插入成功', str(data))
            else:
                print('数据已存在', str(data))
        else:
            print('插入的数据为 None：' + str(data))

    def spider_detail(self, data):
        """
        1. 爬去职位详情页数据
        2. 每次爬去更换 cookies
        3. 解析页面获取职位详情
        4. 将单个职位数据存入 mongodb
        5. 将单个职位简略数据存进 self.data 队列
        :param data: 职位列表页 json 数据中的单个职位数据
        :return:
        """
        self.cookies2 = self.gen_cookies()
        detail_url = 'https://www.lagou.com/jobs/' + str(data.get('positionId')) + '.html'
        response = requests.get(detail_url, headers=self.header, cookies=self.cookies2)
        response.encoding = 'utf-8'

        html = etree.HTML(response.text)
        detail = ''.join(html.xpath('//*[@class="job-detail"]//*/text()')).strip()

        if detail.isspace():
            detail = ''.join(html.xpath('//*[@class="job-detail"]/text()')).strip()

        detail_data = {
            "detail_url": detail_url,
            "detail": detail
        }

        data.update(detail_data)
        self.save_to_mongo(data)
        self.num += 1
        print('成功插入第' + str(self.num) + '条数据')
        print('-' * 80)

        csv_data = {
            "职位名称": data.get('positionName'),
            "工作地点": data.get('district'),
            "薪资": data.get('salary'),
            "公司名称": data.get('companyFullName'),
            "经验要求": data.get('workYear'),
            "学历": data.get('education'),
            "福利": data.get('positionAdvantage'),
            "详细链接": detail_url,
            "职位信息": detail
        }
        self.data.put(csv_data)

    def spider(self):
        """
        1. 拉勾职位搜索最多显示 30 页，遍历请求每页，每次请求更换 cookies，防封
        2. 每页 15 条数据，遍历 15 条数据，对职位详情页发起请求
        :return:
        """
        for i in tqdm(range(1, 31)):
            self.cookies1 = self.gen_cookies()
            self.query_data.update({'pn': i})
            req = requests.post(self.ajax_url, headers=self.header, data=self.query_data, params=self.params,
                                cookies=self.cookies1, timeout=3)
            text = req.json()
            data = text['content']['positionResult']['result']
            for item in data:
                self.spider_detail(item)

    def run(self):
        self.spider()
        if os.path.exists(self.path):
            data_list = []
            self.path = os.path.join(self.path, 'Data')
            while not self.data.empty():
                data_list.append(self.data.get())
            with open(os.path.join(self.path, '拉钩网招聘_城市_{}_关键词_{}.csv'.format(self.city, self.keyword)), 'w',
                      newline='', encoding='utf-8-sig') as f:
                f_csv = csv.DictWriter(f, self.csv_header)
                f_csv.writeheader()
                f_csv.writerows(data_list)


if __name__ == '__main__':
    keyword = 'java'
    city = '上海'
    mongo_client = pymongo.MongoClient('mongodb://localhost:27017')
    mongo_db = mongo_client['lagou']
    mongo_col = mongo_db[city + '_' + keyword]
    LaGou(keyword=keyword, city=city).run()
    mongo_client.close()
