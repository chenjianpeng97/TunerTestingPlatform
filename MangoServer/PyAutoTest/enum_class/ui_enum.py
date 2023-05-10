# -*- coding: utf-8 -*-
# @Project: auto_test
# @Description: 
# @Time   : 2022-12-06 21:05
# @Author : 毛鹏
from enum import Enum


class DevicePlatform(Enum):
    """ {"0": "web"}，{"1": "安卓"}，{"2": "IOS"}，{"3": "桌面PC"} """
    WEB = 0
    ANDROID = 1
    IOS = 2
    DESKTOP = 3


class BrowserType(Enum):
    CHROMIUM = 0
    FIREFOX = 1
    WEBKIT = 2


class EnvironmentEnum(Enum):
    """ {"0": "测试环境"}，{"1": "预发环境"}，{"2": "生产环境"} """
    TEST = 0
    PRE = 1
    PRO = 2


class OpeType(Enum):
    """ {"0": "打开url"}，{"1": "点击"}，{"2": "输入"}，{"3": "截图"} """
    get = 0
    CLICK = 1
    INPUT = 2
    CHART = 3


class Assertions(Enum):
    """ {"0": "-"}，{"1": "相等"}，{"2": "比元素大"}，{"3": "比元素小"} """
    NULL = 0
    EQUAL = 1
    LARGE = 2
    SMALL = 3


class ElementExp(Enum):
    """ {0: "XPATH"}，{1: "ID"}，{2: "NAME"}，{3: "TEXT"}，{4: "占位符"}，{5: "CSS"}，{11: "DESCRIPTION"}，{12: "BOUNDS"}，{13: "百分比坐标点击"} """
    XPATH = 0
    ID = 1
    NAME = 2
    TEXT = 3
    PLACEHOLDER = 4
    CSS = 5
    # APP专属
    DESCRIPTION = 11
    BOUNDS = 12
    PERCENTAGE = 13


class State(Enum):
    """ 0 是未测试，1 是失败，2 是通过"""
    NOT = 0
    FAIL = 1
    ADOPT = 2


if __name__ == '__main__':
    r = []
    for i in OpeType.__doc__.split("，"):
        for key, value in eval(i).items():
            r.append({
                'type': key,
                'dec': value
            })
    print(r)