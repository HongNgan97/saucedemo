import logging
import sys

from Objects.checkout_step_one import CheckoutStepOne
from Pages.checkout_step_one_page import CheckoutStepOnePage
from Utils import assertion
from Utils.assertion import Assertion

sys.path.append(".")

import unittest
import time

from Pages.login_page import LoginPage
from Pages.products_page import ProductsPage
from Pages.cart_page import CartPage
from Testcases.base_test import BaseTest
from Testdata.data import Data
from Objects.account import Account


class TestProduct02(BaseTest):
    @classmethod
    def setUp(self):
        super().setUp()

    @classmethod
    def tearDown(self):
        super().tearDown()

    def test_product(self):
        products = Data.getProducts_json(self)
        assertion = Assertion()

        login_page = LoginPage(self.driver)
        account = Account('standard_user', Data.PASSWORD)
        login_page.login(account)

        products_page = ProductsPage(self.driver)

        # for index, expected_product in enumerate(products, start=1):
        #     products_page.click_add_to_cart_button(index)
        for index in [1, 2, 3]:
            products_page.click_add_to_cart_button(index)

        products_page.click_badge_icon()
        cart_page = CartPage(self.driver)
        for index in [1, 2, 3]:
            actual_product = cart_page.get_product_info(index)
            expected_product = products[index - 1]
            assertion.compare_products(actual_product, expected_product)
        # logging.info("Verify products from the cart page are the same with the selected products")
        # for index in [1, 2, 3]:
        #     assertion.compare_products(cart_page.get_product_info(index), products[index - 1])

        cart_page.click_checkout_button()

        checkout_step_one_page = CheckoutStepOnePage(self.driver)
        checkoutStepOne = CheckoutStepOne('fname', 'lname', 'zipcode')
        checkout_step_one_page.add_checkout_info(checkoutStepOne)
        checkout_step_one_page.click_continue()


if __name__ == "__main__":
    unittest.main()
