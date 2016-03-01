#!/usr/bin/python2.7
# coding=utf-8
"""
Created on 2015-4-25

@author: Jay
"""
import site
import os
site.addsitedir(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
site.addsitedir(os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "common_server"))
from gevent import monkey
monkey.patch_all()

from invest_da import setting
from utils.service_control.controller import MainService
from utils.service_control.setting import RT_MYSQL
import time
from utils.service_control.parser import parser_boolean


class Service(MainService):
    """
    主服务
    """
    def __init__(self):
        super(Service, self).__init__(setting.SERVICE_TYPE,
                                      setting.VERSION,
                                      db_update_dir_path=os.path.join(os.path.dirname(__file__), "db_update"),
                                      use_mysqldb=True)

    def init(self, args):
        from invest_da.lib.lib_mgr import LibMgr
        LibMgr().init()

    def update(self):
        super(Service, self).update()
        cur_time = time.time()
        from invest_da.lib.lib_mgr import LibMgr
        LibMgr().update(cur_time)

    def services(self, args, thread_ls):
        """
        添加服务接口
        :param args: 参数变量
        :param thread_ls: 现有的服务列表
        :return:
        """
        from invest_da.apps.rpc_app import RpcApp
        from invest_da.apps.web_app import WebApp

        thread_ls.append(RpcApp(args.tcp_port))
        thread_ls.append(WebApp(args.http_port, args.is_https))

    def add_cmd_opts(self, arg_parser):
        """
        在获取sm参数之前，提供添加arg_parser参数接口
        :param arg_parser: 参数变量
        :return:
        """
        pass

    def add_cmd_opts_after_sm(self, arg_parser):
        """
        在获取sm参数之后，提供添加arg_parser参数接口
        :param arg_parser: 参数变量
        :return:
        """
        from utils.service_control.cacher import ServiceMgrCacher
        mysql_dic = ServiceMgrCacher.find_tp_service(RT_MYSQL)
        arg_parser.add_argument('--db_host', default=mysql_dic['ip'], type=str, help="The host of the db")
        arg_parser.add_argument('--db_port', default=mysql_dic['port']['tcp'], type=int, help="The port of the db")
        arg_parser.add_argument('--db_user', default=mysql_dic['params']['db_user'], type=str, help="The username of the db")
        arg_parser.add_argument('--db_password', default=mysql_dic['params']['db_password'], type=str, help="The password for the db user")


if __name__ == "__main__":
    import sys
    reload(sys)
    sys.setdefaultencoding('utf8')
    Service().start_service()