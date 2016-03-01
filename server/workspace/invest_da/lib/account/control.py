#!/usr/bin/python2.7
# coding=utf-8
"""
Created on 2015-12-15

@author: Jay
"""
from utils.interfaces.common import IManager
from utils.meta.singleton import Singleton
from model import Account
from invest_da.db import DBAccountInst
import time


class AccountMgr(IManager):
    __metaclass__ = Singleton

    def __init__(self):
        self.__id_to_dic = {}
        self.__init_data_ls = None
        self.__system_account = None
        self.__phone_ls = []

    def init(self, data_ls):
        self.__init_data_ls = data_ls
        self.__id_to_dic = {}
        self.__system_account = None

        for dic in data_ls:
            self.__add_account_2_mem(dic)

    def update(self, curtime):
        [account_obj.update(curtime) for account_obj in self.__id_to_dic.values()]


    def db_pick(self, data_ls):
        """
        db 序列化
        :param data_ls:
        :return:
        """
        return data_ls

    def db_unpick(self, data_ls, *args):
        """
        db 反序列化
        :param data_ls:
        :return:
        """
        return data_ls

    def __add_account_2_mem(self, data):
        # add id_to_service_dic
        account = Account(db_update_fun=DBAccountInst.update_ls, **data)
        self.__id_to_dic[str(data['id'])] = account
        self.__phone_ls.append(data['phone'])

    def create_account(self, data_dic):
        """
        创建账号
        data_dic:account, passwd,
        id_card, email, phone,
        leader_id,
        bank, bank_address, bank_account, bank_name,
        wechat, alipay
        """
        data_dic['create_time'] = time.time()

        DBAccountInst.insert_ls([data_dic])

        db_data_dic = DBAccountInst.db_instance.read_db("select * from %s where id = %s" % (DBAccountInst.table_name, data_dic['id']))
        assert db_data_dic
        self.__add_account_2_mem(db_data_dic[0])

    def get_data_by_id(self, id):
        return self.__id_to_dic.get(str(id), None)

    def get_all_ids(self):
        return self.__id_to_dic.keys()

    @property
    def system_account(self):
        return self.__system_account

    def is_id_exist(self, tid):
        """
        判断id是否存在
        :param tid: 检测的id
        :return:
        """
        return str(tid) in self.__id_to_dic.keys()

