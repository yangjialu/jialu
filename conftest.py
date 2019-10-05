import time
import pytest
from selenium import webdriver
from pages.login import LoginPage


@pytest.fixture(scope="session")
def init_web():
    driver = webdriver.Remote(command_executor='http://192.168.3.48:4444/wd/hub', desired_capabilities={'browserName': 'chrome'})
    login_page = LoginPage(driver)
    driver.maximize_window()
    yield driver, login_page
    time.sleep(2)
    driver.quit()