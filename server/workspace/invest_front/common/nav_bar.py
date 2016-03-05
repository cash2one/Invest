#!/usr/bin/python2.7
# coding=utf-8
"""
Created on 2016-3-3

@author: Jay
"""

# 导航栏名字ID列表
LOAN_NAV_BAR_ID_LS = [
    # index
    LBL_ROOT,
    LBL_KNOWLEDGE,
    LBL_CASE,
    LBL_PROBLEM,
    LBL_LOGIN,

    # about
    LBL_ABOUT,
    LBL_CONTACT,
    LBL_COOPERATION,
    LBL_RECRUIT,

    # user
    LBL_U_BUSIMGR,          # 业务管理
    LBL_U_DATA,             # 个人资料
    LBL_U_CO_EMAIL,         # 公司邮箱
    LBL_U_NOTICE,           # 网站公告

    # user - 业务员管理
    LBL_UB_LIST,            # 业务列表
    LBL_UB_APPLY,           # 提交贷款
] = xrange(0, 15)

# INDEX导航栏详细信息列表
INDEX_NAV_BAR_DIC = {
    # index
    LBL_ROOT:       {"idx": 0, "des": "首页",     "url": "/",                "html": "/index/index.html"},
    LBL_KNOWLEDGE:  {"idx": 1, "des": "贷款攻略", "url": "/knowledge",        "html": "/util/list.html"},
    LBL_CASE:       {"idx": 2, "des": "贷款案例", "url": "/case",             "html": "/util/list.html"},
    LBL_PROBLEM:    {"idx": 3, "des": "常见问题", "url": "/problem",          "html": "/util/list.html"},
    LBL_ABOUT:      {"idx": 4, "des": "关于宏圆", "url": "/about",            "html": "/about/about.html"},
    LBL_LOGIN:      {"idx": 5, "des": "经理登录", "url": "/login",            "html": "/user/login.html"},
}

# ABOUT导航栏详细信息列表
ABOUT_NAV_BAR_DIC = {
    LBL_ABOUT:      {"idx": 0, "des": "关于我们", "url": "/about",            "html": "/about/about.html"},
    LBL_CONTACT:    {"idx": 1, "des": "联系我们", "url": "/about/contact",     "html": "/about/contact.html"},
    LBL_COOPERATION:{"idx": 2, "des": "商务合作", "url": "/about/cooperation", "html": "/about/cooperation.html"},
    LBL_RECRUIT:    {"idx": 3, "des": "招贤纳士", "url": "/about/recruit",     "html": "/about/recruit.html"},
}

# 用户管理信息列表
USER_NAV_BAR_DIC = {
    LBL_U_BUSIMGR:  {"idx": 0, "des": "业务管理", "url": "/u_busimgr"},
    LBL_U_DATA:     {"idx": 1, "des": "个人资料", "url": "/u_data",          "html": "/user/u_data.html"},
    LBL_U_CO_EMAIL: {"idx": 2, "des": "公司邮箱", "url": "/u_co_email",      "html": "/user/u_co_mail.html"},
    LBL_U_NOTICE:   {"idx": 3, "des": "网站公告", "url": "/u_notice",        "html": "/user/u_notice.html"},
}

# 用户管理-业务管理信息列表
USER_BUSIMGR_BAR_DIC = {
    LBL_UB_LIST:   {"idx": 0, "des": "业务列表", "url": "/u_busimgr/list",    "html": "/user/u_busimgr_list.html"},
    LBL_UB_APPLY:  {"idx": 1, "des": "提交贷款", "url": "/u_busimgr/apply",   "html": "/user/u_busimgr_apply.html"},
}

LOAN_NAV_BAR_DIC = {}
LOAN_NAV_BAR_DIC.update(INDEX_NAV_BAR_DIC)
LOAN_NAV_BAR_DIC.update(ABOUT_NAV_BAR_DIC)
LOAN_NAV_BAR_DIC.update(USER_NAV_BAR_DIC)
LOAN_NAV_BAR_DIC.update(USER_BUSIMGR_BAR_DIC)
