#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019/10/11 15:50
# @Author: yanmiexingkong
# @email : yanmiexingkong@gmail.com
# @File  : 1.py
import requests

url = "https://www.lagou.com/jobs/positionAjax.json"

querystring = {"city": "%E4%B8%8A%E6%B5%B7", "needAddtionalResult": "false"}

payload = "first=true&pn=1&kd=%E9%94%80%E5%94%AE"
headers = {
    'Sec-Fetch-Mode': "cors",
    'Origin': "https://www.lagou.com",
    'X-Anit-Forge-Code': "0",
    'Accept-Language': "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-TW;q=0.6",
    'X-Requested-With': "XMLHttpRequest",
    'Accept-Encoding': "gzip, deflate, br",
    'Cookie': "_ga=GA1.2.1105657872.1542698799; user_trace_token=20181120152638-9e60fd83-ec95-11e8-aa77-525400f775ce; LGUID=20181120152638-9e61003f-ec95-11e8-aa77-525400f775ce; OUTFOX_SEARCH_USER_ID_NCOO=1514844181.3726397; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2216803e9d52173-00a544947dd88d-10336653-2304000-16803e9d5221e9%22%2C%22%24device_id%22%3A%2216803e9d52173-00a544947dd88d-10336653-2304000-16803e9d5221e9%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; JSESSIONID=ABAAABAAAIAACBIA64E3D4927D3F3DDDDEDFBD7F6944FA3; WEBTJ-ID=20191010112233-16db3b086dc31e-0d248a9cbda741-1d3d6b55-2304000-16db3b086ddc50; _gid=GA1.2.577872853.1570677754; index_location_city=%E4%B8%8A%E6%B5%B7; X_MIDDLE_TOKEN=e352f707d48c6dd83a4481032a585983; gate_login_token=d9693cf70836e55cc7f55379499de090b00e9a2083d1bb8f; LG_LOGIN_USER_ID=74adc577ce859f9eab99e94df2267c716a37ff1b04bd350c; LG_HAS_LOGIN=1; _putrc=2672DC7FBFD8AC03; login=true; unick=%E8%8C%85%E5%BC%8B%E9%B8%A3; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; hasDeliver=107; privacyPolicyPopup=false; TG-TRACK-CODE=index_navigation; LGSID=20191011152224-df2f3749-ebf7-11e9-a57b-5254005c3644; PRE_UTM=; PRE_HOST=www.v2ex.com; PRE_SITE=https%3A%2F%2Fwww.v2ex.com%2Ft%2F529842; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Fgongsi%2F%25E8%258E%25B7%25E5%258F%2596; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1570677755,1570776470,1570778545; _gat=1; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1570780125; LGRID=20191011154845-8da19e48-ebfb-11e9-a57b-5254005c3644; X_HTTP_TOKEN=b23cdb7185e25e155410870751e1e06f31d7bbd31c; SEARCH_ID=296fcb5aad9a4748988ca202e05de9c3",
    'Connection': "keep-alive",
    'Pragma': "no-cache",
    'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36",
    'Content-Type': "application/x-www-form-urlencoded; charset=UTF-8",
    'Accept': "application/json, text/javascript, */*; q=0.01",
    'Cache-Control': "no-cache",
    'Referer': "https://www.lagou.com/jobs/list_%E9%94%80%E5%94%AE/p-city_3?&cl=false&fromSearch=true&labelWords=&suginput=",
    'Sec-Fetch-Site': "same-origin",
    'X-Anit-Forge-Token': "None",
    'cache-control': "no-cache",
    'Postman-Token': "42bd84ba-9466-4ca9-9db6-cc7cece8ae3a"
}

response = requests.request("POST", url, data=payload, headers=headers, params=querystring)

print(response.text)
