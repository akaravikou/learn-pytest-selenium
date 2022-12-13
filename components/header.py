from selenium.webdriver.common.by import By

from page.abstractPage import AbstractPage
from page.searchResultPage import SearchResultPage
from page.signInPage import SignInPage


class Header(AbstractPage):

    LOGO = (By.XPATH, "//*[@aria-label = 'Amazon']")
    SIGN_IN_BUTTON = (By.XPATH, "//span[contains(text(),'Account & Lists')]")
    USERNAME_BUTTON = (By.XPATH, "//*[contains(text(), 'Hello')]")
    SEARCH_FIELD = (By.XPATH, "//input[@type = 'text']")
    SEARCH_BUTTON = (By.XPATH, "//input[@id = 'nav-search-submit-button']")

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

    def search_input(self, text):
        self.enter_input(self.SEARCH_FIELD, text)

    def click_search_button(self):
        self.button_click(self.SEARCH_BUTTON)
        return SearchResultPage(self.driver)
