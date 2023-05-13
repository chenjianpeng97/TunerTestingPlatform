# -*- coding: utf-8 -*-
# @Project: auto_test
# @Description: 处理所有用例的数据
# @Time   : 2023-03-12 10:54
# @Author : 毛鹏

from PyAutoTest.auto_test.auto_system.models import TestObject
from PyAutoTest.auto_test.auto_ui.models import UiCase, RunSort, UiConfig
from PyAutoTest.auto_test.auto_ui.models import UiCaseGroup
from PyAutoTest.auto_test.auto_ui.ui_tools.enum import DevicePlatform, BrowserType


class CaseData:

    def __init__(self, user):
        self.user = user

    def group_cases(self, group: UiCaseGroup) -> dict:
        """
        根据用例组的列表，返回所有的测试对象
        @param group: UiCaseGroup对象，一条数据
        @return:
        """
        case_single = {group.name: []}
        for case_id in eval(group.case_id):
            case_single.get(group.name).append(self.data_ui_case(group.test_obj.id, case_id))
        return case_single

    def data_ui_case(self, test_obj: int, case_id: int) -> dict:
        """
        根据test对象和用例ID返回一个UI测试对象回去
        @param test_obj: 测试环境id
        @param case_id: 用例id
        @return: 返回一个数据处理好的测试对象
        """
        case_ = UiCase.objects.get(id=case_id)
        run_sort = RunSort.objects.filter(case=case_.id).order_by('run_sort')
        case_strip = {'case_id': case_.id, 'case_name': case_.name, }
        if case_.case_type == DevicePlatform.WEB.value:
            # 如果是web用例，则写入浏览器的端口，浏览器打开地址，type 执行用例url和浏览器的类型
            case_strip['local_port'], case_strip['browser_path'] = self.__get_web_config()
            case_strip['type'] = DevicePlatform.WEB.value
            case_strip['case_url'] = TestObject.objects.get(id=test_obj).value + run_sort[0].el_page.url
            case_strip['browser_type'] = BrowserType.CHROMIUM.value
        elif case_.case_type == DevicePlatform.ANDROID.value:
            # 如果是安卓用例，则写入设备，app和type
            case_strip['equipment'] = self.__get_app_config()
            case_strip['package'] = TestObject.objects.get(id=test_obj).value
            case_strip['type'] = DevicePlatform.ANDROID.value
        elif case_.case_type == DevicePlatform.IOS.value:
            pass
        elif case_.case_type == DevicePlatform.DESKTOP.value:
            pass
        case_data = []
        for i in run_sort:
            if i.el_name is not None:
                case_data.append({
                    'ope_type': i.ope_type,
                    'ass_type': i.ass_type,
                    'ope_value': i.ope_value,
                    'ass_value': i.ass_value,
                    'ele_name': i.el_name.name,
                    'ele_page_name': i.el_page.name,
                    'ele_exp': i.el_name.exp,
                    'ele_loc': i.el_name.loc,
                    'ele_sleep': i.el_name.sleep,
                    'ele_sub': i.el_name.sub,
                    'ope_value_key': i.ope_value_key
                })
        case_strip['case_data'] = case_data
        return case_strip

    def __get_web_config(self) -> tuple:
        user_ui_config = UiConfig.objects.get(user_id=self.user)
        return user_ui_config.local_port, user_ui_config.browser_path

    def __get_app_config(self) -> tuple:
        user_ui_config = UiConfig.objects.get(user_id=self.user)
        return user_ui_config.equipment
