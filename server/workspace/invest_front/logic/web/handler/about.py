#!/usr/bin/python2.7
# coding=utf-8
"""
Created on 2016-3-3

@author: Jay
"""
from utils.route import route
from utils.network.http import HttpRpcHandler
from utils.wapper.web import web_adaptor
from invest_front.logic.web.handler import get_common_dic
from invest_front.setting import *

@route(LOAN_NAV_BAR_DIC[LBL_ABOUT]['url'])  # 关于我们
class AboutHandle(HttpRpcHandler):
    @web_adaptor(use_http_render=False)
    def get(self):
        render_dict = {}
        render_dict.update(get_common_dic(self))
        self.render(LOAN_NAV_BAR_DIC[LBL_ABOUT]['html'], **render_dict)

@route(LOAN_NAV_BAR_DIC[LBL_CONTACT]['url'])  # 联系我们
class ContactHandle(HttpRpcHandler):
    @web_adaptor(use_http_render=False)
    def get(self):
        render_dict = {}
        render_dict.update(get_common_dic(self))
        self.render(LOAN_NAV_BAR_DIC[LBL_CONTACT]['html'], **render_dict)


@route(LOAN_NAV_BAR_DIC[LBL_COOPERATION]['url'])  # 商务合作
class CooperationtHandle(HttpRpcHandler):
    @web_adaptor(use_http_render=False)
    def get(self):
        render_dict = {}
        render_dict.update(get_common_dic(self))
        self.render(LOAN_NAV_BAR_DIC[LBL_COOPERATION]['html'], **render_dict)


@route(LOAN_NAV_BAR_DIC[LBL_RECRUIT]['url'])  # 商务合作
class RecruitHandle(HttpRpcHandler):
    @web_adaptor(use_http_render=False)
    def get(self):
        render_dict = {"recruit_ls": RECRUIT_LS}
        render_dict.update(get_common_dic(self))
        self.render(LOAN_NAV_BAR_DIC[LBL_RECRUIT]['html'], **render_dict)
