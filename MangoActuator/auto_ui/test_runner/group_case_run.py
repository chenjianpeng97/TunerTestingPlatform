# -*- coding: utf-8 -*-
# @Project: auto_test
# @Description: 
# @Time   : 2023/5/4 14:33
# @Author : 毛鹏

from typing import Optional

from auto_ui.test_runner.case_run_method import CaseRunMethod
from auto_ui.test_runner.element_runner.web import WebRun


class GroupCaseRun:

    @classmethod
    def group_case_decompose(cls, data: dict):
        """
        分发用例给不同的驱动进行执行
        @param data: 用例列表
        @return:
        """
        GroupCaseRunR().group_obj(data)


class GroupCaseRunR(CaseRunMethod):

    def __init__(self):
        super().__init__()
        self.web: Optional[WebRun] = None

    def group_obj(self, group_case: dict):
        print(f'GroupCaseRunR内存地址是：{id(self)}')
        # 获取组用例名称和组用例对象
        for group_name, group_value in group_case.items():
            # 获取每个用例
            for case_one in group_value:
                # 分给用例分发去执行
                self.distribute_to_drivers(case_one)
        self.close()

    def test_res(self, response):
        print('用例执行结果', response)

    def close(self):
        self.web.page.close()


if __name__ == '__main__':
    pass