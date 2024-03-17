# -*- coding: utf-8 -*-
# @Project: MangoActuator
# @Description: 
# @Time   : 2023/4/6 13:36
# @Author : 毛鹏
from autotest.ui.driver.android.a_assertion import UiautomatorAssertion
from autotest.ui.driver.web.assertion import PlaywrightAssertion
from tools.assertion.public_assertion import *


class Assertion(WhatIsItAssertion, ContainAssertion, MatchingAssertion, WhatIsEqualToAssertion, PlaywrightAssertion,
                UiautomatorAssertion):

    @classmethod
    def get_methods(cls):
        """
        获取所有子类方法
        :return:
        """
        class_list = []
        for subclass in cls.__bases__:
            func_list = []
            for method_name in dir(subclass):
                if not method_name.startswith("__"):
                    method = getattr(subclass, method_name)
                    if callable(method):
                        func_list.append({
                            'label': method_name,
                            'value': method.__doc__
                        })
            if func_list:
                if subclass.__name__ == 'PlaywrightAssertion':
                    class_list.append({'title': 'WEB元素断言', 'func_list': func_list})
                elif subclass.__name__ == 'UiautomatorAssertion':
                    class_list.append({'title': '安卓元素断言', 'func_list': func_list})
                else:
                    class_list.append({'title': subclass.__doc__, 'func_list': func_list})
                func_list = []
        return class_list


if __name__ == '__main__':
    import json

    print(json.dumps(Assertion.get_methods(), ensure_ascii=False))
