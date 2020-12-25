import logging

from Locators.checkout_step_one_page_locators import CheckoutOnePageLocator
from Pages.base_page import BasePage


class CheckoutStepOnePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

    def add_checkout_info(self, checkoutstepone):
        self.enter_text(CheckoutOnePageLocator.INPUT_FIRSTNAME, checkoutstepone.firstname)
        self.enter_text(CheckoutOnePageLocator.INPUT_LASTNAME, checkoutstepone.lastname)
        self.enter_text(CheckoutOnePageLocator.INPUT_POSTALCODE, checkoutstepone.postalcode)

    def click_continue(self):
        self.click(CheckoutOnePageLocator.BUTTON_CONTINUE)

    def click_cancel(self):
        self.click(CheckoutOnePageLocator.BUTTON_CANCEL)
