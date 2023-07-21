

from poco.drivers.unity3d import UnityPoco
from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from airtest.cli.parser import cli_setup
from airtest.utils.logger import get_logger
import os
import logging
import time
from launch import APP


class BasePage:
    poco = UnityPoco(use_airtest_input=True, screenshot_each_action=False)  # 获取poco驱动对象
    #启动APP
    def start(self):
        APP.start_app('')
    #退出APP
    def quit_app(self):
        APP.stop_app('')

    def install_app(self):
        self.install_app('')

    def uninstall_app(self):
        self.uninstall_app('')


    #获取设备的宽高
    def get_myWindow_size(self):
        width,heigth=self.poco.get_screen_size()
        return width,heigth

    def mobile_page_up_or_down_swip(self,start_x=0.5,start_y=0.6,end_y=0.9):
        """
        页面上下滑动
        :param start_x:
        :param start_y:
        :param end_y:
        :return:
        """
        size=self.get_myWindow_size()
        print("size[0]={0},size[1]={1}".format(size[0],size[1]))
        logging.info("size[0]={0},size[1]={1}".format(size[0],size[1]))
        x1=size[0]*start_x #size[0]取元祖的第一个值，*0.5表示中间的点
        y1=size[1]*start_y #size[1]取元祖的第二个值，*0.5表示距离底部的点
        y2=size[1]*end_y
        time.sleep(2)
        swipe((x1*start_x,y1*start_y),vector=(x1*start_x,y2*end_y))


    def mobile_page_left_or_right_swip(self,start_x=0.5,start_y=3/4,end_x=1/6):
        """
        页面左右滑动
        :param start_x:
        :param start_y:
        :param end_x:
        :return:
        """
        size=self.get_myWindow_size()
        print("size[0]={0},size[1]={1}".format(size[0],size[1]))
        x1=int(size[0]*start_x) #size[0]取元祖的第一个值，*0.5表示中间的点
        y1=int(size[1]*start_y) #size[1]取元祖的第二个值，*0.5表示距离底部近
        x2=int(size[0]*end_x)
        time.sleep(2)
        swipe((x1*start_x,y1*start_y),(x2*end_x,y1*start_y))



    def find_element(self,element):
        """
        查找元素
        :param element:
        :return:
        """
        try:
            if element is None:
                return None
            else:
                return self.poco(element)
        except:
            logging.error("找不到元素")

    def find_element_text(self,texts):
        """
        查找元素
        :param text:
        :return:
        """
        return self.poco(text=texts)

    def find_element_Parent(self,element):
        """
        查找父元素
        :param element:
        :return:
        """
        return self.poco(element).parent()

    def find_element_Child(self,element,childelement):
        """
        查找子元素
        :param element:
        :return:
        """
        return self.poco(element).offspring(childelement)

    def find_element_Child_Parent(self,element,childelement):
        """
        查找子元素的父元素
        :param element:
        :return:
        """
        return self.poco(element).offspring(childelement).parent()

    def find_element_AllChild(self,element):
        """
        查找所有子元素
        :param element:
        :return:
        """
        return self.poco(element).child()

    def touch_img(self,imgFile,time=1):
        """
        点击图片
        :param imgFile:
        :param time:
        :return:
        """
        #self.touch(Template(os.path.abspath(os.path.dirname(__file__))+"/images/{}").format(imgFile))
        self.touch(Template(os.path.abspath(os.path.dirname(__file__))+"/images/{}").format(imgFile),time=time)


    def click_element(self,element):
        """
        点击元素
        :param element:
        :return:
        """
        self.find_element(element).click()


    def wait_for_element(self,element,times=15):
        """
        等待元素出现
        :param element:
        :param time:
        :return:
        """
        self.find_element(element).wait(time=times,timeout=True)

    def click_element_Long(self,element):
        """
        长按元素
        :param element:
        :return:
        """
        self.find_element(element).long_click()


    def click_element_Wait(self,element,time=5):
        """
        等待元素5S出现后点击
        :param element:
        :time:
        :return:
        """
        self.find_element(element).wait(time).click()

    def text_inupt(self,element,texts):
        """
        设置文本
        :param element:
        :param text:
        :return:
        """
        self.find_element(element).set_text(texts)

    def get_image(self,element):
        """
        获取图片
        :param element:
        :return:
        """
        return self.find_element(element).get_image()

    
    def get_element_text(self,element):
        """
        获取元素文本
        :param element:
        :return:
        """
        return self.find_element(element).get_text()


    def get_element_size(self,element):
        """
        获取元素大小
        :param element:
        :return:
        """
        return self.find_element(element).get_size()


    def is_element_exist(self,element):
        """
        通过element检测元素是否存在
        :param element:
        :return:
        """
        if element=="name":
            return self.poco(name=element).exists()
        elif element=="text":
            return self.poco(text=element).exists()

        else:
            pass


if __name__=="__main__":
    pass





