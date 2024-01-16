# -*- coding: utf-8 -*-
# @Project: auto_test
# @Description: 
# @Time   : 2023-12-01 12:45
# @Author : 毛鹏
import logging
import os

from django.http import FileResponse
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.viewsets import ViewSet

from PyAutoTest.auto_test.auto_user.service.files_crud import FilesCRUD
from PyAutoTest.tools.view_utils.response_data import ResponseData

logger = logging.getLogger('user')


class ProjectFileViews(ViewSet):

    @action(methods=['get'], detail=False)
    def test(self, request: Request):
        FilesCRUD().initialization()
        return ResponseData.success('获取所有项目测试文件成功', FilesCRUD().get_project_all_list())

    @action(methods=['get'], detail=False)
    def get_project_all_list(self, request: Request):
        return ResponseData.success('获取所有项目测试文件成功', FilesCRUD().get_project_all_list())

    @action(methods=['post'], detail=False)
    def upload_files(self, request: Request):
        file_obj = request.FILES['file']
        project_id = request.headers.get('Project')
        if project_id:
            FilesCRUD(project_id).upload_files(file_obj)
            return ResponseData.success('上传文件成功', )
        return ResponseData.fail('请先选择所属项目再上传', )

    @action(methods=['get'], detail=False)
    def download_file(self, request: Request):
        project_id = request.query_params.get('project_id')
        file_name = request.query_params.get('file_name')
        file_obj = FilesCRUD(project_id)
        file_path = os.path.join(file_obj.project_upload_folder, file_name)
        if os.path.exists(file_path):
            response = FileResponse(open(file_path, 'rb'))
            response['Content-Disposition'] = f'attachment; filename="{file_name}"'
            return response
        else:
            return ResponseData.fail('文件不存在')

    @action(methods=['get'], detail=False)
    def delete_file(self, request: Request):
        project_id = request.query_params.get('project_id')
        file_name = request.query_params.get('file_name')
        FilesCRUD(project_id).delete_file(file_name)
        return ResponseData.success('文件删除成功')