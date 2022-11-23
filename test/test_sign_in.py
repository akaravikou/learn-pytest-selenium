from config.config import TestData
from page.amazonMainPage import AmazonMainPage
from test.abstract_test import AbstractTest


class TestSignIn(AbstractTest):

    def test_sign_in(self):
        self.amazonMainPage = AmazonMainPage(self.driver)
        self.amazonMainPage.open_page()
        assert self.amazonMainPage.is_page_opened(), "Main page isn't opened"
        self.signInPage = self.amazonMainPage.click_sign_in_button()
        assert self.signInPage.is_page_opened(), "Sign in page isn't opened"
        self.signInPage.enter_email()
        self.signInPage.click_continue()
        self.signInPage.enter_password()
        self.signInPage.click_sign_in()
        username = self.amazonMainPage.get_user_name()
        assert username == TestData.USERNAME, "Username isn't correct"
