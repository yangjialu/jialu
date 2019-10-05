import time
import pytest
from selenium.webdriver import Chrome
from pages.login import LoginPage


@pytest.fixture(scope="session")
def init_web():
    driver = Chrome()
    login_page = LoginPage(driver)
    driver.maximize_window()
    yield driver, login_page
    time.sleep(2)
    driver.quit()