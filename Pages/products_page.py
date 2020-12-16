import logging

from Objects.product import Product
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

    def get_product_info(self, index):
        name = self.get_text(ProductsPageLocators.LABEL_PRODUCT_NAME(index))
        desc = self.get_text(ProductsPageLocators.LABEL_PRODUCT_DESC(index))
        price = self.get_text(ProductsPageLocators.LABEL_PRODUCT_PRICE(index))

        product = Product(name, desc, price)
        print(product)
        # print(name)
        # print(desc)
        # print(price)
        return product

    def get_all_products_info(self):
        products = []
        for i in range(6):
            products.append(self.get_product_info(i + 1))

        return products
