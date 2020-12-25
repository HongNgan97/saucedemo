from selenium.webdriver.common.by import By


class CheckoutTwoPageLocator(object):
    BUTTON_FINISH = (By.XPATH, "//a[@class='btn_action cart_button'][text()='FINISH']")
    ICON_CART_BADGE = (By.XPATH, "//span[@class='fa-layers-counter shopping_cart_badge']")
    CART_ITEM = "//div[@class='cart_list']//div[@class='cart_item']["
    BUTTON_CANCEL = (By.XPATH, "//a[@class='cart_cancel_link btn_secondary'][text()='CANCEL']")

    LABEL_PAYMENT_INFO = (By.XPATH, "//div[@class='summary_value_label'][text()='SauceCard #31337']")
    LABEL_SHIPPING_INFO = (By.XPATH, "//div[@class='summary_value_label'][text()='FREE PONY EXPRESS DELIVERY!']")

    PART1 = "//div[@class='cart_item']["

    def LABEL_PRODUCT_NAME(index):
        part2 = "]//div[@class='inventory_item_name']"
        return By.XPATH, CheckoutTwoPageLocator.PART1 + str(index) + part2

    def LABEL_PRODUCT_DESC(index):
        part2 = "]//div[@class='inventory_item_desc']"
        return By.XPATH, CheckoutTwoPageLocator.PART1 + str(index) + part2

    def LABEL_PRODUCT_PRICE(index):
        part2 = "]//div[@class='inventory_item_price']"
        return By.XPATH, CheckoutTwoPageLocator.PART1 + str(index) + part2

    def LABEL_PRODUCT_QUANTITY(index):
        part2 = "]//div[@class='summary_quantity']"
        return By.XPATH, CheckoutTwoPageLocator.PART1 + str(index) + part2
