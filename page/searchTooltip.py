from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from page.abstractPage import AbstractPage


class SearchTooltip(AbstractPage):
    TOOLTIP = (By.XPATH, "//*[@class = 'autocomplete-results-container']")

    def is_element_present(self):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.TOOLTIP)).is_displayed()
