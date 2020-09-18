from appium.webdriver.common.mobileby import MobileBy


class MemoryLoc:
    # 存储空间元素
    MemorySpace_loc = (MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("存储空间")')
    # 用户存储空间的已用空间
    UserStorage_loc = (MobileBy.ID,'com.lzui.setting:id/tv_mem_used')
    #清空按钮
    Clean_Button_loc = (MobileBy.ID,'com.lzui.setting:id/btn_mem_clean')
    #清空提示框的确定按钮
    Cleantips_Button__loc = (MobileBy.ID,'com.lzui.setting:id/btn_dialog_left')


