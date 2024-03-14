# -*- coding: utf-8 -*-
# @Project: MangoActuator
# @Description: 
# @Time   : 2023-07-07 10:14
# @Author : 毛鹏
from exceptions import MangoActuatorError


class UiError(MangoActuatorError):
    pass


class BrowserPathError(UiError):
    pass


class BrowserObjectClosed(UiError):
    pass


class UiTimeoutError(UiError):
    pass


class ElementTypeError(UiError):
    pass


class UiAssertionError(UiError):
    pass


class UiSqlAssertionError(UiError):
    pass


class LocatorError(UiError):
    pass


class ElementIsEmptyError(UiError):
    pass


class ElementLocatorError(UiError):
    pass


class UiAttributeError(UiError):
    pass


class UploadElementInputError(UiError):
    pass


class UiCacheDataIsNullError(UiError):
    pass


class ReplaceElementLocatorError(UiError):
    pass