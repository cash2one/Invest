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
        self.redirect(USER_NAV_BAR_DIC[LBL_U_BUSIMGR]['url'])


@route(USER_NAV_BAR_DIC[LBL_U_BUSIMGR]['url'])  # 业务管理
class UserBusimgrHandle(HttpRpcHandler):
    @web_adaptor(use_http_render=False)
    def get(self):
        # 默认跳转到业务列表
        self.redirect(USER_BUSIMGR_BAR_DIC[LBL_UB_LIST]['url'])


@route(USER_NAV_BAR_DIC[LBL_U_DATA]['url'])  # 个人资料
class UserDataHandle(HttpRpcHandler):
    @web_adaptor(use_http_render=False)
    def get(self):
        render_dict = {"UserName": "杜若飞"}
        render_dict.update(get_common_dic(self, USER_NAV_BAR_DIC))
        return self.render(USER_NAV_BAR_DIC[LBL_U_DATA]['html'], **render_dict)


@route(USER_BUSIMGR_BAR_DIC[LBL_UB_LIST]['url'])  # 业务列表
class UserBusimgrListHandle(HttpRpcHandler):
    @web_adaptor(use_http_render=False)
    def get(self):
        UBNavBarLs = USER_BUSIMGR_BAR_DIC.values()
        UBNavBarLs.sort(key=lambda dic: dic['idx'])

        render_dict = {"UserName": "杜若飞",
                       'UBNavBarLs': UBNavBarLs}
        render_dict.update(get_common_dic(self, USER_NAV_BAR_DIC))
        return self.render(USER_BUSIMGR_BAR_DIC[LBL_UB_LIST]['html'], **render_dict)


@route(USER_BUSIMGR_BAR_DIC[LBL_UB_APPLY]['url'])  # 提交贷款
class UserBusimgrApplyHandle(HttpRpcHandler):
    @web_adaptor(use_http_render=False)
    def get(self):
        UBNavBarLs = USER_BUSIMGR_BAR_DIC.values()
        UBNavBarLs.sort(key=lambda dic: dic['idx'])
        LoanProductLs = LOAN_PRODUCT_DIC.values()
        LoanProductLs.sort(key=lambda dic: dic['idx'])

        render_dict = {"UserName": "杜若飞",
                       'UBNavBarLs': UBNavBarLs,
                       'LoanProductLs':LoanProductLs}
        render_dict.update(get_common_dic(self, USER_NAV_BAR_DIC))
        return self.render(USER_BUSIMGR_BAR_DIC[LBL_UB_APPLY]['html'], **render_dict)


