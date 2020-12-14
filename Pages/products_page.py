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
