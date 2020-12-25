import logging

from Locators.check_out_step_two_page_locators import CheckoutTwoPageLocator
from Objects.product import Product
from Pages.base_page import BasePage


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
