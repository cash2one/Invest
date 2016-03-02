# coding=utf-8
"""
Created on 2015-4-22

@author: Jay
"""
from utils.route import route
from utils.network.http import HttpRpcHandler
from utils.wapper.web import web_adaptor
from invest_front.setting import *

@route(r'/', name='index')  # 首页
class RootHandle(HttpRpcHandler):
    @web_adaptor(use_http_render=False)
    def get(self):
        LoanProductLs = LOAN_PRODUCT_DIC.values()
        LoanProductLs.sort(key=lambda dic:dic['idx'])

        LoanBusinessLs = LOAN_BUSINESS_DIC.values()
        LoanBusinessLs.sort(key=lambda dic:dic['idx'])
        render_dict = {'LoanProductLs': LoanProductLs,
                       'LoanAdvLs': LOAN_ADV_LS,
                       'LoanBusinessLs': LoanBusinessLs,
                       'LoanKnowledgeLs': LOAN_KNOWLEDAGE_LS,
                       'LoanCaseLs': LOAN_CASE_LS,
                       'LoanProblemLs': LOAN_PROBLEM_LS,
                       'LoanAniLs':LOAN_ANI_LS}

        self.render('index/index.html', **render_dict)

