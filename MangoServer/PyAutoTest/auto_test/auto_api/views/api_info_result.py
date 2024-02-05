# -*- coding: utf-8 -*-
# @Project: auto_test
# @Description: 
# @Time   : 2023-11-13 10:42
# @Author : 毛鹏
import logging

from rest_framework import serializers
from rest_framework.viewsets import ViewSet

from PyAutoTest.auto_test.auto_api.models import ApiInfoResult
from PyAutoTest.auto_test.auto_api.views.api_case import ApiCaseSerializers
from PyAutoTest.auto_test.auto_api.views.api_info import ApiInfoSerializers
from PyAutoTest.tools.view_utils.model_crud import ModelCRUD

logger = logging.getLogger('api')


class ApiInfoResultSerializers(serializers.ModelSerializer):
    create_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', read_only=True)
    update_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', read_only=True)

    class Meta:
        model = ApiInfoResult
        fields = '__all__'


class ApiInfoResultSerializersC(serializers.ModelSerializer):
    create_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', read_only=True)
    update_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', read_only=True)
    case = ApiCaseSerializers(read_only=True)
    api_info = ApiInfoSerializers(read_only=True)

    class Meta:
        model = ApiInfoResult
        fields = '__all__'


class ApiInfoResultCRUD(ModelCRUD):
    model = ApiInfoResult
    queryset = ApiInfoResult.objects.all()
    serializer_class = ApiInfoResultSerializersC
    serializer = ApiInfoResultSerializers


class ApiInfoResultViews(ViewSet):
    model = ApiInfoResult
    serializer_class = ApiInfoResultSerializers