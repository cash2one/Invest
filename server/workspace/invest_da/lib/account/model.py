#!/usr/bin/python2.7
# coding=utf-8
"""
Created on 2015-12-15

@author: Jay
"""
from utils.data.cache.dirty import DirtyFlagProcess
import time
from setting import *

class Account(object):
    def __init__(self, db_update_fun=None, **kwargs):
        """
        id, passwd,
        id_card, email, phone,
        leader_id,
        bank, bank_address, bank_account, bank_name,
        wechat, alipay
        :param db_update_fun:
        :param kwargs:
        :return:
        """
        self.__dict__ = kwargs

        self.dfp = DirtyFlagProcess(self)
        self.db_update_fun = db_update_fun

    def update(self, curtime):
        dirty_db_dict = self.dfp.get_db_dirty_attr()
        if dirty_db_dict and self.db_update_fun:
            dirty_db_dict['id'] = self.id
            self.db_update_fun([dirty_db_dict])

    def __str__(self):
        return str(self.get_info_dic())

    def __eq__(self, other):
        return self.id == other.id

    def __get_key(self, key):
        return self.__dict__[key] if key in self.__dict__ else getattr(self, "attr_%s" % key, "")

    def get_info_dic(self):
        """
        获取所有信息
        :return:
        """
        return dict([(key, self.__get_key(key)) for key in KEY_SET])

    def view_info_dic(self):
        """
        允许别人来查看的信息
        :return:
        """
        return dict([(key, self.__get_key(key)) for key in KEY_SET - PRIVATE_KEY_SET])

    def update_data(self, data_dic):
        """
        数据更新
        :param data_dic: 需要更新的数据
        :return:
        """
        for k, v in data_dic.items():
            self.__dict__[k] = v
        self.dfp.add_db_flag_ls(data_dic.keys())

    # passwd
    @property
    def attr_passwd(self):
        return self.passwd

    @attr_passwd.setter
    def attr_passwd(self, new_passwd):
        if self.passwd == new_passwd or not new_passwd:
            return

        self.passwd = new_passwd
        self.dfp.add_db_flag("passwd")

    # stat
    @property
    def attr_stat(self):
        return self.stat

    @attr_stat.setter
    def attr_stat(self, new_stat):
        if self.stat == new_stat:
            return

        self.stat = new_stat
        self.dfp.add_db_flag("stat")
        self.attr_active_time = time.time()

    # login_time
    @property
    def attr_login_time(self):
        return self.login_time

    @attr_login_time.setter
    def attr_login_time(self, new_login_time):
        if self.login_time == new_login_time:
            return

        self.login_time = new_login_time
        self.dfp.add_db_flag("login_time")

    # active_time
    @property
    def attr_active_time(self):
        return self.active_time

    @attr_active_time.setter
    def attr_active_time(self, new_active_time):
        if self.active_time == new_active_time:
            return

        self.active_time = new_active_time
        self.dfp.add_db_flag("active_time")

    # level
    @property
    def attr_level(self):
        finished_orders = self.attr_finished_accept + self.attr_finished_apply

        cur_lvel_idx = 0
        for i, lvl_req in enumerate(LEV_REQ):
            if finished_orders > lvl_req:
                cur_lvel_idx = i
            else:
                break

        return LEVEL[cur_lvel_idx]

    @property
    def is_seal(self):
        """
        是否封号
        :return:
        """
        return self.attr_stat == SEALED

    @property
    def is_active(self):
        """
        是否激活
        :return:
        """
        return self.attr_stat == ACTIVED