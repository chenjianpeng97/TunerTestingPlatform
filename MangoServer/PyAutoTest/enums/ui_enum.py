# -*- coding: utf-8 -*-
# @Project: MangoServer
# @Description: 
# @Time   : 2022-12-06 21:05
# @Author : 毛鹏
from enum import Enum


class DriveTypeEnum(Enum):
    """ {0: "WEB"}，{1: "安卓"} """
    WEB = 0
    ANDROID = 1


class BrowserTypeEnum(Enum):
    """ {0: "谷歌浏览器"}，{1: "EDGE"}，{2: "火狐"}，{3: "WEBKIT"} """
    CHROMIUM = 0
    EDGE = 1
    FIREFOX = 2
    WEBKIT = 3


class UiPublicTypeEnum(Enum):
    """ {"0": "CUSTOM"}，{"1": "SQL"}，{"2": "HEAD"} """
    CUSTOM = 0
    SQL = 1


class ElementExpEnum(Enum):
    """ {0: "W_XPATH"}，{1: "W_TestID"}，{3: "W_文本"}，{4: "W_占位符"}，{5: "W_标签"}，{6: "W_标题"}，{7: "W_ROLE"}，{8: "W_AIT_TEXT"}，{11: "W_TITLE"}，{12: "A_BOUNDS"}，{13: "A_百分比坐标点击"} """
    XPATH = 0
    TEST_ID = 1
    TEXT = 3
    PLACEHOLDER = 4
    LABEL = 5
    TITLE = 6
    ROLE = 7
    AIT_TEXT = 8

    # APP专属
    DESCRIPTION = 11
    BOUNDS = 12
    PERCENTAGE = 13


class StatusEnum(Enum):
    """ 0 是未测试，1 是失败，2 是通过"""
    NOT = 0
    FAIL = 1
    ADOPT = 2


class DevicePlatform(Enum):
    """ 什么端 """
    WEB = 0
    ANDROID = 1
    IOS = 2
    DESKTOP = 3
