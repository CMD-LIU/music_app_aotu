import pytest
import time
import logging
import difflib
from PageObjects.HomePage import HomePage
from PageObjects.SongplayPage import SongplayPage


@pytest.mark.usefixtures("init_app")
class TestSongPage:

    def test_06_auto_Collect(self, init_app):
        logging.info("******* 收藏功能 *******")
        # 切换到分类页签
        HomePage(init_app).click_main_type("分类")
        # 进入欧美流行
        HomePage(init_app).target_click(981,239,1167,435, "选择歌曲类型为欧美音乐")
        song_context = SongplayPage(init_app).search_song_context()
        # 点击收藏按钮
        SongplayPage(init_app).click_collect_button()
        # 回到app首页
        HomePage(init_app).change_firstpage()
        HomePage(init_app).click_main_type("分类")
        # 选择我的收藏
        HomePage(init_app).target_click(135,239,321,435, "选择我的收藏")
        song_context2 = SongplayPage(init_app).search_song_context()
        # 断言：点击收藏的歌曲名称在我的收藏歌曲列表上能找到
        assert song_context2 == song_context

    def test_07_auto_Forward(self,init_app):
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

    # def test_08_auto_Backward(self,init_app):
    #     logging.info("******* 快退功能 *******")
    #     # 切换到分类页签
    #     HomePage(init_app).click_main_type("分类")
    #     # 进入欧美流行
    #     HomePage(init_app).target_click(981, 239, 1167, 435, "选择歌曲类型为欧美音乐")
    #     song_context = SongplayPage(init_app).search_song_context()
    #     # 点击收藏按钮
    #     SongplayPage(init_app).click_collect_button()
    #     # 回到app首页
    #     HomePage(init_app).change_firstpage()
    #     HomePage(init_app).click_main_type("分类")
    #     # 选择我的收藏
    #     HomePage(init_app).target_click(135, 239, 321, 435, "选择我的收藏")
    #     song_context2 = SongplayPage(init_app).search_song_context()
    #     # 断言：点击收藏的歌曲名称在我的收藏歌曲列表上能找到
    #     assert song_context2 == song_context
    #
    # def test_08_auto_Stop(self,init_app):
    #     logging.info("******* 暂停功能 *******")
    #     # 切换到分类页签
    #     HomePage(init_app).click_main_type("分类")
    #     # 进入欧美流行
    #     HomePage(init_app).target_click(981, 239, 1167, 435, "选择歌曲类型为欧美音乐")
    #     song_context = SongplayPage(init_app).search_song_context()
    #     # 点击收藏按钮
    #     SongplayPage(init_app).click_collect_button()
    #     # 回到app首页
    #     HomePage(init_app).change_firstpage()
    #     HomePage(init_app).click_main_type("分类")
    #     # 选择我的收藏
    #     HomePage(init_app).target_click(135, 239, 321, 435, "选择我的收藏")
    #     song_context2 = SongplayPage(init_app).search_song_context()
    #     # 断言：点击收藏的歌曲名称在我的收藏歌曲列表上能找到
    #     assert song_context2 == song_context
    #
    # def test_09_auto_broadcast(self,init_app):
    #     logging.info("******* 播放功能 *******")
    #     # 切换到分类页签
    #     HomePage(init_app).click_main_type("分类")
    #     # 进入欧美流行
    #     HomePage(init_app).target_click(981, 239, 1167, 435, "选择歌曲类型为欧美音乐")
    #     song_context = SongplayPage(init_app).search_song_context()
    #     # 点击收藏按钮
    #     SongplayPage(init_app).click_collect_button()
    #     # 回到app首页
    #     HomePage(init_app).change_firstpage()
    #     HomePage(init_app).click_main_type("分类")
    #     # 选择我的收藏
    #     HomePage(init_app).target_click(135, 239, 321, 435, "选择我的收藏")
    #     song_context2 = SongplayPage(init_app).search_song_context()
    #     # 断言：点击收藏的歌曲名称在我的收藏歌曲列表上能找到
    #     assert song_context2 == song_context

    def test_10_auto_checked(self,init_app):
        logging.info("******* 正常流程：搜索结果 *******")
        # 搜索刘德华的忘情水
        HomePage(init_app).click_search_singer_song("刘德华的忘情水")
        # 断言：搜索的歌曲存在
        song_context = SongplayPage(init_app).search_song_list()
        assert difflib.SequenceMatcher(None, song_context, "刘德华的忘情水").quick_ratio()
        similarity_ratio = difflib.SequenceMatcher(None, song_context, "刘德华的忘情水").quick_ratio()
        logging.info("相似率为：{}".format(similarity_ratio))
