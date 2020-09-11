from appium.webdriver.common.mobileby import MobileBy


class LocalLoc:
    # 问题反馈
    search_context_loc = (MobileBy.ID, 'com.lzui.setting:id/tv_second_item_name')
    # 开始记录问题按钮
    record_button = (MobileBy.ID,'com.lzui.setting:id/btn_about')
    # 确认上传日志按钮
    upload_log_button = (MobileBy.ID,'com.lzui.setting:id/upload_upload')
    # 问题日志上传成功提示
    upload_success_tip = (MobileBy.ID,'com.lzui.setting:id/finish_tip')



