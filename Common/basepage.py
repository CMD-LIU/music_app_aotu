import logging
import datetime
import time
import win32gui
import win32con

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

from appium.webdriver.webdriver import WebDriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.multi_action import MultiAction

from Common import logger
from Common.handle_path import screenshot_dir


class BasePage:
    """
       # 包含了PageObjects当中，用到所有的selenium底层方法。
       # 还可以包含通用的一些元素操作，如alert,iframe,windows...
       # 实现日志记录、实现失败截图
    """

    def __init__(self, driver: WebDriver):
        self.driver = driver

    # 等待元素可见（可见一定存在）
    def wait_ele_visible(self, locator, img_doc, timeout=30, poll_fre=0.5):
        """
        :param locator: 元组类型(元素定位策略,元素定位表达式)
        :param img_doc: 截图文件的命名部分。${页面名称_行为名称}_当前的时间.png
        :param timeout: 超时，最大时间为30s
        :param poll_fre: 等待间隔，默认为0.5s
        :return: None
        """
        logging.info("{} : 等待<{}>元素可见".format(img_doc, locator))
        try:
            # 起始等待的时间 datetime
            start = datetime.datetime.now()
            WebDriverWait(self.driver, timeout, poll_fre).until(EC.visibility_of_element_located(locator))
        except:
            # 异常信息写入日志
            logging.exception("等待元素可见失败：")  # 级别：Error，tracebak的信息完整的写入日志。
            # 截图命名：页面名称_行为名称_当前的时间.png
            self.save_page_screenshot(img_doc)
            raise
        else:
            # 结束等待的时间
            end = datetime.datetime.now()
            logging.info("等待结束. 开始时间为:{},结束时间为:{},一共等待耗时为:{}".format(start, end, end - start))

    # 等待元素存在（存在不一定可见）
    def wait_page_contains_element(self, locator, img_doc, timeout=30, poll_fre=0.5):
        logging.info("{} : 等待<{}>元素存在".format(img_doc, locator))
        try:
            # 起始等待的时间 datetime
            start = datetime.datetime.now()
            WebDriverWait(self.driver, timeout, poll_fre).until(EC.presence_of_element_located(locator))
        except:
            # 异常信息写入日志
            logging.exception("等待元素存在失败：")  # 级别：Error，tracebak的信息完整的写入日志。
            # 截图命名：页面名称_行为名称_当前的时间.png
            self.save_page_screenshot(img_doc)
            raise
        else:
            # 结束等待的时间
            end = datetime.datetime.now()
            logging.info("等待结束. 开始时间为:{},结束时间为:{},一共等待耗时为:{}".format(start, end, end - start))

    # 检测元素是否在页面存在且可见
    def check_element_visible(self, locator, img_doc, timeout=30, poll_fre=0.5):
        """
         检测元素是否在页面存在且可见。
         如果退出元素存在，则返回True。否则返回False
        :return: 布尔值
        """
        logging.info("{}: 检测元素<{}>存在且可见于页面。".format(img_doc, locator))
        try:
            WebDriverWait(self.driver, timeout, poll_fre).until(EC.visibility_of_element_located(locator))
        except:
            logging.exception(" {}秒内元素在当前页面不可见。".format(timeout))
            self.save_page_screenshot(img_doc)
            return False
        else:
            logging.info(" {}秒内元素可见。".format(timeout))
            return True

    # 查找页面单个元素
    def get_element(self, locator, img_doc):
        logging.info("{} : 查找<{}>元素.".format(img_doc, locator))
        try:
            ele = self.driver.find_element(*locator)
        except:
            # 异常信息写入日志
            logging.exception("查找元素失败：")  # 级别：Error，tracebak的信息完整的写入日志。
            # 截图命名：页面名称_行为名称_当前的时间.png
            self.save_page_screenshot(img_doc)
            raise
        else:
            return ele

    # 查找页面中所有元素
    def get_elements(self, locator, img_doc):
        logging.info("{} : 查找<{}>元素.".format(img_doc, locator))
        try:
            ele = self.driver.find_elements(*locator)
        except:
            # 异常信息写入日志
            logging.exception("查找元素失败：")  # 级别：Error，tracebak的信息完整的写入日志。
            # 截图命名：页面名称_行为名称_当前的时间.png
            self.save_page_screenshot(img_doc)
            raise
        else:
            return ele

    # 文本框输入
    def input_text(self, locator, value, img_doc, timeout=30, poll_fre=0.5):
        # 1）等待元素可见；2）查找元素；3）输入动作
        self.wait_ele_visible(locator, img_doc, timeout, poll_fre)
        ele = self.get_element(locator, img_doc)
        logging.info("{}: 对<{}>元素输入文本 {}".format(img_doc, locator, value))
        try:
            ele.send_keys(value)
        except:
            # 异常信息写入日志
            logging.exception("输入文本失败：")  # 级别：Error，tracebak的信息完整的写入日志。
            # 截图命名：页面名称_行为名称_当前的时间.png
            self.save_page_screenshot(img_doc)
            raise

    # 清除文本框的内容
    def clear_text(self, locator, img_doc, timeout=20, poll_fre=0.5):
        self.wait_ele_visible(locator, img_doc, timeout, poll_fre)
        ele = self.get_element(locator, img_doc)
        logging.info("{}: 对<{}>元素内容清除文本".format(img_doc, locator))
        try:
            ele.clear()
        except:
            # 异常信息写入日志
            logging.exception("清除文本内容失败：")  # 级别：Error，tracebak的信息完整的写入日志。
            # 截图命名：页面名称_行为名称_当前的时间.png
            self.save_page_screenshot(img_doc)
            raise

    # 点击操作
    def click_element(self, locator, img_doc, timeout=30, poll_fre=0.5):
        # 1）等待元素可见；2）查找元素；3）点击
        self.wait_ele_visible(locator, img_doc, timeout, poll_fre)
        ele = self.get_element(locator, img_doc)
        logging.info("{}: 点击<{}>元素 ".format(img_doc, locator))
        try:
            ele.click()
        except:
            # 异常信息写入日志
            logging.exception("点击操作失败：")  # 级别：Error，tracebak的信息完整的写入日志。
            # 截图命名：页面名称_行为名称_当前的时间.png
            self.save_page_screenshot(img_doc)
            raise

    # 获取元素文本
    def get_element_text(self, locator, img_doc, timeout=30, poll_fre=0.5):
        # 1）等待元素存在；2）查找元素；3）获取元素文本
        self.wait_ele_visible(locator, img_doc, timeout, poll_fre)
        ele = self.get_element(locator, img_doc)
        logging.info("{}: 获取<{}>元素的文本内容.".format(img_doc, locator))
        try:
            text = ele.text
        except:
            # 异常信息写入日志
            logging.exception("获取元素文本值失败：")  # 级别：Error，tracebak的信息完整的写入日志。
            # 截图命名：页面名称_行为名称_当前的时间.png
            self.save_page_screenshot(img_doc)
            raise
        else:
            logging.info("获取的文本值为: {}".format(text))
            return text

    # 获取元素的属性值
    def get_element_attribute(self, locator, attr, img_doc, timeout=30, poll_fre=0.5):
        # 1）等待元素存在；2）查找元素；3）获取元素的属性值
        self.wait_page_contains_element(locator, img_doc, timeout, poll_fre)
        ele = self.get_element(locator, img_doc)
        logging.info("{}: 获取<{}>元素的属性 {}.".format(img_doc, locator, attr))
        try:
            value = ele.get_attribute(attr)
        except:
            # 异常信息写入日志
            logging.exception("获取元素属性失败：")  # 级别：Error，tracebak的信息完整的写入日志。
            # 截图命名：页面名称_行为名称_当前的时间.png
            self.save_page_screenshot(img_doc)
            raise
        else:
            logging.info("获取的属性值为: {}".format(value))
            return value

    # 获取所有的窗口列表
    def get_window_handles(self):
        logging.info("获取当前打开的所有窗口")
        try:
            wins = self.driver.window_handles
        except:
            # 异常信息写入日志
            logging.exception("获取当前打开的所有窗口失败：")  # 级别：Error，tracebak的信息完整的写入日志。
            raise
        else:
            logging.info("窗口列表为：{}".format(wins))
            return wins

    # 切换到最新窗口
    # 1）触发新窗口出现; 2）获取窗口列表；3）切换到最后一个
    def switch_to_new_window(self):
        time.sleep(3)
        wins = self.get_window_handles()
        logging.info("切换到最新的窗口：{}".format(wins[-1]))
        try:
            win = self.driver.switch_to.window(wins[-1])
        except:
            # 异常信息写入日志
            logging.exception("切换最新窗口失败：")  # 级别：Error，tracebak的信息完整的写入日志。
            raise
        else:
            logging.info("最新窗口为：{}".format(win))
            return win

    @staticmethod
    def upload(filePath, browser_type="chrome"):
        """非input标签文件上传"""
        time.sleep(2)
        if browser_type == "chrome":
            title = "打开"
        else:
            title = ""

        # 找元素
        # 一级窗口"#32770","打开"
        dialog = win32gui.FindWindow("#32770", title)
        ComboBoxEx32 = win32gui.FindWindowEx(dialog, 0, "ComboBoxEx32", None)  # 二级
        comboBox = win32gui.FindWindowEx(ComboBoxEx32, 0, "ComboBox", None)  # 三级
        # 编辑按钮
        edit = win32gui.FindWindowEx(comboBox, 0, 'Edit', None)  # 四级
        # 打开按钮
        button = win32gui.FindWindowEx(dialog, 0, 'Button', "打开(&O)")  # 二级

        # 往编辑当中，输入文件路径 。
        win32gui.SendMessage(edit, win32con.WM_SETTEXT, None, filePath)  # 发送文件路径
        win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)  # 点击打开按钮
        time.sleep(2)

    def save_page_screenshot(self, img_doc):
        """
        :param img_doc:
        :return:
        """
        # 路径配置文件中引入图片保存路径  + 年月日-时分秒
        # 截图命名：页面名称_行为名称_当前的时间.png
        # 页面_功能_时间.png
        now = time.strftime("%Y-%m-%d %H_%M_%S")
        screenshot_path = screenshot_dir + "/{}_{}.png".format(img_doc, now)
        try:
            self.driver.save_screenshot(screenshot_path)
        except:
            logging.exception("当前网页截图失败")
        else:
            logging.info("截取当前网页成功并存储在: {}".format(screenshot_path))

    def switch_to_frame(self, loc, img_doc, timeout=20, poll_fre=0.5):
        '''
        切换iframe页面
        :param loc: 元素定位的XPATH元组表达式
        :param img_doc: 截图说明
        :param timeout: 等待的超时时间
        :param poll_fre: 轮询频率
        :return:
        '''
        try:
            logging.info("在{}中根据元素<{}>进行iframe切换".format(img_doc, loc))
            start_time = time.time()
            WebDriverWait(self.driver, timeout, poll_fre).until(EC.frame_to_be_available_and_switch_to_it(loc))
        except Exception as e:
            logging.error("在{}中根据元素<{}>进行iframe切换失败！".format(img_doc, loc))
            self.save_page_screenshot(img_doc)
            raise e
        else:
            end_time = time.time()
            logging.info("在{}中根据元素<{}>进行iframe切换，等待时间：{}秒".
                         format(img_doc, loc, round(end_time - start_time, 2)))

    def switch_to_default_content(self, img_doc):
        '''
        切换iframe到main页面
        :param img_doc: 截图说明
        :return:
        '''
        try:
            logging.info("切换iframe到main页面")
            self.driver.switch_to.default_content()
        except Exception as e:
            logging.error("切换iframe到main页面失败！")
            self.save_page_screenshot(img_doc)
            raise e

    def switch_to_parent(self, img_doc):
        '''
        切换iframe到上一层页面
        :param img_doc: 截图说明
        :return:
        '''
        try:
            logging.info("切换iframe到上一层页面")
            self.driver.switch_to.parent_frame()
        except Exception as e:
            logging.error("切换iframe到上一层页面失败！")
            self.save_page_screenshot(img_doc)
            raise e

    def suspend_mouse(self, loc, img_doc, timeout=20, frequency=0.5):
        '''
        鼠标悬浮
        :param loc: 元素定位的XPATH元组表达式
        :param img_doc: 截图说明
        :param timeout: 等待的超时时间
        :param frequency: 轮询频率
        :return:
        '''
        try:
            logging.info("在{}上根据元素<{}>进行悬浮".format(img_doc, loc))
            self.wait_page_contains_element(loc, img_doc, timeout, frequency)
            ele = self.get_element(loc, img_doc)
            ActionChains(self.driver).move_to_element(ele).perform()
        except Exception as e:
            logging.error("在{}上根据元素<{}>进行悬浮失败！".format(img_doc, loc))
            self.save_page_screenshot(img_doc)
            raise e

    def alert_close(self, img_doc, alert_type='alert', text=None, timeout=20, frequency=0.5):
        '''
        弹框关闭
        :param img_doc: 截图说明
        :param alert_type: 弹框类型：alert/confirm/prompt
        :param text: prompt弹框输入的文本
        :param timeout: 等待的超时时间
        :param frequency: 轮询频率
        :return:
        '''
        try:
            logging.info("在{}中切换并关闭{}类型的弹框".format(img_doc, alert_type))
            start_time = time.time()
            WebDriverWait(self.driver, timeout, frequency).until(EC.alert_is_present())
            if alert_type in ['alert', 'confirm']:
                self.driver.switch_to.alert.accept()
            elif alert_type == 'prompt':
                self.driver.switch_to.alert.send_keys(text)
                self.driver.switch_to.alert.accept()
            else:
                logging.error("不支持{},请确认alert的类型".format(alert_type))
        except Exception as e:
            logging.error("在{}中切换并关闭{}类型的弹框失败！".format(img_doc, alert_type))
            self.save_page_screenshot(img_doc)
            raise e
        else:
            end_time = time.time()
            logging.info("在{}中切换并关闭{}类型的弹框，等待时间：{}秒".
                         format(img_doc, alert_type, round(end_time - start_time, 2)))

    def select_action(self, loc, img_doc, content, select_type, timeout=20, frequency=0.5):
        '''
        Select操作
        :param loc: 元素定位的XPATH元组表达式
        :param img_doc: 截图说明
        :param content: select_by_方法的入参
        :param select_type: select类型
        :param timeout: 等待的超时时间
        :param frequency: 轮询频率
        :return:
        '''
        try:
            logging.info("在{}上根据元素<{}>以{}方式进行下拉选择".format(img_doc, loc, select_type))
            self.wait_page_contains_element(loc, img_doc, timeout, frequency)
            ele = self.get_element(loc, img_doc)
            if select_type == 'index':
                Select(ele).select_by_index(content)
            elif select_type == 'value':
                Select(ele).select_by_value(content)
            elif select_type == 'text':
                Select(ele).select_by_visible_text(content)
            else:
                logging.error("不支持{},请确认Select的类型".format(select_type))
        except Exception as e:
            logging.error("在{}上根据元素<{}>以{}方式进行下拉选择失败！".format(img_doc, loc, select_type))
            self.save_page_screenshot(img_doc)
            raise e

    """===========================app封装==========================================="""

    def sliding_screen(self, direction, img_doc):
        '''
        滑屏操作
        :param direction: 滑屏方向：上-up；下-down；左-left；右-right
        :param img_doc: 截图说明
        :return:
        '''
        size = self.driver.get_window_size()
        try:
            logging.info("开始向{}方向滑动".format(direction))
            if direction.lower() == 'up':
                self.driver.swipe(start_x=size['width'] * 0.5,
                                  start_y=size['height'] * 0.9,
                                  end_x=size['width'] * 0.5,
                                  end_y=size['height'] * 0.1,
                                  duration=200)
            elif direction.lower() == 'down':
                self.driver.swipe(start_x=size['width'] * 0.5,
                                  start_y=size['height'] * 0.1,
                                  end_x=size['width'] * 0.5,
                                  end_y=size['height'] * 0.9,
                                  duration=200)
            elif direction.lower() == 'left':
                self.driver.swipe(start_x=size['width'] * 0.9,
                                  start_y=size['height'] * 0.5,
                                  end_x=size['width'] * 0.1,
                                  end_y=size['height'] * 0.5,
                                  duration=200)
            elif direction.lower() == 'right':
                self.driver.swipe(start_x=size['width'] * 0.1,
                                  start_y=size['height'] * 0.5,
                                  end_x=size['width'] * 0.9,
                                  end_y=size['height'] * 0.5,
                                  duration=200)
            else:
                logging.error("方向选择错误！")
        except Exception as e:
            logging.error("向{}方向滑动屏幕失败！".format(direction))
            self.save_page_screenshot(img_doc)
            raise e

    def get_toast_msg(self, partial_text, img_doc):
        '''
        获取toast文本信息
        :param partial_text: 不完整文本
        :param img_doc: 截图说明
        :return: toast文本
        '''
        loc = (MobileBy.XPATH, '//*[contains(@text,"{}")]'.format(partial_text))
        try:
            WebDriverWait(self.driver, 10, 0.01).until(EC.presence_of_element_located(loc))
            msg = self.driver.find_element(*loc).text
            print("toast出现了！！！")
            return msg
        except Exception as e:
            print("好可惜，toast没找到！！")
            logging.error("获取toast文本失败！")
            self.save_page_screenshot(img_doc)
            raise e

    def switch_to_webview(self, loc, img_doc, timeout=20, frequency=0.5):
        '''
        切换到webview页面
        :param loc: webview页面的元素
        :param img_doc: 截图说明
        :param timeout: 等待的超时时间
        :param frequency: 轮询频率
        :return:
        '''
        try:
            logging.info("等待元素{}可见，并进行webview切换".format(loc))
            start_time = time.time()
            WebDriverWait(self.driver, timeout, frequency).until(EC.visibility_of_element_located(loc))
            cons = self.driver.contexts
            logging.info("开始切换到webview：{}".format(cons[-1]))
            self.driver.switch_to.context(cons[-1])
        except Exception as e:
            logging.error("切换webview失败！")
            self.save_page_screenshot(img_doc)
            raise e
        else:
            end_time = time.time()
            logging.info("切换到webview：{}成功，等待时间：{}秒".format(cons[-1], round(end_time - start_time, 2)))

    def switch_to_native_app(self, img_doc):
        '''
        切换到app原生页面
        :param img_doc: 截图说明
        :return:
        '''
        try:
            logging.info("切换到app原生页面")
            self.driver.switch_to.context('NATIVE_APP')
        except Exception as e:
            logging.error("切换到app原生页面失败！")
            self.save_page_screenshot(img_doc)
            raise e

    def application_switching(self, package_name, activity_name, img_doc):
        '''
        应用切换
        :param package_name: 包名
        :param activity_name: 欢迎页面名
        :param img_doc: 截图说明
        :return:
        '''
        try:
            logging.info("切换应用到{}".format(package_name))
            self.driver.start_activity(app_package=package_name, app_activity=activity_name)
        except Exception as e:
            logging.error("切换应用到{}失败！".format(package_name))
            self.save_page_screenshot(img_doc)
            raise e

    def target_click(self, x1, y1, img_doc):
        """
        模拟单手点击操作
        :param x1: 为使用设备的实际X轴坐标
        :param y1: 为使用设备的实际Y轴坐标
        :return:
        """
        x = self.driver.get_window_size()['width']  # 获取设备的屏幕宽度
        y = self.driver.get_window_size()['height']  # 获取设备屏幕的高度
        x_1 = x1 / x  # 计算坐标在横坐标上的比例，720为设备的宽
        y_1 = y1 / y  # 计算坐标在纵坐标上的比例，1280为设备的高

        print(x_1 * x, y_1 * y)  # 打印出点击的坐标点
        try:
            logging.info("单手点击")
            self.driver.tap([(x_1 * x, y_1 * y)], 200)  # 模拟单手点击操作
        except Exception as e:
            logging.error("单手点击失败")
            self.save_page_screenshot(img_doc)
            raise e

    def list_swipe(self, locator, timeout=30, poll_fre=0.5):
        """
        列表向上滑动
        :param locator: 定位元素
        :param timeout: 超时时间
        :param poll_fre: 间隔频率
        :return:
        """
        # 获取设备的大小
        size = self.driver.get_window_size()
        # 向上滑动
        old_page = None
        new_page = self.driver.page_source
        while old_page != new_page:
            try:
                logging.info("开始滑动")
                WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(locator))
                break
            except:
                self.driver.swipe(size["width"] * 0.5, size["height"] * 0.9, size["width"] * 0.5,
                                  size["height"] * 0.1, 200)
                old_page = new_page
                new_page = self.driver.page_source

    def screen_zoom(self, scale, img_doc):
        """
        屏幕放大、缩小
        :param scale: 为pinch时：缩小，两个手指向内滑动。为zoom时：放大，两个手指向外滑动
        :param img_doc:
        :return:
        """
        # 获取设备大小
        size = self.driver.get_window_size()
        # 定义中心点
        center_point = (size['width'] * 0.5, size['height'] * 0.5)
        # 定义两个外点
        out_point_01 = (size['width'] * 0.2, size['height'] * 0.2)
        out_point_02 = (size['width'] * 0.8, size['height'] * 0.8)
        # 点击一下屏幕
        TouchAction(self.driver).tap(x=size['width'] * 0.5, y=size['height'] * 0.5).wait(200).perform()
        # pinch：缩小，两个手指向内滑动
        a1 = TouchAction(self.driver).press(x=out_point_01[0], y=out_point_01[1]).wait(200) \
            .move_to(x=center_point[0], y=center_point[1]).wait(200)
        a2 = TouchAction(self.driver).press(x=out_point_02[0], y=out_point_02[1]).wait(200) \
            .move_to(x=center_point[0], y=center_point[1]).wait(200)
        # zoom：放大，两个手指向外滑动
        b1 = TouchAction(self.driver).press(x=center_point[0], y=center_point[1]).wait(200) \
            .move_to(x=out_point_01[0], y=out_point_01[1]).wait(200)
        b2 = TouchAction(self.driver).press(x=center_point[0], y=center_point[1]).wait(200) \
            .move_to(x=out_point_02[0], y=out_point_02[1]).wait(200)
        try:
            logging.info("进行{}操作".format(scale))
            if scale.lower() == 'pinch':
                m = MultiAction(self.driver)
                m.add(a1, a2)
                m.perform()
            elif scale.lower() == 'zoom':
                m = MultiAction(self.driver)
                m.add(b1, b2)
                m.perform()
        except Exception as e:
            logging.error("进行{}操作失败！".format(scale))
            self.save_page_screenshot(img_doc)
            raise e



if __name__ == '__main__':
    pass
