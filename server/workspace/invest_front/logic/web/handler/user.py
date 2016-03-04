#!/usr/bin/python2.7
# coding=utf-8
"""
Created on 2016-3-4

@author: Jay
"""
from utils.route import route
from utils.network.http import HttpRpcHandler
from utils.wapper.web import web_adaptor
from invest_front.logic.web.handler import get_common_dic
from invest_front.common.about import RECRUIT_LS
from invest_front.common import *

@route(r"/is_username_exist")  # 检测用户名
class LoanProblemHandle(HttpRpcHandler):
    @web_adaptor()
    def post(self, username):
        # 存在返回1,不存在返回0
        return int(True)


@route(LOAN_NAV_BAR_DIC[LBL_LOGIN]['url'])  # 登陆
class LoginHandle(HttpRpcHandler):
    @web_adaptor(use_http_render=False)
    def get(self):
        render_dict = {"recruit_ls": RECRUIT_LS}
        render_dict.update(get_common_dic(self))
        self.render(LOAN_NAV_BAR_DIC[LBL_LOGIN]['html'], **render_dict)

    @web_adaptor(use_http_render=False)
    def post(self, *args, **kwargs):
        # 默认登陆成功
        render_dict = {"recruit_ls": RECRUIT_LS}
        render_dict.update(get_common_dic(self))
        self.redirect(USER_NAV_BAR_DIC[LBL_U_DATA]['url'], **render_dict)


@route(USER_NAV_BAR_DIC[LBL_U_BUSIMGR]['url'])  # 用户
class UserBusimgrHandle(HttpRpcHandler):
    @web_adaptor(use_http_render=False)
    def get(self):
        # 默认登陆成功
        render_dict = {"UserName": "杜若飞"}
        render_dict.update(get_common_dic(self, USER_NAV_BAR_DIC))
        return self.render(USER_NAV_BAR_DIC[LBL_U_BUSIMGR]['html'], **render_dict)


@route(USER_NAV_BAR_DIC[LBL_U_DATA]['url'])  # 用户
class UserDataHandle(HttpRpcHandler):
    @web_adaptor(use_http_render=False)
    def get(self):
        # 默认登陆成功
        render_dict = {"UserName": "杜若飞"}
        render_dict.update(get_common_dic(self, USER_NAV_BAR_DIC))
        return self.render(USER_NAV_BAR_DIC[LBL_U_DATA]['html'], **render_dict)

