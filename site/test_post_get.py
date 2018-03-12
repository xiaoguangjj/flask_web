# -*- coding:utf-8 -*-
import requests

def get(url, datas=None):
    response = requests.get(url, params=datas)
    data = response.json()
    return data

def post(url, datas=None):
    response = requests.post(url, data=datas)
    json = response.json()
    return json

if __name__=="__main__":
    # url = "http://0.0.0.0:8000/article_query"
    url = "http://0.0.0.0:8000/article_info"
    # url = "http://0.0.0.0:8000/article_alter"
    # url = "http://0.0.0.0:8000/article_add"

    datas = {
        # 'title' : 'title',
        'creater':'123',
        # 'page': 1,
        # 'limit':3
    }

    param = {
        'text' : "文章1",
        'creater' : 'user',
        'title': '主题1'
    }

    data = get(url,datas)

    # data = post(url,param)
