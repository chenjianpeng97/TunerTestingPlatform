# -*- coding: utf-8 -*-
# @Project: auto_test
# @Description: 
# @Time   : 2023-09-28 16:18
# @Author : 毛鹏
import json

from PySide6.QtCore import (QThread, Signal)
from blinker import signal

from enums.socket_api_enum import ToolsSocketEnum
from enums.system_enum import CacheDataKey2Enum
from enums.tools_enum import CacheKeyEnum, CacheValueTypeEnum
from service.socket_client.client_socket import ClientWebSocket
from tools.assertion import Assertion
from tools.data_processor.sql_cache import SqlCache
from tools.other_utils.get_class_methods import GetClassMethod
from .ui_window import Ui_MainWindow
import service

custom_signal = signal('notice_signal')


class MyThread(QThread):
    my_signal = Signal()


class Window(Ui_MainWindow):
    signal = Signal(object)  # 定义信号

    def setup(self):
        self.setupUi(self)
        self.sendRedisData.clicked.connect(self.clickSendRedisData)
        self.test.clicked.connect(self.clickTest)
        self.signal.connect(self.signalLabel6)

        self.radioButton.clicked.connect(self.signalTextEdit1)
        BROWSER_IS_MAXIMIZE = SqlCache.get_sql_cache(CacheKeyEnum.BROWSER_IS_MAXIMIZE.value)
        if BROWSER_IS_MAXIMIZE:
            self.radioButton.setChecked(BROWSER_IS_MAXIMIZE)
        self.comboBox.currentTextChanged.connect(self.on_combobox_changed)
        TEST_CASE_PARALLELISM = SqlCache.get_sql_cache(CacheKeyEnum.TEST_CASE_PARALLELISM.value)
        if TEST_CASE_PARALLELISM:
            self.comboBox.setCurrentText(TEST_CASE_PARALLELISM)
        custom_signal.connect(self.setTextEdit)
        self.label_3.setText(service.USERNAME)

    def clickSendRedisData(self):
        """
        设置web页面的操作元素
        @return:
        """
        r = GetClassMethod()
        send_list: list = r.main()
        send_list.append({CacheDataKey2Enum.ASSERTION_METHOD.value: json.dumps(Assertion.get_methods(), ensure_ascii=False)})
        cls = ClientWebSocket()
        cls.sync_send('设置缓存数据', func_name=ToolsSocketEnum.SET_OPERATION_OPTIONS.value, func_args=send_list)

    def clickTest(self):
        self.signal.emit("hello, is happy!")

    # 接受信号的槽函数
    def signalLabel6(self, text):
        self.label_6.setText(text)

    def signalTextEdit(self, text):
        self.textEdit.setText(text)

    def signalTextEdit1(self, text):
        SqlCache.set_sql_cache(CacheKeyEnum.BROWSER_IS_MAXIMIZE.value, '1' if text else '0',
                               CacheValueTypeEnum.INT.value)
        if text:
            self.textEdit.append(f'开启浏览器最大化成功')
        else:
            self.textEdit.append(f'关闭浏览器最大化成功')

    def on_combobox_changed(self, text):
        SqlCache.set_sql_cache(CacheKeyEnum.TEST_CASE_PARALLELISM.value, text)
        self.textEdit.append(f'设置用例并行数为{text}成功')

    def setTextEdit(self, sender, data: str):
        if sender == 1:
            self.label_6.setText(data)
        else:
            self.textEdit.append(data)