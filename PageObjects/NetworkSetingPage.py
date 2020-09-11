import logging
from Common.basepage import BasePage
from PageLocators.NetworkSettingLoc import NetworkSettingLoc as loc
import requests

class NetworkSetingPage(BasePage):

    #判断是否有联网
    def isConnected(self):
        """
        请求百度
        :return: 布尔值：True有网/False没网
        """
        try:
            html = requests.get("http://www.baidu.com", timeout=2)
        except:
            return False
        return True

    #点击无线热点模块
    def click_hotspot_element(self):
        self.click_element(loc.Wifi_type_loc,"点击无线网络模块")

    #打开热点开关
    def open_wifi_button(self):
        self.click_element(loc.HotSpot_button_loc,"打开无线网络开关")

    # 判断热点名称和热点密码元素的存在
    def check_hotspot_loc_exit(self):
        """
        :return:ture:热点名称和热点密码元素都存在；false：有一个不存在
        """
        a = self.check_element_visible(loc.HotSpotName_title_loc,"判断热点名称元素的存在")
        b = self.check_element_visible(loc.HotSpotPassword_title_loc, "判断热点密码元素的存在")
        return a and b

    # 清空热点的名称和密码
    def clear_hotspot(self):
        self.clear_text(self,loc.HotSpot_name_loc,"清空热点名称")
        self.clear_text(self, loc.HotSpot_password_loc, "清空热点密码")


    # 输入热点的名称和密码
    def enter_hotspot(self,context1,context2):
        '''
        :return:返回输入的名称和密码
        '''
        self.input_text(loc.HotSpot_name_loc,context1,"输入热点名称")
        self.input_text(loc.HotSpot_password_loc, context2, "输入热点密码")
        return context1,context2

    # 点击热点的确定按钮
    def click_hotspot_surebutton(self):
        self.click_element(loc.HotSpot_surebutton_loc,"点击确定按钮")





