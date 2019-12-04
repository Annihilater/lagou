#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019-10-10 11:16
# @Author: yanmiexingkong
# @email : yanmiexingkong@gmail.com
# @File  : spider.py
import time
import pymongo
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm

from config import start_url, headers, per_page_job_num, good_urls, mongo_client_name, mongo_db_name, mongo_uri

mongo_client = pymongo.MongoClient(mongo_uri)
mongo_db = mongo_client[mongo_client_name]
mongo_col = mongo_db[mongo_db_name]


def spider_sum_jobs(url, headers):
    """
    获取查询出的总职位数
    :param url:
    :param headers:
    :return:
    """
    r = requests.get(url=url, headers=headers)
    if r.status_code == 200:
        print('请求成功')
        soup = BeautifulSoup(r.text, 'lxml')
        job_num = soup.select('#tab_pos span')
        if job_num:
            job_num = job_num[0].text
            print('总职位数：' + job_num)
            return int(job_num)
        else:
            print('没有获取到总职位数')
            return None
    else:
        print('请求失败')
        return None


def gen_urls():
    """
    生成待爬取的 url 列表
    :return: 待爬去的 url 列表
    """
    urls = []
    job_num = spider_sum_jobs(start_url, headers)
    page_num = int(job_num / 15)
    if job_num % per_page_job_num:
        page_num += 1
    for i in range(1, page_num + 1):
        if start_url.endswith('/'):
            urls.append(start_url + str(i))
        else:
            urls.append(start_url + '/' + str(i))
    return urls


def spider(url, headers):
    """
    :param url:
    :param headers:
    :return:
    """
    # print(url)
    results = []
    time.sleep(10)
    r = requests.get(url=url, headers=headers)

    if r.status_code == 200:
        print('请求成功')
        """
        利用BS解析, r.text是返回的网页内容，可以print查看, lxml是解析器，不行就用html.parser
        http://beautifulsoup.readthedocs.io/zh_CN/stable/#id12 各种解析器对比
        print(r.text)
        """
        soup = BeautifulSoup(r.text, 'lxml')

        # 使用css selector解析，'.' 用来选择class，'#'选择id
        format_time_list = soup.select(".position .p_top .format-time")  # [0].text.strip() 发布时间
        position_list = soup.select(".position .p_top .position_link h3")  # 职位
        position_link_list = soup.select(".position .p_top a[href] ")  # 职位详情地址
        location_list = soup.select(".position .p_top .position_link .add em")  # 地点
        money_list = soup.select(".position .p_bot .li_b_l span")  # 薪水
        exp_list = soup.select(".position .p_bot .li_b_l")  # 经验学历
        company_name_list = soup.select(".list_item_top .company .company_name a")  # 公司名
        industry_list = soup.select(".con_list_item .list_item_top .company .industry")  # 企业状况
        label1_list = soup.select(".list_item_bot .li_b_l")  # 公司标签 1
        label2_list = soup.select(".list_item_bot .li_b_r")  # 公司标签 2

        """
        判断是否抓取到数据
        如果没有抓到数据且 url 在 bad_url 中，就把 url 放到 bad_url 后面再抓
        如果抓到数据且 url 在 bad_url中，就将该 url 从 bad_url 中移除
        """
        if not format_time_list:
            print('没有抓取到数据')
        else:
            print('成功抓取到数据')
            if url not in good_urls:
                good_urls.append(url)

            for i in range(len(format_time_list)):
                format_time = format_time_list[i].text
                position = position_list[i].text
                position_link = position_link_list[i].attrs['href'].split('?')[0]
                location = location_list[i].text
                money = money_list[i].text
                exp = exp_list[i].text.strip()
                company_name = company_name_list[i].text
                industry = industry_list[i].text.strip()
                label1 = label1_list[i].text.strip()
                label2 = label2_list[i].text.strip()

                result = dict(format_time=format_time, position=position, position_link=position_link,
                              location=location, money=money, exp=exp, company_name=company_name, industry=industry,
                              label1=label1, label2=label2)
                results.append(result)
            return results
    else:
        print('请求失败')


def save_to_mongo(data):
    """
    :param data:dict
    :return:
    """
    if data:
        # print(str(data))
        if not mongo_col.find_one(data):
            mongo_col.insert_one(data)
            # print('单个数据插入成功')
        else:
            # print('数据已存在')
            pass
    else:
        print('插入的数据为 None：' + str(data))


def main():
    urls = gen_urls()
    tasks = tqdm(total=len(urls))

    while urls:
        for url in urls:
            results = spider(url, headers)
            # print('待抓取列表', urls)
            # print('已抓取列表', good_urls)
            # print('results: ', result)
            if results:
                urls.remove(url)
                for result in results:
                    save_to_mongo(result)
                    tasks.update(1)


mongo_client.close()  # 关闭 mongodb 客户端

if __name__ == '__main__':
    main()
