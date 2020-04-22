import pytest
import yaml
import os
import logging
from appium import webdriver
from Common import logger
from Common.handle_path import caps_dir


# 订制服务器启动参数
def _base_driver(server_port=4723, **kwargs):
    # 读取公共的默认配置
    fs = open(os.path.join(caps_dir, "desired_caps.yaml"))
    desired_caps = yaml.full_load(fs)

    # 看一下是否有定制化的配置项
    if kwargs:
        for key, value in kwargs.items():
            desired_caps[key] = value

    # 启动一个server会话
    driver = webdriver.Remote('http://127.0.0.1:{}/wd/hub'.format(server_port), desired_caps)
    driver.get_window_size()
    return driver


@pytest.fixture(scope="class")
def init_app():
    driver = _base_driver(unicodeKeyboard=True, resetKeyboard=True)
    yield driver
    driver.close_app()

