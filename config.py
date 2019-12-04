#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019-10-10 11:52
# @Author: yanmiexingkong
# @email : yanmiexingkong@gmail.com
# @File  : config.py

# 本地 mongodb 服务器地址、数据库名、集合名
mongo_uri = 'mongodb://localhost:27017'
mongo_client_name = 'lagou'
mongo_db_name = 'python4'

# 必须设置headers里的UserAgent,否则拉钩网不返回正确数据
# 因为requests发送请求的默认UA是python-requests/1.2.0，会被检测到是爬虫
# 我们伪装成一个正常的Chrome浏览器，你也可以换成其他的浏览器UA
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-TW;q=0.6',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Cookie': '_ga=GA1.2.1105657872.1542698799; user_trace_token=20181120152638-9e60fd83-ec95-11e8-aa77-525400f775ce; LGUID=20181120152638-9e61003f-ec95-11e8-aa77-525400f775ce; OUTFOX_SEARCH_USER_ID_NCOO=1514844181.3726397; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2216803e9d52173-00a544947dd88d-10336653-2304000-16803e9d5221e9%22%2C%22%24device_id%22%3A%2216803e9d52173-00a544947dd88d-10336653-2304000-16803e9d5221e9%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; LG_LOGIN_USER_ID=ae35e4d76133f5e0baac36d5e66b0384158a04dd2e7c9a24; JSESSIONID=ABAAABAAAIAACBIA64E3D4927D3F3DDDDEDFBD7F6944FA3; WEBTJ-ID=20191010112233-16db3b086dc31e-0d248a9cbda741-1d3d6b55-2304000-16db3b086ddc50; _gid=GA1.2.577872853.1570677754; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1570677755; index_location_city=%E4%B8%8A%E6%B5%B7; TG-TRACK-CODE=index_search; LGSID=20191010182454-33991e83-eb48-11e9-a57a-5254005c3644; X_MIDDLE_TOKEN=e352f707d48c6dd83a4481032a585983; _gat=1; SEARCH_ID=f9b76a0fd78e4192b9e30eeda7c227a8; X_HTTP_TOKEN=b23cdb7185e25e155335070751e1e06f31d7bbd31c; LGRID=20191010190215-6b32345a-eb4d-11e9-a57a-5254005c3644; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1570705336',
    'Host': 'www.lagou.com',
    'Pragma': 'no-cache',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
}

headers1 = {
    'Sec-Fetch-Mode': "cors",
    'Origin': "https://www.lagou.com",
    'X-Anit-Forge-Code': "0",
    'Accept-Language': "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-TW;q=0.6",
    'X-Requested-With': "XMLHttpRequest",
    'Accept-Encoding': "gzip, deflate, br",
    'Cookie': "_ga=GA1.2.1105657872.1542698799; user_trace_token=20181120152638-9e60fd83-ec95-11e8-aa77-525400f775ce; LGUID=20181120152638-9e61003f-ec95-11e8-aa77-525400f775ce; OUTFOX_SEARCH_USER_ID_NCOO=1514844181.3726397; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2216803e9d52173-00a544947dd88d-10336653-2304000-16803e9d5221e9%22%2C%22%24device_id%22%3A%2216803e9d52173-00a544947dd88d-10336653-2304000-16803e9d5221e9%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; JSESSIONID=ABAAABAAAIAACBIA64E3D4927D3F3DDDDEDFBD7F6944FA3; WEBTJ-ID=20191010112233-16db3b086dc31e-0d248a9cbda741-1d3d6b55-2304000-16db3b086ddc50; _gid=GA1.2.577872853.1570677754; index_location_city=%E4%B8%8A%E6%B5%B7; X_MIDDLE_TOKEN=e352f707d48c6dd83a4481032a585983; gate_login_token=d9693cf70836e55cc7f55379499de090b00e9a2083d1bb8f; LG_LOGIN_USER_ID=74adc577ce859f9eab99e94df2267c716a37ff1b04bd350c; LG_HAS_LOGIN=1; _putrc=2672DC7FBFD8AC03; login=true; unick=%E8%8C%85%E5%BC%8B%E9%B8%A3; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; hasDeliver=107; privacyPolicyPopup=false; TG-TRACK-CODE=index_navigation; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1570677755,1570776470,1570778545; LGSID=20191011163327-cc11e725-ec01-11e9-a57b-5254005c3644; PRE_UTM=; PRE_HOST=; PRE_SITE=https%3A%2F%2Fwww.lagou.com%2Futrack%2FtrackMid.html%3Ff%3Dhttps%253A%252F%252Fwww.lagou.com%252Fjobs%252Flist%255F%2525E9%252594%252580%2525E5%252594%2525AE%252Fp-city%255F3%253F%2526cl%253Dfalse%2526fromSearch%253Dtrue%2526labelWords%253D%2526suginput%253D%26t%3D1570780145%26_ti%3D3; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Fjobs%2Flist_%25E9%2594%2580%25E5%2594%25AE%2Fp-city_3%3F%26cl%3Dfalse%26fromSearch%3Dtrue%26labelWords%3D%26suginput%3D; _gat=1; X_HTTP_TOKEN=b23cdb7185e25e157713870751e1e06f31d7bbd31c; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1570783178; LGRID=20191011163938-a9091ef1-ec02-11e9-9a37-525400f775ce; SEARCH_ID=4d1fad602e154ac1a4cea5294e75dbbc,_ga=GA1.2.1105657872.1542698799; user_trace_token=20181120152638-9e60fd83-ec95-11e8-aa77-525400f775ce; LGUID=20181120152638-9e61003f-ec95-11e8-aa77-525400f775ce; OUTFOX_SEARCH_USER_ID_NCOO=1514844181.3726397; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2216803e9d52173-00a544947dd88d-10336653-2304000-16803e9d5221e9%22%2C%22%24device_id%22%3A%2216803e9d52173-00a544947dd88d-10336653-2304000-16803e9d5221e9%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; JSESSIONID=ABAAABAAAIAACBIA64E3D4927D3F3DDDDEDFBD7F6944FA3; WEBTJ-ID=20191010112233-16db3b086dc31e-0d248a9cbda741-1d3d6b55-2304000-16db3b086ddc50; _gid=GA1.2.577872853.1570677754; index_location_city=%E4%B8%8A%E6%B5%B7; X_MIDDLE_TOKEN=e352f707d48c6dd83a4481032a585983; gate_login_token=d9693cf70836e55cc7f55379499de090b00e9a2083d1bb8f; LG_LOGIN_USER_ID=74adc577ce859f9eab99e94df2267c716a37ff1b04bd350c; LG_HAS_LOGIN=1; _putrc=2672DC7FBFD8AC03; login=true; unick=%E8%8C%85%E5%BC%8B%E9%B8%A3; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; hasDeliver=107; privacyPolicyPopup=false; TG-TRACK-CODE=index_navigation; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1570677755,1570776470,1570778545; LGSID=20191011163327-cc11e725-ec01-11e9-a57b-5254005c3644; PRE_UTM=; PRE_HOST=; PRE_SITE=https%3A%2F%2Fwww.lagou.com%2Futrack%2FtrackMid.html%3Ff%3Dhttps%253A%252F%252Fwww.lagou.com%252Fjobs%252Flist%255F%2525E9%252594%252580%2525E5%252594%2525AE%252Fp-city%255F3%253F%2526cl%253Dfalse%2526fromSearch%253Dtrue%2526labelWords%253D%2526suginput%253D%26t%3D1570780145%26_ti%3D3; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Fjobs%2Flist_%25E9%2594%2580%25E5%2594%25AE%2Fp-city_3%3F%26cl%3Dfalse%26fromSearch%3Dtrue%26labelWords%3D%26suginput%3D; _gat=1; X_HTTP_TOKEN=b23cdb7185e25e157713870751e1e06f31d7bbd31c; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1570783178; LGRID=20191011163938-a9091ef1-ec02-11e9-9a37-525400f775ce; SEARCH_ID=4d1fad602e154ac1a4cea5294e75dbbc; user_trace_token=20191010194225-fc607026-59d5-4443-a8b0-9ad025560a42; X_HTTP_TOKEN=b23cdb7185e25e157710870751e1e06f31d7bbd31c; JSESSIONID=ABAAABAABEEAAJA7ED5AB7A695F71BEA591F99E99FCF5E8; SEARCH_ID=01d9c248730549b99452e2e97f625ca7",
    'Connection': "keep-alive",
    'Pragma': "no-cache",
    'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36",
    'Content-Type': "application/x-www-form-urlencoded; charset=UTF-8",
    'Accept': "application/json, text/javascript, */*; q=0.01",
    'Cache-Control': "no-cache",
    'Referer': "https://www.lagou.com/jobs/list_%E9%94%80%E5%94%AE/p-city_3?&cl=false&fromSearch=true&labelWords=&suginput=",
    'Sec-Fetch-Site': "same-origin",
    'X-Anit-Forge-Token': "None",
    'Postman-Token': "c95e7c19-1937-425f-9b24-2a3e2eea06ba,d6859c41-dbec-48b0-a7cd-0e8559f11cb4",
    'Host': "www.lagou.com",
    'Content-Length': "37",
    'cache-control': "no-cache"
    }

# 请求地址，Java可以换成其他的搜索词
# url = 'https://www.lagou.com/zhaopin/Java/'
start_url = 'https://www.lagou.com/zhaopin/Python/'
# url = 'https://www.lagou.com/jobs/list_python/p-city_3?px=default#filterBox'
# url = 'https://www.lagou.com/jobs/list_平面设计师/p-city_3'
# url = 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput='

# 每页职位数量，拉勾默认是 15 个
per_page_job_num = 15

# 存放已经成功抓取到数据的 url
good_urls = []
