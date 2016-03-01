#!/usr/bin/python2.7
# coding=utf-8
"""
Created on 2015-12-30

@author: Jay
"""
MUST_KEY_SET = set(["id", "passwd","email", "phone",])

OPTION_KEY_SET = set(["create_time",
                      "login_time",
                      "active_time", "stat",])

DB_KEY_SET = set(["id"])

MEM_KEY_SET = set(["level"])

PRIVATE_KEY_SET = set(["passwd", "create_time", "active_time", "stat"])
PRIVATE_KEY_SET |= MEM_KEY_SET

KEY_SET = MUST_KEY_SET | OPTION_KEY_SET | DB_KEY_SET | MEM_KEY_SET

# 状态
STAT =[
    NORMAL,    # 正常
    SEALED     # 封号
] = xrange(0, 2)