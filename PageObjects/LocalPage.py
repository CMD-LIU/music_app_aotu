import time
from Common.basepage import BasePage
from PageLocators.LocalLoc import LocalLoc as loc



class LocalPage(BasePage):

    # 点击开始记录问题按钮
    def click_record_button(self):
       self.click_element(self,loc.record_button,"点击开始记录问题按钮" )

    # 等待5s后按遥控器菜单键,调出上传问题日志界面
    def recall_recordtips(self):
        time.sleep(5)
        self.driver.keyevent(82);

   # 点击上传日志按钮
    def click_upload_button(self):
        self.click_element(self,loc.upload_log_button,"点击上传日志按钮")

    # 获取问题日志上传成功提示
    def get_upload_success_tip(self):
        self.get_element_text(self,loc.upload_success_tip,"获取上传成功提示")
