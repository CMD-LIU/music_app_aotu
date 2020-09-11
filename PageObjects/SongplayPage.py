import logging
from Common.basepage import BasePage
from PageLocators.LocalLoc import SongplayPageLoc as loc


class SongplayPage(BasePage):

    # 获取搜索内容
    def search_song_context(self):
        return self.get_element_text(loc.search_context_loc, "搜索的内容")

    # 获取音乐列表的标题
    def search_song_list(self):
        return self.get_element_text(loc.search_list_loc,"搜索的标题")

    # 点击收藏按钮
    def click_collect_button(self):
        self.click_element(loc.song_collect_loc,"点击收藏按钮")

    # 点击快进按钮
    def click_forward_button(self):
        self.click_element(loc.song_forward_loc,"点击快进按钮")

    # 点击快进按钮
    def click_backward_button(self):
        self.click_element(loc.song_backward_loc, "点击快退按钮")

    # 获取歌曲播放的音乐时间class属性
    def search_song_MusicTime(self):
         return self.get_element_attribute(loc.song_MusicTime_loc,"className", "音乐播放时间")




