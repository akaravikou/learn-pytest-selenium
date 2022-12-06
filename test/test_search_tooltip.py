from page.amazonMainPage import AmazonMainPage
from page.searchTooltip import SearchTooltip
from test.abstract_test import AbstractTest


class TestSearchTooltip(AbstractTest):

    def test_search_tooltip(self):
        self.amazonMainPage = AmazonMainPage(self.driver)
        self.amazonMainPage.open_page()
        assert self.amazonMainPage.is_page_opened(), "Main page isn't opened"
        self.amazonMainPage.search_input('s')
        self.searchTooltip = SearchTooltip(self.driver)
        assert self.searchTooltip.is_element_present(), "Tooltip don't exist"


