from selenium.webdriver.common.by import By


class ProductsPageLocators(object):
    """A class for min page locators. All main page locators should come here"""
    IMAGE_BROKEN = (By.XPATH, "//img[@class='inventory_item_img' and contains(@src, 'WithGarbageOnItToBreakTheUrl')]")

    # def find_items(self, index):
        # NAME_ITEM = (By.XPATH, "//div[@class='inventory_item_name']")


