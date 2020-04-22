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
class Test_Search:

    def test_01_Search(self, init_app):
        logging.info("******* 正常流程：搜索歌曲 *******")
        # 搜索刘德华的忘情水
        HomePage(init_app).click_search_singer_song("刘德华的忘情水")
        # 断言：搜索的歌曲存在
        song_context = SongplayPage(init_app).search_song_context()
        assert difflib.SequenceMatcher(None, song_context, "刘德华的忘情水").quick_ratio()
        similarity_ratio = difflib.SequenceMatcher(None, song_context, "刘德华的忘情水").quick_ratio()
        logging.info("相似率为：{}".format(similarity_ratio))

    def test_02_Search(self, init_app):
        logging.info("******* 正常流程：搜索歌手 *******")
        HomePage(init_app).change_firstpage()
        #
        HomePage(init_app).click_search_singer_song("周杰伦")
        # 断言：搜索的歌曲存在
        song_context = SongplayPage(init_app).search_song_list()
        assert "周杰伦" == song_context

