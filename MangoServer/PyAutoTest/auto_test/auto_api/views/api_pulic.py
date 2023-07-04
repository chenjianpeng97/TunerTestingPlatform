# -*- coding: utf-8 -*-
# @Project: auto_test
# @Description: 
# @Time   : 2023-02-17 21:39
# @Author : 毛鹏
from rest_framework import serializers
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from PyAutoTest.auto_test.auto_api.data_producer.run_api_send import RunApiSend
from PyAutoTest.auto_test.auto_api.models import ApiPublic
from PyAutoTest.enums.api_enum import PublicTypeEnum, ClientEnum
from PyAutoTest.settings import DRIVER, SERVER
from PyAutoTest.utils.view_utils.model_crud import ModelCRUD
from PyAutoTest.utils.view_utils.view_tools import enum_list


class ApiPublicSerializers(serializers.ModelSerializer):
    class Meta:
        model = ApiPublic
        fields = '__all__'


class ApiPublicCRUD(ModelCRUD):
    model = ApiPublic
    queryset = ApiPublic.objects.all()
    serializer_class = ApiPublicSerializers


class ApiPublicViews(ViewSet):

    @action(methods=['get'], detail=False)
    def client_refresh(self, request: Request):
        data, res = RunApiSend(request.query_params.get("username")).public_args_data()
        return Response({
            'code': 200,
            'msg': f'刷新{DRIVER}api自动化数据成功',
            'data': data
        }) if res else Response({
            'code': 300,
            'msg': f'刷新失败，请确保{DRIVER}已连接{SERVER}',
            'data': data
        })

    @action(methods=['get'], detail=False)
    def get_public_type(self, request):
        """
        获取公共类型
        :param request:
        :return:
        """
        return Response({
            'code': 200,
            'msg': '获取类型成功',
            'data': enum_list(PublicTypeEnum)
        })

    @action(methods=['get'], detail=False)
    def get_end_type(self, request):
        """
        获取客户端类型
        :param request:
        :return:
        """
        return Response({
            'code': 200,
            'msg': '获取类型成功',
            'data': enum_list(ClientEnum)
        })
