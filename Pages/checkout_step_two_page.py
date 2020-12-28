import logging

from Locators.check_out_step_two_page_locators import CheckoutTwoPageLocator
from Objects.product import Product
from Pages.base_page import BasePage
from Utils.utility import Utility


class CheckoutStepTwoPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

    def click_finish(self):
        self.click(CheckoutTwoPageLocator.BUTTON_FINISH)

    def click_cancel(self):
        self.click(CheckoutTwoPageLocator.BUTTON_CANCEL)

    def get_product_info(self, index):
        name = self.get_text(CheckoutTwoPageLocator.LABEL_PRODUCT_NAME(index))
        desc = self.get_text(CheckoutTwoPageLocator.LABEL_PRODUCT_DESC(index))
        price = self.get_text(CheckoutTwoPageLocator.LABEL_PRODUCT_PRICE(index))
        quantity = self.get_text(CheckoutTwoPageLocator.LABEL_PRODUCT_QUANTITY(index))
        return Product(name, desc, price, quantity)

    def get_payment_info(self):
        payment_info = self.get_text(CheckoutTwoPageLocator.LABEL_PAYMENT_INFO)
        return payment_info

    def get_shipping_info(self):
        shipping_info = self.get_text(CheckoutTwoPageLocator.LABEL_SHIPPING_INFO)
        return shipping_info

    def get_item_total(self, auto_convert=True):
        text = self.get_text(CheckoutTwoPageLocator.LABEL_ITEM_TOTAL)
        if auto_convert:
            return Utility().convert_string_to_float(text)
        else:
            return

    def get_tax(self, auto_convert=True):
        text = self.get_text(CheckoutTwoPageLocator.LABEL_TAX)
        if auto_convert:
            return Utility().convert_string_to_float(text)
        else:
            return

    def get_total(self, auto_convert=True):
        text = self.get_text(CheckoutTwoPageLocator.LABEL_TOTAL)
        if auto_convert:
            return Utility().convert_string_to_float(text)
        else:
            return
