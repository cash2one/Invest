#!/usr/bin/python2.7
# coding=utf-8
"""
Created on 2015-12-15

@author: Jay
"""

import time
from utils import logger
from utils.interfaces.common import IManager
from utils.meta.singleton import Singleton
from invest_da.db import DBAccountInst
from invest_da.lib.account.control import AccountMgr


# 系统逻辑管理器列表
G_LOGIC_MANAGER_LIST = [
    (AccountMgr, DBAccountInst),
]


class LibMgr(IManager):
    __metaclass__ = Singleton

    def __init__(self):
        self.cur_time = time.time()

    def init(self, reload_db=False):
        """
        逻辑系统初始化
        @param reload_db:是否重新加载db
        """
        for mgr_info in G_LOGIC_MANAGER_LIST:
            mgr = mgr_info[0]()
            dbint = mgr_info[1]
            init_sql = mgr.init_sql()
            # 如果有特殊的提供初始化的sql语句，则采用该sql语句初始化，否则全部加载
            if init_sql:
                logger.warn("LibMgr::init mgr:%s init_sql:%s" % (mgr, init_sql))
                mgr.init(mgr.db_unpick(dbint.query(init_sql)))
            else:
                mgr.init(mgr.db_unpick(dbint.query_all()))

    def update(self, cur_time):
        """
        逻辑系统更新
        @param curtime:当前时间戳
        """
        [mgr_info[0]().update(cur_time) for mgr_info in G_LOGIC_MANAGER_LIST]

