from selenium.webdriver.common.by import By


class LoginPageLocators(object):
    """A class for min page locators. All main page locators should come here"""
    INPUT_USERNAME = (By.ID, 'user-name')
    INPUT_PASSWORD = (By.ID, 'password')
    BUTTON_LOGIN = (By.XPATH, "//*[@id='login-button']")
    # BLOCK_OUT_USER_MSG = (By.CSS_SELECTOR, "#login_button_container > div > form > h3")
    LABEL_ERROR_MSG = (By.XPATH, "//h3[@data-test='error']")
