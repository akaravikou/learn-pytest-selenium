from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config.config import TestData
from page.abstractPage import AbstractPage


class SignInPage(AbstractPage):
    EMAIL_FIELD = (By.XPATH, "//input[@type = 'email']")
    CONTINUE_BUTTON = (By.XPATH, "//input[@id = 'continue']")
    PASSWORD_FIELD = (By.XPATH, "//input[@type = 'password']")
    SIGN_IN_BUTTON = (By.XPATH, "//input[@id = 'signInSubmit']")

    def __init__(self, driver):
        super().__init__(driver)

    def enter_email(self):
        self.enter_input(self.EMAIL_FIELD, TestData.EMAIL)

    def click_continue(self):
        self.button_click(self.CONTINUE_BUTTON)

    def enter_password(self):
        self.enter_input(self.PASSWORD_FIELD, TestData.PASSWORD)

    def click_sign_in(self):
        self.button_click(self.SIGN_IN_BUTTON)

    def is_page_opened(self):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.EMAIL_FIELD)).is_displayed()


