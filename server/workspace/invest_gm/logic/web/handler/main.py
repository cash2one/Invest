# coding=utf-8
"""
Created on 2015-4-22

@author: Jay
"""
from utils.route import route
from utils.network.http import HttpRpcHandler
from utils.wapper.web import web_adaptor
from utils.web import cookie

@route(r'/', name='index')  # 首页
class RootHandle(HttpRpcHandler):
    @web_adaptor(use_http_render=False)
    def get(self):
        self.render('index.html')

