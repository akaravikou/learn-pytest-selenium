from selenium.webdriver.common.by import By

from page.abstractPage import AbstractPage
from page.signInPage import SignInPage


class AmazonMainPage(AbstractPage):
    LOGO = (By.XPATH, "//*[@aria-label = 'Amazon']")
    SIGN_IN_BUTTON = (By.XPATH, "//span[contains(text(),'Account & Lists')]")
    USERNAME_BUTTON = (By.XPATH, "//*[contains(text(), 'Hello')]")

    def __init__(self, driver):
        super().__init__(driver)

    def click_sign_in_button(self):
        self.button_click(self.SIGN_IN_BUTTON)
        return SignInPage(self.driver)

    def get_user_name(self):
        username = self.get_text(self.USERNAME_BUTTON)
        username = username.split(" ")
        username = username[1]
        return username




