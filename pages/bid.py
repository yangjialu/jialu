from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from pages.base import BasePage


class BidPage(BasePage):
    """投资页面"""
    #  投资输入框元素
    bid_input = (By.CSS_SELECTOR, ".form-control")
    # 按钮元素定位
    bid_submit = (By.CSS_SELECTOR, ".btn")
    # 点击激活元素
    alert_locator = (By.XPATH, "//*[@class='layui-layer-content']//button[text()='查看并激活']")

    def get_bid_input(self):
        # 定位投资输入框
        return self.wait_presence_element(self.bid_input)

    def click_bid_submit(self):
        # 点击投标按钮，确保该按钮可以点击
        return self.wait_clickable_element(self.bid_submit).click()

    def click_alert(self):
        # 点击查看并激活按钮
        return self.wait_clickable_element(self.alert_locator).click()