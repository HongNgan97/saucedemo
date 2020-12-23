import logging

from Objects.product import Product
from Pages.base_page import BasePage
from Locators.cart_page_locators import CartLocators
from Testdata.data import Data


class CartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

    def get_product_url(self):
        return self.current_url()

    def click_remove_button(self, index):
        self.click(CartLocators.BUTTON_REMOVE(index))

    def get_product_info(self, index):
        name = self.get_text(CartLocators.LABEL_PRODUCT_NAME(index))
        desc = self.get_text(CartLocators.LABEL_PRODUCT_DESC(index))
        price = self.get_text(CartLocators.LABEL_PRODUCT_PRICE(index))
        quantity = self.get_text(CartLocators.LABEL_PRODUCT_QUANTITY(index))
        return Product(name, desc, price, quantity)

    def click_checkout_button(self):
        self.click(CartLocators.BUTTON_CHECKOUT)

    def click_continue_shopping_button(self):
        self.click(CartLocators.BUTTON_CONTINUE)
