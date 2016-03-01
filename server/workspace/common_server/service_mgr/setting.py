# coding=utf-8
"""
Created on 2015-4-22

@author: Jay
"""
# 逻辑服务类型
LOGIC_SERVICE_TYPE = [
    ST_SERVICE_MGR,
    ST_INVEST_FRONT,
    ST_INVEST_DA,
    ST_INVEST_GM,
] = [
    "service_mgr",
    "invest_front",
    "invest_da",
    "invest_gm",
]

SERVICE_TYPE = ST_SERVICE_MGR
VERSION = "0.0.1"

# 内网默认配置
DB_HOST = "192.168.1.117"
DB_PORT = 3306
DB_NAME = "invest_service_mgr"
DB_USER = "system"
DB_PWD = "system"