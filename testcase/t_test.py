import allure
import pytest

from base.BasePage import BasePage
from page.login_page import LoginPage
from airtest.core.api import *
class Login_game(BasePage):
    @pytest.fixture(autouse=True, scope='session')
    @allure.feature("登录游戏")
    @allure.story("登录游戏验证头像")
    def test_login(self):
        App = LoginPage.gamestart('')
        LoginPage.out_local()
        assert_equal(LoginPage.get_locators()['LogoScene'],"logo")