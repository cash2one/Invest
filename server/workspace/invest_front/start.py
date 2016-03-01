#!/usr/bin/python2.7
# coding=utf-8
"""
Created on 2015-4-22

@author: Jay
"""
import site
import os
site.addsitedir(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
site.addsitedir(os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "common_server"))
from gevent import monkey
monkey.patch_all()
from invest_front import setting
from utils.service_control.controller import MainService


class Service(MainService):
    def __init__(self):
        super(Service, self).__init__(setting.SERVICE_TYPE,
                                      setting.VERSION)

    def init(self, args):
        pass

    def exit(self):
        super(Service, self).exit()
        self.update()

    def update(self):
        pass

    def services(self, args, thread_ls):
        from invest_front.apps.web_app import WebApp
        thread_ls.append(WebApp(args.http_port, args.is_https))

    def add_cmd_opts(self, arg_parser):
        arg_parser.add_argument('--http_port', default=10000, type=int,  help="The port of the http app listen")
        
if __name__ == "__main__":
    import sys
    reload(sys)
    sys.setdefaultencoding('utf8')

    Service().start_service()
