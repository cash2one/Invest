# coding=utf-8
"""
Created on 2015-4-22

@author: Jay
"""
from utils.route import route
from utils.network.http import HttpRpcHandler
from utils.wapper.web import web_adaptor
from invest_front.setting import *

def get_common_dic(http_handler):
    return {'LoanNavls': LOAN_NAV_LS,
            'CurUrl': http_handler.request.uri}

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

        render_dict.update(get_common_dic(self))
        self.render('index/index.html', **render_dict)


@route(r'/loan_knowledge', name='loan_knowledge')  # 贷款攻略
class LoanKnowledgeHandle(HttpRpcHandler):
    @web_adaptor(use_http_render=False)
    def get(self):
        render_dict = {'DataLs':LOAN_KNOWLEDAGE_LS,
                       'LoanKnowledgeLs': LOAN_KNOWLEDAGE_LS,
                       'LoanCaseLs': LOAN_CASE_LS,
                       'LoanProblemLs': LOAN_PROBLEM_LS,}

        render_dict.update(get_common_dic(self))
        self.render('util/list.html', **render_dict)


@route(r'/loan_case', name='loan_case')  # 贷款案例
class LoanCaseHandle(HttpRpcHandler):
    @web_adaptor(use_http_render=False)
    def get(self):
        render_dict = {'DataLs':LOAN_CASE_LS,
                       'LoanKnowledgeLs': LOAN_KNOWLEDAGE_LS,
                       'LoanCaseLs': LOAN_CASE_LS,
                       'LoanProblemLs': LOAN_PROBLEM_LS,}

        render_dict.update(get_common_dic(self))
        self.render('util/list.html', **render_dict)


@route(r'/loan_problem', name='loan_problem')  # 贷款问题
class LoanProblemHandle(HttpRpcHandler):
    @web_adaptor(use_http_render=False)
    def get(self):
        render_dict = {'DataLs':LOAN_PROBLEM_LS,
                       'LoanKnowledgeLs': LOAN_KNOWLEDAGE_LS,
                       'LoanCaseLs': LOAN_CASE_LS,
                       'LoanProblemLs': LOAN_PROBLEM_LS,}

        render_dict.update(get_common_dic(self))
        self.render('util/list.html', **render_dict)


