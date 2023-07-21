

import allure
import pytest
from launch import APP
from base.BasePage import BasePage
from page.login_page import LoginPage
from airtest.core.api import *
class TestLogin(LoginPage):
    @allure.feature("登录游戏")
    @allure.story("登录游戏验证设置按钮")
    def test_login(self):
        LoginPage().pull_up_login_wechat()
        assset=self.get_locators()['SetButton'].exists()
        assert_equal(assset,"设置")
