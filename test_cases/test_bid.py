import time
import allure
import pytest
from selenium.webdriver.common.by import By
from pages.bid import BidPage
from pages.index import IndexPage
from pages.login import LoginPage
import unittest
from selenium.webdriver import Chrome
from pages.user import UserPage
from test_data.bid_data import invest_money
from test_data.login_data import user_success


@allure.feature("测试投资用例")
class TestBid(object):

    @allure.story("测投资成功的用例")
    @pytest.mark.parametrize("data", user_success)
    def test_bid_success(self, data, init_web):
        """首页选择标，点击投标"""
        self.driver, self.login_page = init_web
        self.bid_page = BidPage(self.driver)
        self.login_page.login(data['user'], data['pwd'])
        IndexPage(self.driver).choose_bid()

        # 定位投资输入框元素
        ele = self.bid_page.get_bid_input()
        data = float(ele.get_attribute("data-amount"))
        # print(data)

        # 输入投资金额
        ele.send_keys(invest_money)

        # 点击投资
        self.bid_page.click_bid_submit()
        # 激活并查看
        self.bid_page.click_alert()

        actual_money_str = UserPage(self.driver).get_user_money()
        actual_money = float(actual_money_str)

        # 调试步骤
        print(int(data * 100))
        print(int(invest_money * 100))
        print(int(actual_money * 100))

        # 断言相关操作
        assert (int(data * 100) - invest_money * 100 == int(actual_money * 100))


if __name__ == '__main__':
    pytest.main(["-m", r"--alluredir=report\allure"])
