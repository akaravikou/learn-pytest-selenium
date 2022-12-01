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
        answer = False
        for title in product_titles:
            title = (str(title.text)).lower()
            if title.__contains__(match_word):
                answer = True
            else:
                answer = False
                break
        return answer








