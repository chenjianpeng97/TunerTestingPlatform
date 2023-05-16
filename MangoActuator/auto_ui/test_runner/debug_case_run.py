# -*- coding: utf-8 -*-
# @Project: auto_test
# @Description: 
# @Time   : 2023/3/23 11:31
# @Author : 毛鹏
import asyncio

from auto_ui.test_runner.case_run_method import CaseRunMethod
from utils.decorator.singleton import singleton


@singleton
class CaseDistribution(CaseRunMethod):
    """
    用例分发
    """

    def debug_case_distribution(self, data: dict):
        """
        处理调试用例，开始用例对象，并调用分发用例方法
        @param data:
        @return:
        """
        asyncio.run(self.distribute_to_drivers(data))
        # self.distribute_to_drivers(data)
        # ResultMain.web_notice(200, '调试用例执行完成，请检查用例执行结果！')

    def close(self):
        self.web.page.close()
