from base.BasePage import BasePage
from airtest.utils.logger import get_logger
from airtest.core.api import *

class CloseToast(BasePage):
    def close_toast(self):
        try:
            for i in range(2):
                self.find_element('m_btnClose').click()
                sleep(1)
        except:
            get_logger().error('关闭toast失败')