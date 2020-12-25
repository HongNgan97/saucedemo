from selenium.webdriver.common.by import By


class CheckoutOnePageLocator(object):
    """A class for cart page locators. All cart page locators should come here"""
    BUTTON_CONTINUE = (By.XPATH, "//input[@class='btn_primary cart_button']")
    ICON_CART_BADGE = (By.ID, "shopping_cart_container")
    CART_ITEM = "//div[@class='cart_list']//div[@class='cart_item']["
    BUTTON_CANCEL = (By.XPATH, "//a[@class='cart_cancel_link btn_secondary']")

    INPUT_FIRSTNAME = (By.ID, 'first-name')
    INPUT_LASTNAME = (By.ID, 'last-name')
    INPUT_POSTALCODE = (By.ID, 'postal-code')
