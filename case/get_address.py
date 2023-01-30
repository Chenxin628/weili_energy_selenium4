# -*- coding: utf-8 -*-
"""
@Time ： 2022/1/18 11:36
@Auth ： 技术空间
@File ：post_demo.py
@IDE ：PyCharm
@Motto：技术总是要日积月累的

"""

import requests
import json

def data_down():
    if __name__ == '__main__':
        #cookie = "token=code_space;"
        header = {
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Connection": "keep-alive",
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"
        }
        # 发送字典
        #post_dict = {'key1': 'value1', 'key2': 'value2'}
        # 发送元组
        #post_tuple = (('key1', 'value1'), ('key1', 'value2'))
        # 发送json
        post_json = json.dumps({
    #  "provinceId": "77c5e25a27a44e46b7e336604e8d619a",  #节能中心license
     "enterpriseCode": "913504236740078825",
     "statType": 2,
     "deviceId": "4f9ec6acf1f2aa8c17b6515d5dc2435f",
     "statDate": "2022-08-01"
    })

        r3 = requests.post("http://www.fjjnzx.cn:9005/downloadEnergyData", data=post_json, headers=header)
        #print("r3返回的内容为-->\n" + r3.text)
        x=json.loads(r3.text) # x 是字典
        #print(x)
        print(len(x))
        print(len(x['data']))
        y = len(x['data'])
        #print(x['data'])
        for i in range(y):
            print(x['data'][i],i)


def get_down_news():
    if __name__ == '__main__':
        #cookie = "token=code_space;"
        header = {
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Connection": "keep-alive",
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"
        }
        # 发送字典
        #post_dict = {'key1': 'value1', 'key2': 'value2'}
        # 发送元组
        #post_tuple = (('key1', 'value1'), ('key1', 'value2'))
        # 发送json
        post_json = json.dumps({
"region":"110000",
"enterpriseCode":"91350521MA2YGTGK30"
})

        r3 = requests.post("http://www.fjjnzx.cn:9005/", data=post_json, headers=header)
        print("r3返回的内容为-->\n" + r3.text)

#get_down_news()
data_down()
'''
{"responseCode":"0","responseMessage":"RECEIVE SUCCESS","data":[]}
'''