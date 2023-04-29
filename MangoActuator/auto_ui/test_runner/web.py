# -*- coding: utf-8 -*-
# @Project: auto_test
# @Description: 
# @Time   : 2023/3/23 11:29
# @Author : 毛鹏
from utlis.cache.data_cleaning import DataCleaning
from enum_class.ui_enum import OpeType, WebEleExp
from auto_ui.web_base.playwright_obj import WebDevice
from utlis.logs.log_control import ERROR
from playwright.sync_api import Locator

from utlis.nuw_logs import NewLog


class WebRun(WebDevice, DataCleaning):

    def __init__(self):
        super().__init__()
        self.case_name = ''
        self.ope_type = ''
        self.ass_type = ''
        self.ope_value = ''
        self.ass_value = ''
        self.ele_name = ''
        self.ele_page_name = ''
        self.ele_exp = 0
        self.ele_loc = ''
        self.ele_sleep = 0
        self.ele_sub = 0
        self.ope_value_key = None
        self.ele_opt_res = {'ele_name': self.ele_name,  #
                            'existence': str or bool,  #
                            'state': 0,  #
                            'case_id': self.case_name,  #
                            'case_group_id': '',
                            'team_id': '',
                            'test_obj_id': '',  #
                            'msg': '',  #
                            'picture_path': ''}  #

    def open_url(self, url: str, case_name):
        """
        记录用例名称，并且打开url
        @param url: url
        @param case_name: 用例名称
        @return:
        """
        self.case_name = case_name
        self.wait_for_timeout(1 * 1000)
        self.goto(url)
        self.ele_opt_res['test_obj_id'] = url

    def ele_along(self, case_dict: dict) -> dict:
        """
        将数据设为变量，并对这个元素进行操作
        @param case_dict: 被操作元素对象
        @return: 返回是否操作成功
        """
        for key, value in case_dict.items():
            setattr(self, key, value)
        try:
            if self.ele_name != 'url':
                ele_obj = self.__find_ele(case_dict)
                if ele_obj:
                    self.action_element(ele_obj)
                else:
                    return self.ele_opt_res
        except Exception as e:
            ERROR.logger.error(f'元素操作失败，请检查内容\n'
                               f'报错信息：{e}\n'
                               f'元素对象：{case_dict}\n')
            path = rf'{NewLog.get_log_screenshot()}\{self.ele_name + self.get_deta_hms()}.jpg'
            self.ele_opt_res['picture_path'] = self.screenshot(path)
        return self.ele_opt_res

    def action_element(self, ele_obj: Locator) -> None:
        """
            处理元素的一些事件，包括点击，输入，移动
        @param ele_obj: 元素对象，只能是一个
        @return:
        """
        # 点击
        if self.ope_type == OpeType.CLICK.value:
            self.click(ele_obj)
            self.ele_opt_res['state'] = 1
        # 输入
        elif self.ope_type == OpeType.INPUT.value:
            self.input(ele_obj, value=self.__input_value())
            self.ele_opt_res['state'] = 1
        # 等待
        if self.ele_sleep:
            self.wait_for_timeout(self.ele_sleep * 1000)

    def __find_ele(self, case_dict: dict) -> Locator or bool:
        """
        基于playwright的元素查找
        @param case_dict:
        @return:
        """
        if self.ele_loc:
            # 处理元素并查找
            match self.ele_exp:
                case WebEleExp.XPATH.value:
                    ele = self.page.locator(f'xpath={self.ele_loc}')
                case WebEleExp.PLACEHOLDER.value:
                    ele = self.page.get_by_placeholder(self.ele_loc)
                case WebEleExp.TEXT.value:
                    ele = self.page.get_by_text(self.ele_loc, exact=True)
                case WebEleExp.CSS.value:
                    ele = self.page.locator(f'css={self.ele_loc}')
                case WebEleExp.ID.value:
                    ele = self.page.locator(f'id={self.ele_loc}')
                case _:
                    ERROR.logger.error(f'没有更多元素，请先联系管理员增加元素定位方式！{self.ele_loc}')
                    ele = None
            # 获取元素的文本或元素下标进行断言
            if not ele:
                ERROR.logger.error(f'元素操作失败，请检查内容\n'
                                   f'元素对象：{case_dict}\n')
                self.screenshot(self.ele_name)
                self.ele_opt_res['existence'] = '不存在'
                return False
            self.ele_opt_res['existence'] = True
            print(ele.count(), self.ele_name)
            return ele.nth(0 if self.ele_sub is None else self.ele_sub)
        else:
            self.ele_opt_res['existence'] = '不存在'
            ERROR.logger.error(f'元素为空，无法定位，请检查元素表达式是否为空！元素对象：{case_dict}')
            return False

    def __find_ele1(self, case_dict):
        """
        查找元素，drissoionpage框架的元素查找
        @return:
        """
        if self.ele_loc:
            # 处理元素并查找
            ele = self.eles(self.__ele_add())
            # 获取元素的文本或元素下标进行断言
            if not ele:
                ERROR.logger.error(f'元素操作失败，请检查内容\n'
                                   f'元素对象：{case_dict}\n')
                self.screenshot(self.ele_name)
                self.ele_opt_res['existence'] = '不存在'
                return False
            self.ele_opt_res['existence'] = str(len(ele))
            el = ele[0 if self.ele_sub is None else self.ele_sub]
            return el
        else:
            self.ele_opt_res['existence'] = '不存在'
            ERROR.logger.error('元素为空，无法定位，请检查元素表达式是否为空！')
            return False

    def __ele_add(self):
        """
        修改ele元素，drissoionpage框架
        :return:
        """
        # exp_type = [{0: "xpath:"}, {1: "#"}, {2: "@name"}, {3: "text="}]
        for i in WebEleExp.__doc__.split('，'):
            for key, value in eval(i).items():
                if key == self.ele_exp:
                    return value + self.ele_loc

    def __input_value(self):
        """
        输入依赖解决
        @return:
        """
        return self.case_input_data(self.case_name, self.ele_name, self.ope_value_key, self.ope_value)
