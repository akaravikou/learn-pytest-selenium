from components.header import Header
from page.abstractPage import AbstractPage


class AmazonMainPage(AbstractPage):

    def __init__(self, driver):
        super().__init__(driver)
        self.header = Header(self.driver)

    def click_sign_in_button(self):
        return self.header.click_sign_in_button()

    def get_user_name(self):
        return self.header.get_user_name()

    def search_input(self, text):
        self.header.search_input(text)

    def click_search_button(self):
        return self.header.click_search_button()
