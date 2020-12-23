import sys

from Utils.assertion import Assertion

sys.path.append(".")

import unittest
import time

from Pages.login_page import LoginPage
from Pages.products_page import ProductsPage
from Testcases.base_test import BaseTest
from Testdata.data import Data
from Objects.account import Account


class TestProduct(BaseTest):
    @classmethod
    def setUp(self):
        super().setUp()

    @classmethod
    def tearDown(self):
        super().tearDown()

    def test_product(self):
        products = Data.getProducts_json(self)
        # for index, expected_product in enumerate(products, start=1):
        #     print(expected_product)

        login_page = LoginPage(self.driver)
        account = Account('standard_user', Data.PASSWORD)
        login_page.login(account)

        products_page = ProductsPage(self.driver)

        for index, expected_product in enumerate(products, start=1):
            actual_product = products_page.get_product_info(index)
            assertion = Assertion()
            assertion.compare_products(actual_product, expected_product)

        # total = products_page.get_badge_total()
        # print(total)
        # products_page.click_badge_icon()
        # products_page.click_add_to_cart_button(1)
        # products_page.click_remove_button(1)
        # time.sleep(5)
        # products_page.get_all_products_info()

        for index, expected_product in enumerate(products, start=1):
            '"Add & remove all products"'
            products_page.click_add_to_cart_button(index)
            self.assertTrue(products_page.does_remove_button_exist(index))
            self.assertEqual(1, products_page.get_product_badge())

            products_page.click_remove_button(index)
            self.assertTrue(products_page.does_add_button_exist(index))
            self.assertTrue(products_page.is_product_badge_invisible())


if __name__ == "__main__":
    unittest.main()
