# -*- coding: utf-8 -*-
# @Project: MangoServer
# @Description:
# @Time   : 2023-06-04 12:24
# @Author : 毛鹏

from rest_framework import serializers
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.viewsets import ViewSet

from PyAutoTest.auto_test.auto_system.service.menu import ad_routes
from PyAutoTest.auto_test.auto_user.models import User
from PyAutoTest.auto_test.auto_user.views.role import RoleSerializers
from PyAutoTest.auto_test.auto_user.views.user_logs import UserLogsCRUD
from PyAutoTest.middleware.utlis.jwt_auth import create_token
from PyAutoTest.tools.data_processor.encryption_tool import EncryptionTool
from PyAutoTest.tools.view.model_crud import ModelCRUD
from PyAutoTest.tools.view.response_data import ResponseData
from PyAutoTest.tools.view.response_msg import *


class UserSerializers(serializers.ModelSerializer):
    create_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', read_only=True)
    update_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', read_only=True)
    last_login_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', read_only=True)

    class Meta:
        model = User
        exclude = ['password']


class UserSerializersC(serializers.ModelSerializer):
    create_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', read_only=True)
    update_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', read_only=True)
    last_login_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', read_only=True)
    role = RoleSerializers(read_only=True)

    class Meta:
        model = User
        exclude = ['password']

    @staticmethod
    def setup_eager_loading(queryset):
        queryset = queryset.select_related(
            'role')
        return queryset


class UserCRUD(ModelCRUD):
    model = User
    queryset = User.objects.all()
    serializer_class = UserSerializersC
    serializer = UserSerializers

    def post(self, request: Request):
        data = request.data
        serializer = self.serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            user = self.model.objects.get(id=serializer.data.get('id'))
            user.password = EncryptionTool.md5_32_small(**{'data': data['password']})
            user.save()
            return ResponseData.success(RESPONSE_MSG_0002, serializer.data)


class UserViews(ViewSet):
    model = User
    serializer = UserSerializers

    @action(methods=['get'], detail=False)
    def get_nickname(self, request: Request):
        """
        获取用户名称
        :param request:
        :return:
        """
        res = User.objects.values_list('id', 'nickname')
        data = [{'key': _id, 'title': name} for _id, name in res]
        return ResponseData.success(RESPONSE_MSG_0033, data)

    @action(methods=['put'], detail=False)
    def put_project(self, request: Request):
        serializer = self.serializer(instance=self.model.objects.get(
            id=request.data.get('id')),
            data={'selected_project': request.data.get('selected_project')})
        if serializer.is_valid():
            serializer.save()
            return ResponseData.success(RESPONSE_MSG_0034, serializer.data)

        else:
            return ResponseData.fail(RESPONSE_MSG_0035, serializer.errors)

    @action(methods=['put'], detail=False)
    def put_environment(self, request: Request):
        serializer = self.serializer(instance=self.model.objects.get(
            id=request.data.get('id')),
            data={'selected_environment': request.data.get('selected_environment')})
        if serializer.is_valid():
            serializer.save()
            return ResponseData.success(RESPONSE_MSG_0036, serializer.data)

        else:
            return ResponseData.fail(RESPONSE_MSG_0037, serializer.errors)

    @action(methods=['get'], detail=False)
    def get_user_project_environment(self, request: Request):
        obj = self.model.objects.get(id=request.query_params.get('id'))
        data = {'id': obj.id, 'selected_environment': obj.selected_environment,
                'selected_project': obj.selected_project}
        return ResponseData.success(RESPONSE_MSG_0041, data)

    @action(methods=['put'], detail=False)
    def put_password(self, request: Request):
        password = EncryptionTool.md5_32_small(**{'data': request.data['password']})
        new_password = EncryptionTool.md5_32_small(**{'data': request.data['new_password']})
        confirm_password = EncryptionTool.md5_32_small(**{'data': request.data['confirm_password']})

        obj = self.model.objects.get(id=request.data.get('id'))
        if password != obj.password:
            return ResponseData.fail(RESPONSE_MSG_0038)
        if new_password != confirm_password:
            return ResponseData.fail(RESPONSE_MSG_0039)
        obj.password = new_password
        obj.save()
        return ResponseData.success(RESPONSE_MSG_0040)


class LoginViews(ViewSet):
    authentication_classes = []
    access_token = None

    @action(methods=['post'], detail=False)
    def login(self, request: Request):
        username = request.data.get('username')
        password = request.data.get('password')
        source_type = request.data.get('type')
        password = EncryptionTool.md5_32_small(**{'data': password})
        user_info = User.objects.filter(username=username, password=password).first()
        if not user_info:
            return ResponseData.fail(RESPONSE_MSG_0042)
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        ip = x_forwarded_for.split(',')[0] if x_forwarded_for else request.META.get('REMOTE_ADDR')
        user_info.ip = ip
        user_info.save()
        UserLogsCRUD().inside_post({
            "nickname": user_info.nickname,
            "username": user_info.username,
            "ip": ip,
            "source_type": source_type,
            "user_id": user_info.id
        })
        return ResponseData.success(RESPONSE_MSG_0043, {
            "nickName": user_info.nickname,
            "userName": user_info.username,
            "userId": user_info.id,
            "roleId": user_info.role.id if user_info.role else None,
            "token": create_token({'id': user_info.id, 'username': user_info.username}),
            "selected_project": user_info.selected_project,
            "selected_environment": user_info.selected_environment,
            "roles": [
                {
                    "description": user_info.role.description if user_info.role else None,
                    "roleId": user_info.role.id if user_info.role else None,
                    "roleName": user_info.role.name if user_info.role else None
                }
            ]
        })

    @action(methods=['post'], detail=False)
    def register(self, request: Request):
        username = request.data.get('username')
        password = request.data.get('password')
        password = EncryptionTool.md5_32_small(**{'data': password})
        if User.objects.filter(username=username).exists():
            return ResponseData.fail(RESPONSE_MSG_0115)
        else:
            data = UserCRUD.inside_post({
                "nickname": request.data.get('nickname'),
                "username": username,
                "password": password,
            })
            user_obj = User.objects.get(id=data.get('id'))
            user_obj.password = password
            user_obj.save()
            return ResponseData.success(RESPONSE_MSG_0114, data)

    @action(methods=['get'], detail=False)
    def menu(self, request: Request):
        return ResponseData.success(RESPONSE_MSG_0044, ad_routes())
