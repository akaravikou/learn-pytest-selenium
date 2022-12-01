import pytest

from page.amazonMainPage import AmazonMainPage
from test.abstract_test import AbstractTest


class TestSearchByBrandName(AbstractTest):

    @pytest.mark.parametrize("brand_name", ["apple", "sony", "samsung", "dell", "intel"])
    def test_search_by_brand_name(self, brand_name):
        self.amazonMainPage = AmazonMainPage(self.driver)
        self.amazonMainPage.open_page()
        assert self.amazonMainPage.is_page_opened(), "Main page isn't opened"
        self.amazonMainPage.search_input(brand_name)
        self.searchResultPage = self.amazonMainPage.click_search_button()
        assert self.searchResultPage.is_page_opened(), "Search result page isn't opened"
        assert self.searchResultPage.get_product_number() > 0, "There are no products"
        assert self.searchResultPage.check_product_title(brand_name), "Current product doesn't contain brand name in " \
                                                                      "search field"
