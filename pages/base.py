import sys
import traceback
import unittest
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from pages.Logger import MyLog

logger = MyLog()


class BasePage(object):
    def __init__(self, driver: Chrome):
        self.driver = driver

    def wait_presence_element(self, locator, timeout=10):
        try:
            user_name = WebDriverWait(self.driver, timeout).until(
                ec.presence_of_element_located(locator))
            return user_name
        except Exception as e:
            logger.error("wait_presence_element元素定位失败")
            self.driver.save_screenshot('presence_error.png')

    def wait_clickable_element(self, locator, timeout=10):
        try:
            user_name = WebDriverWait(self.driver, timeout).until(
                ec.element_to_be_clickable(locator))
            return user_name
        except Exception as e:
            logger.error("wait_clickable_element元素定位失败")
            self.driver.save_screenshot("clickable_error.png")


if __name__ == '__main__':
    driver = Chrome()
    driver.get('http://www.baidu.com')
    user = BasePage(driver).wait_presence_element((By.ID, 'w'))
