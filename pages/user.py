from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from pages.base import BasePage


class UserPage(BasePage):
    """用户页面"""
    user_money_locator = (By.CSS_SELECTOR, ".color_sub")

    def get_user_money(self):
        ele = self.wait_presence_element(self.user_money_locator)
        money = ele.text[:-1]
        return money