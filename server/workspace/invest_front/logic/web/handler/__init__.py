# coding=utf-8
"""
Created on 2015-4-22

@author: Jay
"""
from invest_front.setting import *

def get_common_dic(http_handler):
    IndexNavBarLs = INDEX_NAV_BAR_DIC.values()
    IndexNavBarLs.sort(key=lambda dic: dic['idx'])
    AboutNavBarLs = ABOUT_NAV_BAR_DIC.values()
    AboutNavBarLs.sort(key=lambda dic: dic['idx'])
    return {'IndexNavBarLs': IndexNavBarLs,
            'AboutNavBarLs': AboutNavBarLs,
            'CurIndexNavBarUrl': "/".join(http_handler.request.uri.split("/")[0:2]),
            'CurNavBarUrl': http_handler.request.uri}
