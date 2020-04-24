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
*元素定位优先级：ID定位>class name定位>Accessibility ID定位>android uiautomator定位>XPath定位
*修改日期：
"""
@pytest.mark.usefixtures("init_app")
class Test_Collect:

    def test_01_Collect(self, init_app):
        logging.info("******* 收藏功能 *******")
        # 切换到分类页签
        HomePage(init_app).click_main_type("分类")
        # 进入欧美流行
        HomePage(init_app).target_click(981, 239, 1167, 435, "选择歌曲类型为欧美音乐")
        song_context = SongplayPage(init_app).search_song_context()
        # 点击收藏按钮
        SongplayPage(init_app).click_collect_button()
        # 回到app首页
        HomePage(init_app).change_firstpage()
        HomePage(init_app).click_main_type("分类")
        # 选择我的收藏
        HomePage(init_app).target_click(135, 239, 321, 435, "选择我的收藏")
        song_context2 = SongplayPage(init_app).search_song_context()
        # 断言：点击收藏的歌曲名称在我的收藏歌曲列表上能找到
        assert song_context2 == song_context