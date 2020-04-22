from appium.webdriver.common.mobileby import MobileBy


class SongplayPageLoc:
    # 搜索内容
    search_context_loc = (MobileBy.ID, 'com.lz.smart.music:id/item_song_btn')
    # 音乐列表的标题
    search_list_loc = (MobileBy.ID, 'com.lz.smart.music:id/playing_list')
    #音乐列表的标题为欧美流行元素
    search_list_loc2 = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("欧美流行")')
    #收藏按钮
    song_collect_loc = (MobileBy.ID,'com.lz.smart.music:id/music_collect_btn')
    #快进按钮
    song_forward_loc = (MobileBy.ID,'com.lz.smart.music:id/music_forward_btn')
    #快退按钮
    song_backward_loc = (MobileBy.ID, 'com.lz.smart.music:id/music_backward_btn')
    #音乐时间
    song_MusicTime_loc = (MobileBy.ID, 'com.lz.smart.music:id/music_time')


