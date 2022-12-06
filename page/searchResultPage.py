from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

from page.abstractPage import AbstractPage


class SearchResultPage(AbstractPage):
    INFO_BAR = (By.XPATH, "//*[@data-component-type = 's-result-info-bar']")
    SEARCHED_RESULT_LIST = (By.XPATH, "//span[@data-component-type = 's-search-results']")

    def is_page_opened(self):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.INFO_BAR)).is_displayed()

    def get_product_number(self):
        return len(self.SEARCHED_RESULT_LIST)

    def check_product_title(self, match_word):
        product_titles = self.driver.find_elements(By.XPATH, "//span[@data-component-type = 's-search-results']")
        webelements_to_text = list(map(lambda x: x.text, product_titles))
        lower_list = list(map(lambda x: x.lower(), webelements_to_text))
        list_of_containing_values = list(filter(lambda x: match_word in x, lower_list))
        return True if len(product_titles) == len(list_of_containing_values) else False









