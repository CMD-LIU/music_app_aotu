import pytest
import time
import logging

from PageObjects.NetworkSetingPage import NetworkSetingPage

@pytest.mark.usefixtures("init_app")
class Test_Hotspot:

    def Test_01_Hotspot(self,init_app):
        logging.info("******* 正常流程：*******")
        #获取