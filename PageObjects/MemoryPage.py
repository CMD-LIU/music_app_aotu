import logging
from Common.basepage import BasePage
from PageLocators.MemoryLoc import MemoryLoc as loc


class MemoryPage(BasePage):

    # 获取用户存储空间的已用空间
    def UserStorage(self):
        self.get_element_text(self,loc.UserStorage_loc,"获取已用空间")

    # 点击清空按钮
    def click_clean_button(self):
        self.click_element(self,loc.Clean_Button_loc,"点击清空按钮")

    # 点击提示框的确定按钮
    def click_Cleantips_Button(self):
        self.click_element(self,loc.Cleantips_Button__loc,"点击提示框的确定按钮")




