# -*- coding: utf-8 -*-
# @Project: MangoServer
# @Description: 
# @Time   : 2023-03-25 18:53
# @Author : 毛鹏
from rest_framework import serializers
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.viewsets import ViewSet

from PyAutoTest.auto_test.auto_ui.models import UiCaseResult, UiPageStepsResult
from PyAutoTest.auto_test.auto_user.views.project import ProjectSerializers
from PyAutoTest.auto_test.auto_user.views.project_module import ProjectModuleSerializers
from PyAutoTest.auto_test.auto_user.views.user import UserSerializers
from PyAutoTest.tools.response_data import ResponseData
from PyAutoTest.tools.view_utils.model_crud import ModelCRUD


class UiCaseResultSerializers(serializers.ModelSerializer):
    create_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', read_only=True)
    update_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', read_only=True)

    class Meta:
        model = UiCaseResult
        fields = '__all__'


class UiCaseResultSerializersC(serializers.ModelSerializer):
    create_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', read_only=True)
    update_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', read_only=True)
    project = ProjectSerializers(read_only=True)
    module_name = ProjectModuleSerializers(read_only=True)
    case_people = UserSerializers(read_only=True)

    class Meta:
        model = UiCaseResult
        fields = '__all__'


class UiCaseResultCRUD(ModelCRUD):
    model = UiCaseResult
    queryset = UiCaseResult.objects.all()
    serializer_class = UiCaseResultSerializersC
    serializer = UiCaseResultSerializers


class UiCaseResultViews(ViewSet):
    model = UiCaseResult
    serializer_class = UiCaseResultSerializers

    @action(methods=['get'], detail=False)
    def suite_get_case(self, request: Request):
        case_result = UiCaseResult.objects.filter(test_suite_id=request.query_params.get('test_suite_id'))
        data = []
        for i in case_result:
            page_steps_result = UiPageStepsResult.objects.filter(
                test_suite_id=request.query_params.get('test_suite_id'),
                case_id=i.case_id)
            case_result_obj = {
                'title': i.case_name,
                'key': f'{"{"}"test_suite_id":{i.test_suite_id},"ui_case_result":{i.id},"case_id":{i.case_id}{"}"}',
                'children': [
                    {'title': e.page_step_name,
                     'key': f'{"{"}"test_suite_id":{e.test_suite_id},"page_steps_result":{e.id},"case_id":{i.case_id},"page_step_id":{e.page_step_id}{"}"}',
                     'children': []
                     } for e in page_steps_result]
            }
            data.append(case_result_obj)
        summary = [
            {'name': '用例总数', 'value': case_result.count()},
            {'name': '成功', 'value': case_result.filter(status=1).count()},
            {'name': '警告', 'value': case_result.filter(status=2).count()},
            {'name': '失败', 'value': case_result.filter(status=0).count()}
        ]
        return ResponseData.success('查询不同类型结果成功', {'data': data, 'summary': summary})

    @action(methods=['get'], detail=False)
    def get_case_res(self, request: Request):
        data = self.model.objects.filter(test_suite_id=request.query_params.get('test_suite_id'))
        return ResponseData.success('查询不同类型结果成功', data)