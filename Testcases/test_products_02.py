# import logging
import sys
import unittest
# import time

from Utils.utility import Utility

sys.path.append(".")

from Objects.checkout_step_one import CheckoutStepOne
from Objects.account import Account

from Locators.check_out_step_two_page_locators import CheckoutTwoPageLocator
from Pages.checkout_step_one_page import CheckoutStepOnePage
from Pages.checkout_step_two_page import CheckoutStepTwoPage
from Pages.login_page import LoginPage
from Pages.products_page import ProductsPage
from Pages.cart_page import CartPage
from Testcases.base_test import BaseTest
from Testdata.data import Data

from Utils.assertion import Assertion


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
        checkoutstepone = CheckoutStepOne('fname', 'lname', 'zipcode')
        checkout_step_one_page.add_checkout_info(checkoutstepone)
        checkout_step_one_page.click_continue()

        checkout_step_two_page = CheckoutStepTwoPage(self.driver)
        # compare selected products in cart page and checkout two page
        total_price = 0.00
        for index in [1, 2, 3]:
            actual_product = checkout_step_two_page.get_product_info(index)
            expected_product = products[index - 1]
            assertion.compare_products(actual_product, expected_product)
            print(actual_product.quantity)
            total_price += Utility().multiple(actual_product.quantity, actual_product.price)

        payment_info = checkout_step_two_page.get_payment_info()
        shipping_info = checkout_step_two_page.get_shipping_info()
        self.assertEqual('SauceCard #31337', payment_info)
        self.assertEqual('FREE PONY EXPRESS DELIVERY!', shipping_info)

        # print(checkout_step_two_page.get_item_total())
        # print(checkout_step_two_page.get_tax())
        # print(checkout_step_two_page.get_total())

        print(total_price)
        self.assertEqual(total_price, checkout_step_two_page.get_item_total())

        actual_tax = total_price * 0.08004
        self.assertEqual(float("{:.2f}".format(actual_tax)), checkout_step_two_page.get_tax())
        print(float("{:.2f}".format(actual_tax)))

        actual_total = total_price + actual_tax
        self.assertEqual(float("{:.2f}".format(actual_total)), checkout_step_two_page.get_total())
        print(float("{:.2f}".format(actual_total)))


if __name__ == "__main__":
    unittest.main()
