"""
测试登录功能
"""
import time
import unittest
import pytest
import allure
from ddt import ddt, data
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from pages.index import IndexPage
from pages.login import LoginPage
from test_data.login_data import user_error, user_error_shouquan, user_success


@allure.feature("测试登录功能")
class TestLogin(object):

    @pytest.mark.success
    @allure.story("登录失败用例")
    @pytest.mark.parametrize("data", user_error)
    def test_login_error1(self, data, init_web):
        with allure.step("获取返回的登录页面"):
            self.driver, self.login_page = init_web

        with allure.step("输入错误的用户名与密码，点击登录"):
            self.login_page.login(data['user'], data['pwd'])

        with allure.step("获取登录失败后错误的提示"):
            error = self.login_page.get_error_info()

        with allure.step("断言"):
            assert(data['expected'] == error.text)

    @pytest.mark.success
    @allure.story("登录失败用例")
    @pytest.mark.parametrize("data", user_error_shouquan)
    def test_login_error2(self, data, init_web):
        with allure.step("获取返回的登录页面"):
            self.driver, self.login_page = init_web

        with allure.step("输入错误的用户名与密码，点击登录"):
            self.login_page.login(data['user'], data['pwd'])

        with allure.step("获取登录失败后错误的提示"):
            error = self.login_page.get_flash_error()

        with allure.step("断言"):
            assert(data['expected'] == error.text)

    @allure.story("登录成功用例")
    @pytest.mark.parametrize("data", user_success)
    def test_login_success(self, data, init_web):
        with allure.step("获取返回的登录页面"):
            self.driver, self.login_page = init_web

        with allure.step("输入正确的用户名与密码，点击登录"):
            self.login_page.login(data['user'], data['pwd'])

        with allure.step("获取登录成功页面的用户信息"):
            user_name = IndexPage(self.driver).get_user_info()

        with allure.step("断言"):
            assert (data['expected'] == user_name.text)


if __name__ == '__main__':
     pytest.main()