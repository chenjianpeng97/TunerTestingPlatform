# -*- coding: utf-8 -*-
# @Project: auto_test
# @Description: 
# @Time   : 2023/3/23 11:28
# @Author : 毛鹏
import time

from DrissionPage import WebPage
from DrissionPage.configs.chromium_options import ChromiumOptions

from utlis.logs.nuw_logs import get_log_screenshot
from utlis.random_data import RandomData


class ChromeBase(WebPage):
    """实例化对象，以及对象方法重写"""

    def __init__(self, local_port, browser_path=None):
        if not browser_path:
            browser_path = './Chrome109/chrome.exe'
        do = ChromiumOptions(read_file=False).set_paths(
            local_port=local_port,
            browser_path=browser_path)
        # do.set_argument('--remote-allow-origins=*')cls=None,
        super().__init__(driver_or_options=do, session_or_options=False)

    def screenshot(self, ele_name: str):
        """
        重写截图方法
        @param ele_name: 元素名称
        @return:
        """
        self.get_screenshot(
            path=rf'{get_log_screenshot()}\{ele_name + RandomData.get_deta_hms()}.jpg',
            full_page=True)


if __name__ == '__main__':
    r = ChromeBase('9222')
    r.get('https://mall-admin-pre.zalldata.cn/#/mall/config/decorate/home/page/welfare')
    time.sleep(10)
