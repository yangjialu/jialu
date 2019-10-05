from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from pages.base import BasePage


class LoginPage(BasePage):
    """登录页面"""
    url = "http://120.78.128.25:8765/Index/login.html"

    user_locator = (By.NAME, "phone")
    pwd_locator = (By.NAME, "password")
    error_locator = (By.CSS_SELECTOR, ".form-error-info")
    auto_locator = (By.CSS_SELECTOR, ".layui-layer-content")

    def login(self, username, pwd):
        self.driver.get(self.url)
        self.driver.maximize_window()

        # 定位用户名、密码输入框
        user_name = self.get_user_info()
        passwd = self.get_pwd_info()

        user_name.send_keys(username)
        passwd.send_keys(pwd)
        user_name.submit()
        return self.driver

    def get_error_info(self):
        user = self.wait_presence_element(self.error_locator)
        return user

    def get_flash_error(self):
        info = self.wait_presence_element(self.auto_locator)
        return info

    def clear_user_info(self):
        """清空用户数据"""
        self.clear_user_info()
        self.clear_pwd()

    def clear_username(self):
        """清空用户"""
        return self.get_user_info().clear()

    def clear_pwd(self):
        """清空密码"""
        return self.get_pwd_info().clear()

    def get_user_info(self):
        """定位用户名输入框"""
        user_ele = self.wait_presence_element(self.user_locator)
        return user_ele

    def get_pwd_info(self):
        """定位密码输入框"""
        pwd_ele = self.wait_presence_element(self.pwd_locator)
        return pwd_ele