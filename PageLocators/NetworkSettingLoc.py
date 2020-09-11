from appium.webdriver.common.mobileby import MobileBy


class NetworkSettingLoc:

    # 无线热点元素
    Wifi_type_loc = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("无线热点")')
    # 热点开关
    HotSpot_button_loc = (MobileBy.ID, 'com.lzui.setting:id/iv_ap_switch')
    # 热点名称元素
    HotSpotName_title_loc = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("热点名称")')
    # 热点密码元素
    HotSpotPassword_title_loc = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("热点密码")')
    # 热点名称输入框
    HotSpot_name_loc = (MobileBy.ID, 'com.lzui.setting:id/edt_ap_ssid')
    # 热点密码输入
    HotSpot_password_loc = (MobileBy.ID, 'com.lzui.setting:id/edt_ap_pwd')
    # 热点的确定按钮
    HotSpot_surebutton_loc = (MobileBy.ID, 'com.lzui.setting:id/btn_ap_change')