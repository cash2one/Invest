#!/usr/bin/python2.7
# coding=utf-8
"""
Created on 2016-3-2

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


# 贷款产品
LOAN_PRODUCT=[
    LP_HOUSE_MORTGAGE,   # 房产抵押贷款
    LP_CAR_OWN_MORTGAGE, # 汽车抵押贷款
    LP_NEW_NOT_MORTGAGE, # 新一贷无抵押贷款
    LP_XIAMEN_PRI_LOAN,  # 厦门私借
    LP_CAR_USE_MORTGAGE, # 车抵贷(押车)
    LP_INSURANCE_LOAN,   # 保险保单贷款
] = xrange(0, 6)

# 贷款业务
LOAN_BUSINESS=[
    LB_PINGAN_XINYI_DAI,        # 平安新一贷
    LB_SMALL_PRIVATE_CONSUME,   # 个人小额消费贷款
    LB_HOUSE_MORTGAGE_CONSUME,  # 房产抵押消费
    LB_SECOND_HAND_HOUSE_LOAN,  # 二手房贷款
    LB_FIRST_HAND_HOUSE_LOAN,   # 一手房贷款
    LB_CAR_MORTGAGE_HOUSE_LOAN, # 汽车抵押贷款
] = xrange(0, 6)