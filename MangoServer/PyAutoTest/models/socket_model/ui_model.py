# -*- coding: utf-8 -*-
# @Project: MangoServer
# @Description:
# @Time   : 2023-05-28 18:40
# @Author : 毛鹏
from pydantic import BaseModel

from PyAutoTest.models.tools_model import MysqlDBModel


class UiPublicModel(BaseModel):
    create_time: str
    update_time: str
    project: int
    name: str
    key: str
    value: str
    status: int


class InputValueModel(BaseModel):
    locating: str
    input_value: str | None

    @classmethod
    def create_empty(cls) -> "InputValueModel":
        return cls(locating=str, input_value=None)


class ElementModel(BaseModel):
    type: int
    ele_name_a: str | None
    ele_name_b: str | None
    ele_loc_a: str | None
    ele_loc_b: str | None
    ele_exp: int | None
    ele_sleep: int | None
    ele_sub: int | None
    ope_type: str | None
    ope_value: dict | None
    is_iframe: int | None
    ass_type: str | None
    ass_value: dict | None


class WEBConfigModel(BaseModel):
    """ web启动配置 """
    browser_type: int
    browser_port: str | None
    browser_path: str | None
    is_headless: int | None


class AndroidConfigModel(BaseModel):
    equipment: str


class PageStepsModel(BaseModel):
    page_steps_id: int
    page_step_name: str
    host: str
    url: str
    type: int
    config: AndroidConfigModel | WEBConfigModel
    mysql_config: MysqlDBModel | None
    page_ele_list: list[ElementModel] = []

    @classmethod
    def create_empty(cls):
        pass


class CaseModel(BaseModel):
    case_id: int
    case_name: str
    project: int
    module_name: str
    case_people: str
    case_cache_data: list[list[dict]] | list
    case_cache_ass: list[list[dict]] | list
    case_list: list[PageStepsModel]


class ElementResultModel(BaseModel):
    test_suite_id: int | None
    case_id: int | None
    page_step_id: int | None
    # 元素的名称
    ele_name_a: str | None
    ele_name_b: str | None
    # 元素个数
    ele_quantity: int
    # 提示语
    msg: str | None
    # 错误截图路径
    picture_path: str | None
    # 测试结果
    status: int

    loc: str | None
    exp: int | None
    sleep: int | None
    sub: int | None

    ope_type: str | None
    ope_value: dict | str | None
    ass_type: str | None
    ass_value: dict | None


class PageStepsResultModel(BaseModel):
    test_suite_id: int | None
    case_id: int | None
    # 测试步骤ID
    page_step_id: int
    # 测试步骤名称
    page_step_name: str
    # 测试结果
    status: int
    ele_result_list: list[ElementResultModel]


class CaseResultModel(BaseModel):
    test_suite_id: int
    case_id: int
    case_name: str
    module_name: str
    case_people: str
    # 测试对象
    test_obj: str
    case_cache_ass: list[list[dict]] | list
    status: int
    case_res_list: list[PageStepsResultModel]


class TestSuiteModel(BaseModel):
    id: int
    type: int
    project: int
    error_message: str | None
    run_status: int
    status: int | None
    case_list: list[CaseModel] | None
    result_list: list[CaseResultModel] | None