import logging

from Pages.base_page import BasePage
from Locators.products_page_locator import ProductsPageLocators


class ProductsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

    def get_product_url(self):
        return self.current_url()

    def count_broken_images(self):
        return self.get_elements_size(ProductsPageLocators.IMAGE_BROKEN)

    def get_badge_total(self):
        index = 0
        try:
            text = self.get_text(ProductsPageLocators.ICON_BADGE_HAS_ITEMS)
            index = int(text)
        except:
            return 0
        return index

    def click_badge_icon(self):
        self.click(ProductsPageLocators.ICON_BADGE_NO_ITEM)

    def click_remove_button(self, index):
        self.click(ProductsPageLocators.BUTTON_REMOVE(index))

    def click_add_to_cart_button(self, index):
        self.click(ProductsPageLocators.BUTTON_ADD_TO_CART(index))
