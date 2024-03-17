# -*- coding: utf-8 -*-
# @Project: auto_test
# @Description: 
# @Time   : 2024-02-28 17:32
# @Author : 毛鹏
import json

from PyAutoTest.auto_test.auto_system.models import CacheData
from PyAutoTest.enums.system_enum import CacheValueTypeEnum


class CacheDataValue:

    @classmethod
    def get_cache_value(cls, key: str):
        cache_data_obj = CacheData.objects.get(key=key)
        if cache_data_obj.value_type == CacheValueTypeEnum.STR.value or cache_data_obj.value_type is None:
            return cache_data_obj.value
        elif cache_data_obj.value_type == CacheValueTypeEnum.INT.value:
            return int(cache_data_obj.value)
        elif cache_data_obj.value_type == CacheValueTypeEnum.BOOL.value:
            return True if cache_data_obj.value else False
        elif cache_data_obj.value_type == CacheValueTypeEnum.DICT.value:
            return json.loads(cache_data_obj.value)
