# -*- coding: utf-8 -*-
# @Project: MangoServer
# @Description:
# @Time   : 2023-06-04 12:24
# @Author : 毛鹏
import logging
import re

from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.viewsets import ViewSet

from PyAutoTest.auto_test.auto_system.consumers import ChatConsumer
from PyAutoTest.auto_test.auto_system.service.scheduled_tasks.tasks import Tasks
from PyAutoTest.enums.tools_enum import ClientTypeEnum
from PyAutoTest.exceptions import MangoServerError
from PyAutoTest.models.socket_model import SocketDataModel, QueueModel
from PyAutoTest.tools.data_processor import ObtainRandomData
from PyAutoTest.tools.redis.redis import Cache
from PyAutoTest.tools.view.response_data import ResponseData
from PyAutoTest.tools.view.response_msg import *

log = logging.getLogger('system')


class SystemViews(ViewSet):

    @action(methods=['get'], detail=False)
    def test_func(self, request: Request):
        Tasks.timing(request.query_params.get('id'))
        return ResponseData.success(RESPONSE_MSG_0061, )

    @action(methods=['get'], detail=False)
    def common_variable(self, request: Request):
        """
        返回公共变量页
        @param request:
        @return:
        """
        return ResponseData.success(RESPONSE_MSG_0061, ObtainRandomData.get_methods())

    @action(methods=['get'], detail=False)
    def random_data(self, request: Request):
        name = request.GET.get("name")
        res1 = name.replace("${", "")
        name: str = res1.replace("}", "").strip()
        if not name:
            return ResponseData.fail(RESPONSE_MSG_0063)
        match = re.search(r'\((.*?)\)', name)
        if match:
            try:
                return ResponseData.success(RESPONSE_MSG_0062, str(ObtainRandomData().regular(name)))
            except MangoServerError as error:
                return ResponseData.fail((error.code, error.msg), )
        else:
            if Cache().read_data_from_cache(name):
                return ResponseData.success(RESPONSE_MSG_0062, Cache().read_data_from_cache(name))
            else:
                return ResponseData.fail(RESPONSE_MSG_0060)

    @action(methods=['get'], detail=False)
    def get_cache_key_value(self, request: Request):
        socket_data = SocketDataModel(
            code=200,
            msg="查询执行器的缓存",
            user=request.user.get('username'),
            is_notice=ClientTypeEnum.ACTUATOR.value,
            data=QueueModel(
                func_name=ToolsEnum.get_cache_key_value.value,
                func_args=request.query_params.get('key')
            )
        )
        ChatConsumer.active_send(socket_data)
        return ResponseData.success(RESPONSE_MSG_0062)
