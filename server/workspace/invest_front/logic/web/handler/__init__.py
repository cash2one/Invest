# coding=utf-8
"""
Created on 2015-4-22

@author: Jay
"""
from invest_front.common.nav_bar import INDEX_NAV_BAR_DIC, ABOUT_NAV_BAR_DIC

def get_common_dic(http_handler, MainNavBarDic=INDEX_NAV_BAR_DIC):
    """
    获取全局的导航条数据信息
    :param http_handler: http handler
    :param MainNavBarDic:  默认的主导航条信息字典
    :return:
    """
    MainNavBarLs = MainNavBarDic.values()
    MainNavBarLs.sort(key=lambda dic: dic['idx'])
    AboutNavBarLs = ABOUT_NAV_BAR_DIC.values()
    AboutNavBarLs.sort(key=lambda dic: dic['idx'])
    return {'MainNavBarLs': MainNavBarLs,
            'AboutNavBarLs': AboutNavBarLs,
            'CurMainNavBarUrl': "/".join(http_handler.request.uri.split("/")[0:2]),
            'CurNavBarUrl': http_handler.request.uri}
