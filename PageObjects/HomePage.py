import logging
from Common.basepage import BasePage
from PageLocators.HomePageLoc import HomePageLoc as loc


class HomePage(BasePage):

    # 切换页签
    def click_main_type(self, main_type_name):
        """
        :param main_type_name: 页签名称，分别为：分类、歌手、关于
        :return: None
        """
        if main_type_name == "分类":
            self.click_element(loc.classify_type_loc, "点击分类页签")
        elif main_type_name == "歌手":
            self.click_element(loc.singer_type_loc, "点击歌手页签")
        elif main_type_name == "关于":
            self.click_element(loc.about_type_loc, "点击关于页签")
        else:
            logging.ERROR("没有该页签！")

    # 分类元素是否存在
    def check_classify_type_loc_exit(self):
        return self.check_element_visible(loc.classify_type_loc, "分类元素是否存在")

    # 搜索歌曲或歌手
    def click_search_singer_song(self, context):
        self.input_text(loc.search_box_loc, context, "搜索框输入")
        self.click_element(loc.search_button_loc, "点击搜索按钮")

    # 切换到app的首页
    def change_firstpage(self):
        self.application_switching('com.lz.smart.music','com.lz.smart.activity.MainActivity',"切换")

    # 重写basepage里点击操作的方法
    def target_click(self, x1, y1,x2,y2, img_doc):
        """
        模拟单手点击操作
        :param x3: 为使用设备的实际x轴坐标
        :param y3: 为使用设备的实际Y轴坐标
        :param x1,y1: 为使用设备的实际bounds第一个坐标
        :param x2,y2: 为使用设备的实际bounds第二个坐标
        :return:
        """
        #焦点中心坐标
        x3 = (x1 + x2)/2
        y3 = (y1 + y2)/2
        x = self.driver.get_window_size()['width']  # 获取设备的屏幕宽度
        y = self.driver.get_window_size()['height']  # 获取设备屏幕的高度
        x_1 = x3 / x  # 计算坐标在横坐标上的比例，720为设备的宽
        y_1 = y3 / y  # 计算坐标在纵坐标上的比例，1280为设备的高

        print(x_1 * x, y_1 * y)  # 打印出点击的坐标点
        try:
            logging.info("单手点击")
            self.driver.tap([(x_1 * x, y_1 * y)], 200)  # 模拟单手点击操作
        except Exception as e:
            logging.error("单手点击失败")
            self.save_page_screenshot(img_doc)
            raise e

    def Music_FangYe(self,direction,img_doc):
        '''
        滑屏操作
        :param direction: 滑屏方向：左-left；右-right
        :param img_doc: 截图说明
        :return:
        '''
        size = self.driver.get_window_size()
        try:
            logging.info("开始向{}方向滑动".format(direction))
            if direction.lower() == 'left':
                self.driver.swipe(start_x=size['width'] * 0.98,
                                  start_y=size['height'] * 0.5,
                                  end_x=size['width'] * 0.02,
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



