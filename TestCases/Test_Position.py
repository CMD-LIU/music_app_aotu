import pytest
import time
import logging
import difflib

from PageObjects.NetworkSetingPage import HomePage
from PageObjects.SongplayPage import SongplayPage

"""
*用例设计人：lqw
*脚本编写人：lqw
*维护人：
*修改内容：无
*Apk版本描述：V2.512
*元素定位优先级：ID定位>class name定位>Accessibility ID定位>android uiautomator定位>XPath定位
*修改日期：
"""
@pytest.mark.usefixtures("init_app")
class Test_Position:

    def test_01_Position(self, init_app):
        logging.info("******* 正常流程：选择歌曲类型：“欧美流行” *******")
        # 回到音乐app首页
        HomePage(init_app).change_firstpage()
        # BasePage(init_app).application_switching('com.lz.smart.music','com.lz.smart.activity.MainActivity',"切换")
        # 切换到分类页签
        HomePage(init_app).click_main_type("分类")
        # 进入到欧美流行
        HomePage(init_app).target_click(981, 239, 1167, 435, "选择歌曲类型为欧美音乐")
        # 断言：判断欧美流行元素是否存在
        song_context = SongplayPage(init_app).search_song_list()
        assert "欧美流行" == song_context

    def test_02_Table(self, init_app):
        logging.info("******* 正常流程：分类、歌手、关于页签切换 *******")
        HomePage(init_app).change_firstpage()
        # 切换到歌手页签
        HomePage(init_app).click_main_type("歌手")
        time.sleep(3)
        # 切换到关于页签
        HomePage(init_app).click_main_type("关于")
        time.sleep(3)
        # 切换到分类页签
        HomePage(init_app).click_main_type("分类")
        time.sleep(3)
        # 断言：最后是切换到分类页签
        assert HomePage(init_app).check_classify_type_loc_exit() is True

    # def test_03_slipping_sucess(self,init_app):
    #     logging.info("******* 正常流程：向右滑动，点击坑位“轻音乐”*******")
    #     HomePage(init_app).click_main_type("分类")
    #     HomePage(init_app).Music_FangYe("left","向左滑动")
    #     HomePage(init_app).target_click(823,239,1009,435, "选择歌曲类型为轻音乐")
    #     song_context = SongplayPage(init_app).search_song_list()
    #     assert "轻音乐" == song_context