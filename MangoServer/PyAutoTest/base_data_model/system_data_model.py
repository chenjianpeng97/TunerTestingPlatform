# -*- coding: utf-8 -*-
# @Project: auto_test
# @Description: 
# @Time   : 2023-07-04 13:25
# @Author : 毛鹏
from typing import Union, Optional, TypeVar
from PyAutoTest.enums.system_enum import ClientTypeEnum

from pydantic import BaseModel

T = TypeVar('T')


class QueueModel(BaseModel):
    func_name: str
    func_args: Optional[Union[list[T], T]]


class SocketDataModel(BaseModel):
    code: int
    msg: str
    user: str = None
    is_notice: ClientTypeEnum | None = None
    data: QueueModel | None = None