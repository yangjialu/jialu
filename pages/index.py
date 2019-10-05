from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from pages.base import BasePage


class IndexPage(BasePage):
    """首页界面"""
    bid_locator = (By.XPATH, "//*[text()=' 借款买船']")
    user_locator = (By.XPATH, "//*[@href='/Member/index.html']")

    def get_user_info(self):
        user = self.wait_presence_element(self.user_locator)
        return user

    def choose_bid(self):
        """该方法一定要确定该元素可以点击"""
        ele = self.wait_clickable_element(self.bid_locator)
        return ele.click()