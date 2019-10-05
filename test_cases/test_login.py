# "18684720553"
import time
import allure
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from pages.index import IndexPage
from pages.login import LoginPage
from test_data.login_data import user_error_info, user_success_info, user_info


@allure.feature("测试登录功能")
@pytest.mark.error
# @pytest.mark.usefixtures("init_web")
class TestLogin(object):
    @allure.story("登录失败用例")
    @pytest.mark.parametrize("data", user_info)
    def test_login_error(self, data, init_web):
        with allure.step("获取返回的登录页面"):
            self.driver, self.login_page = init_web

        with allure.step("输入错误的用户名与密码，点击登录"):
            self.login_page.login(data["username"], data["pwd"])

        with allure.step("获取登录失败后的错误提示"):
            error_ele = self.login_page.get_error_auto()

        with allure.step("断言"):
            assert(data["expected"] == error_ele.text)

    @allure.story("登录失败用例")
    @pytest.mark.parametrize("data", user_error_info)
    def test_login_empty(self, data, init_web):
        with allure.step("获取返回的登录页面"):
            self.driver, self.login_page = init_web

        with allure.step("输入错误的用户名与密码，点击登录"):
            self.login_page.login(data["username"], data["pwd"])

        with allure.step("获取登录失败后的错误提示"):
            error_ele = self.login_page.get_error_info()

        with allure.step("断言"):
            assert(data["expected"] == error_ele.text)

    @allure.story("登录成功用例")
    @pytest.mark.parametrize("data", user_success_info)
    def test_login_success(self, data, init_web):
        with allure.step("获取返回的登录页面"):
            self.driver, self.login_page = init_web

        with allure.step("输入正确的用户名与密码，点击登录"):
            self.login_page.login(data["username"], data["pwd"])

        with allure.step("获取登录成功页面的用户信息"):
            user_name = IndexPage(self.driver).get_user_info()

        with allure.step("断言"):
            assert(data["expected"] == user_name.text)


if __name__ == '__main__':
    pytest.main()





#  pytest test_xueqiu.py --alluredir allure-report

#  allure serve allure-report