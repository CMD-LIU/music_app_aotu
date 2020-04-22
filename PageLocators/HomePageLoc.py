from appium.webdriver.common.mobileby import MobileBy


class HomePageLoc:
    # 分类页签
    classify_type_loc = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("分类")')
    # 歌手页签
    singer_type_loc = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("歌手")')
    # 关于页签
    about_type_loc = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("关于")')
    # 搜索框
    search_box_loc = (MobileBy.ID, 'com.lz.smart.music:id/edt_searchinfo')
    # 搜索按钮
    search_button_loc = (MobileBy.ID, 'com.lz.smart.music:id/btn_start_search')
