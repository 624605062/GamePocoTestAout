import logging
import time
from poco.drivers.unity3d import UnityPoco
import pytest
import airtest.core.api
from page.mainpage import MainPage
from base.BasePage import BasePage
from launch import APP
from airtest.core.api import *
class LoginPage(BasePage):

    def get_locators(self):
        locators = {
            'LogoScene': self.find_element(element='logo'),
            'Startgame': self.find_element_text(texts="开始探险"),
            'Xbox' : self.find_element(element='m_tog_Read'),
            'SelectPhone' : self.find_element(element='m_btnLoginSelectPhone'),
            'Phonenumber' : self.find_element_text(texts="请输入手机号码"),
            'Code' : self.find_element_text(texts="请输入验证码"),
            'getCode' : self.find_element(element='m_txtLoginPhoneGetCode'),
            'LoginPhone' : self.find_element(element='m_btnLoginPhoneConfirm'),
            'CloseLoginPhone' : self.find_element(element='m_btnLoginPhoneClose'),
            'LoginWechat' : self.find_element(element='m_btnLoginSelectWechat'),
            'CloseLoginWechat' : self.find_element(element='m_btnLoginSelectClose'),
            'LoginTourist' : self.find_element(element='游客登录'),
            'IDname' : self.find_element(element='请填写真实姓名'),
            'IDcard' : self.find_element(element='请填写身份证号'),
            'IDclose' : self.find_element(element='m_btnCertifiedClose'),
            'IDLogin' : self.find_element(element='m_btnCertifiedConfirm'),
            'SetButton' : self.find_element(element='m_btnSet')
        }
        return locators

    def wait_for_logo(self):
        self.get_locators()['LogoScene'].wait(timeout=20)

    def pull_up_login_iphone(self):
        "拉起手机登录弹窗"
        "判断勾选按钮是否存在"
        try:
            if self.get_locators()['Xbox'].exists():
                pass
            else:
                self.get_locators()['Xbox'].click()
        except:
            logging.info('勾选按钮不存在')
        time.sleep(2)
        self.get_locators()['Startgame'].click()
        time.sleep(2)
        self.get_locators()['SelectPhone'].click()
        time.sleep(2)
        try:
            self.get_locators()['Phonenumber'].click()
            self.get_locators()['Phonenumber'].set_text('13479612723')
            time.sleep(2)
            self.get_locators()['getCode'].click()
        except:
            logging.info('手机号设置错误')
        self.get_locators()['Code'].click()
        self.get_locators()['Code'].set_text('123456')
        self.get_locators()['LoginPhone'].click()
    def pull_up_login_wechat(self):
        "拉起微信登录"
        self.get_locators()['Xbox'].click()
        time.sleep(2)
        self.get_locators()['Startgame'].click()
        time.sleep(2)
        self.get_locators()['LoginWechat'].click()
        time.sleep(10)

    def pull_up_login_tourist(self):
        "拉起游客登录"
        pass


    def set_parameters(self):
        "输入手机号和验证码"

    def login_game(self):
        "登录游戏"
        pass






