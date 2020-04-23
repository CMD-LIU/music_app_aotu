import pytest
import time
import logging
import difflib

from PageObjects.HomePage import HomePage
from PageObjects.SongplayPage import SongplayPage

"""
*用例设计人：刘权威
*脚本编写人：刘权威
*维护人：
*修改内容：无
*Apk版本描述：V2.512
*元素定位优先级：ID定位>name定位>class name定位>Accessibility ID定位>android uiautomator定位>XPath定位
*修改日期：
"""
@pytest.mark.usefixtures("init_app")
class Test_Collect:

    def test_02_auto_Forward(self,init_app):
        logging.info("******* 快进功能 *******")
        HomePage(init_app).click_main_type("分类")
        HomePage(init_app).target_click(981, 239, 1167, 435, "选择歌曲类型为欧美音乐")
        # 获取播放时间
        before_time = SongplayPage(init_app).search_song_MusicTime()
        # 点击快进按钮
        SongplayPage(init_app).click_forward_button()
        # 获取快进后的播放时间
        after_time = SongplayPage(init_app).search_song_MusicTime()
        # 断言：播放的时长增加了5秒
        print(before_time)
        assert  after_time == before_time