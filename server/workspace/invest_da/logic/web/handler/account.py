#!/usr/bin/python2.7
# coding=utf-8
"""
Created on 2015-12-15

@author: Jay
"""
from utils.route import route
from utils.network.http import HttpRpcHandler
from utils.wapper.web import web_adaptor
from invest_da.lib.token import TokenMgr
from invest_da.lib.account.control import AccountMgr
from utils import error_code
from utils import logger
from invest_da.lib.web import body_json_parser
from invest_da.lib.web import id_passwd_login


@route(r'/register', name='register')
class RegisterHandler(HttpRpcHandler):
    @web_adaptor(body_parser_fun= body_json_parser)
    def post(self, **kwargs):
        """
        data_dic:account, passwd,
        id_card, email, phone,
        leader_id,
        bank, bank_address, bank_account, bank_name,
        wechat, alipay
        :param kwargs:
        :return:
        """
        if AccountMgr().is_id_exist(kwargs['id']):
            logger.info("register ERROR_LOGIC, id existed, %s" % kwargs['id'])
            self.set_status(error_code.ERROR_LOGIC, 'Parameter Error')
            return {"result": error_code.ERROR_LOGIC}

        AccountMgr().create_account(kwargs)
        return {"result": error_code.ERROR_SUCCESS}

@route(r'/login', name='login')
class LoginHandler(HttpRpcHandler):
    @web_adaptor(body_parser_fun=body_json_parser)
    @id_passwd_login()
    def post(self, account, **kwargs):
        return {"result": error_code.ERROR_SUCCESS,
                "account_info": account.get_info_dic(),
                "access_token": TokenMgr().generate_access_token(account.id)}