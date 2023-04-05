import sys

from uiautomator2 import UiObjectNotFoundError
from uiautomator2.xpath import XPath
from wda import WDAElementNotFoundError

from auto_ui.app_auto_base import ElementNotFoundError, ElementNotDisappearError
from auto_ui.app_auto_base.android_base import AndroidBase
from utlis.logs.log_control import ERROR, INFO


class View(AndroidBase):
    """视图类操作"""

    def click(self, element):
        """单击"""
        try:
            self.find_element(element).click_exists(timeout=3)
            INFO.logger.info("成功单击")
        except Exception as e:
            ERROR.logger.error("无法单击")
            raise e

    def double_click(self, system, element):
        """双击"""
        try:
            if system == "android":
                self.app.double_click(*self.find_element(element).center())
            else:
                self.app.double_tap(*self.find_element(element).center())
            INFO.logger.info("成功双击")
        except Exception as e:
            ERROR.logger.error("无法双击")
            raise e

    def long_click(self, system, element, second):
        """长按"""
        try:
            if system == "android":
                self.find_element(element).long_click(second)
            else:
                self.find_element(element).tap_hold(second)
            INFO.logger.info("成功长按%sS" % str(second))
        except Exception as e:
            ERROR.logger.error("无法长按%sS" % str(second))
            raise e

    def click_coord(self, x, y):
        """坐标单击 百分比或坐标值"""
        try:
            self.app.click(x, y)
            INFO.logger.info("成功坐标单击")
        except Exception as e:
            ERROR.logger.error("无法坐标单击")
            raise e

    def double_click_coord(self, system, x, y):
        """坐标双击 百分比或坐标值"""
        try:
            if system == "android":
                self.app.double_click(x, y)
            else:
                self.app.double_tap(x, y)
            INFO.logger.info("成功坐标双击")
        except Exception as e:
            ERROR.logger.error("无法坐标双击")
            raise e

    def long_click_coord(self, system, x, y, second):
        """坐标长按 百分比或坐标值"""
        try:
            if system == "android":
                self.app.tap_hold(x, y, second)
            else:
                self.app.long_click(x, y, second)
            INFO.logger.info("成功坐标长按%sS" % str(second))
        except Exception as e:
            ERROR.logger.error("无法坐标长按%sS" % str(second))
            raise e

    def swipe(self, system, fx, fy, tx, ty, duration=None):
        """坐标滑动 百分比或坐标值"""
        try:
            if system == "android":
                if duration == "":
                    duration = None
                self.app.swipe(fx, fy, tx, ty, duration)
            else:
                if duration == "" or duration is None:
                    duration = 0
                self.app.swipe(fx, fy, tx, ty, duration)
            INFO.logger.info("成功执行滑动")
        except Exception as e:
            ERROR.logger.error("无法执行滑动")
            raise e

    def input_text(self, element, text):
        """输入"""
        try:
            self.find_element(element).set_text(text)
            INFO.logger.info("成功输入%s" % str(text))
        except Exception as e:
            ERROR.logger.error("无法输入%s" % str(text))
            raise e

    def clear_text(self, system, element):
        """清空"""
        try:
            ele = self.find_element(element)
            if system == "android" and len(element) == 1 and "xpath" in element:
                xe = ele.get()
                ele._d.set_fastinput_ime()
                xe.click()
                ele._parent._d.set_fastinput_ime()
                ele._parent._d.clear_text()
            else:
                ele.clear_text()
            INFO.logger.info("成功清空")
        except Exception as e:
            ERROR.logger.error("无法清空")
            raise e

    def scroll_to_ele(self, system, element, direction):
        """滑动到元素出现"""
        try:
            if system == "android":
                if "xpath" in element:
                    XPath(self.app).scroll_to(element["xpath"], direction)
                elif direction == "up":
                    self.app(scrollable=True).forward.to(**element)
                elif direction == "down":
                    self.app(scrollable=True).backward.to(**element)
                elif direction == "left":
                    self.app(scrollable=True).horiz.forward.to(**element)
                else:
                    self.app(scrollable=True).horiz.backward.to(**element)
            else:
                self.find_element(element).scroll(direction)
            INFO.logger.info("成功滑动到元素出现")
        except Exception as e:
            ERROR.logger.error("无法滑动到元素出现")
            raise e

    def pinch_in(self, system, element):
        """缩小 安卓仅支持属性定位"""
        try:
            if system == "android":
                self.find_element(element).pinch_in()
            else:
                self.find_element(element).pinch(0.5, -1)
            INFO.logger.info("成功缩小")
        except Exception as e:
            ERROR.logger.error("无法缩小")
            raise e

    def pinch_out(self, system, element):
        """放大 安卓仅支持属性定位"""
        try:
            if system == "android":
                self.find_element(element).pinch_out()
            else:
                self.find_element(element).pinch(2, 1)
            INFO.logger.info("成功放大")
        except Exception as e:
            ERROR.logger.error("无法放大")
            raise e

    def wait(self, element, second):
        """等待元素出现"""
        try:
            if self.find_element(element).wait(timeout=second):
                INFO.logger.info("成功等待元素出现")
            else:
                ERROR.logger.error("等待元素出现失败 元素不存在")
                raise ElementNotFoundError("element not exists")
        except ElementNotFoundError as e:
            raise e
        except Exception as e:
            ERROR.logger.error("无法等待元素出现")
            raise e

    def wait_gone(self, system, element, second):
        """等待元素消失"""
        try:
            if system == "android":
                res = self.find_element(element).wait_gone(timeout=second)
            else:
                res = self.find_element(element).wait_gone(timeout=second, raise_error=False)
            if res:
                INFO.logger.info("成功等待元素消失")
            else:
                ERROR.logger.error("等待元素消失失败 元素仍存在")
                raise ElementNotDisappearError("element exists")
        except ElementNotDisappearError as e:
            raise e
        except Exception as e:
            ERROR.logger.error("无法等待元素消失")
            raise e

    def drag_to_ele(self, start_element, end_element):
        """拖动到元素 安卓专属 只支持属性定位"""
        try:
            self.find_element(start_element).drag_to(**end_element)
            INFO.logger.info("成功拖动到元素")
        except Exception as e:
            ERROR.logger.error("无法拖动到元素")
            raise e

    def drag_to_coord(self, element, x, y):
        """拖动到坐标 安卓专属 只支持属性定位"""
        try:
            self.find_element(element).drag_to(x, y)
            INFO.logger.info("成功拖动到坐标")
        except Exception as e:
            ERROR.logger.error("无法拖动到坐标")
            raise e

    def drag_coord(self, fx, fy, tx, ty):
        """坐标拖动 安卓专属"""
        try:
            self.app.drag(fx, fy, tx, ty)
            INFO.logger.info("成功坐标拖动")
        except Exception as e:
            ERROR.logger.error("无法坐标拖动")
            raise e

    def swipe_ele(self, element, direction):
        """元素内滑动 安卓专属"""
        try:
            self.find_element(element).swipe(direction)
            INFO.logger.info("成功元素内滑动")
        except Exception as e:
            ERROR.logger.error("无法元素内滑动")
            raise e

    def alert_wait(self, second):
        """等待弹框出现 IOS专属"""
        try:
            self.app.alert.wait(second)
            INFO.logger.info("成功等待弹框出现")
        except Exception as e:
            ERROR.logger.error("无法等待弹框出现")
            raise e

    def alert_accept(self):
        """弹框确认 IOS专属"""
        try:
            self.app.alert.accept()
            INFO.logger.info("成功弹框确认")
        except Exception as e:
            ERROR.logger.error("无法弹框确认")
            raise e

    def alert_dismiss(self):
        """弹框取消 IOS专属"""
        try:
            self.app.alert.dismiss()
            INFO.logger.info("成功弹框取消")
        except Exception as e:
            ERROR.logger.error("无法弹框取消")
            raise e

    def alert_click(self, name):
        """弹框点击 IOS专属"""
        try:
            self.app.alert.click(name)
            INFO.logger.info("成功弹框点击%s" % name)
        except Exception as e:
            ERROR.logger.error("无法弹框点击%s" % name)
            raise e

    def custom(self, **kwargs):
        """自定义"""
        code = kwargs["code"]
        names = locals()
        names["element"] = kwargs["element"]
        names["data"] = kwargs["data"]
        names["device"] = self.app
        names["test"] = self.test
        try:
            def _print(*args, sep=' ', end='\n', file=None, flush=False):
                if file is None or file in (sys.stdout, sys.stderr):
                    file = names["test"].stdout_buffer
                print(*args, sep=sep, end=end, file=file, flush=flush)

            def sys_get(name):
                if name in names["test"].context:
                    return names["test"].context[name]
                elif name in names["test"].common_params:
                    return names["test"].common_params[name]
                else:
                    raise KeyError("不存在的公共参数或关联变量: {}".format(name))

            def sys_put(name, val, ps=False):
                if ps:
                    names["test"].common_params[name] = val
                else:
                    names["test"].context[name] = val

            exec(code)
            INFO.logger.info("成功执行 %s" % kwargs["trans"])
        except UiObjectNotFoundError as e:
            raise e
        except WDAElementNotFoundError as e:
            raise e
        except Exception as e:
            ERROR.logger.error("无法执行 %s" % kwargs["trans"])
            raise e
