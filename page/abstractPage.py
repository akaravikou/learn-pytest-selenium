from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config.config import TestData


class AbstractPage:

    def __init__(self, driver):
        self.driver = driver

    def open_page(self):
        self.driver.get(TestData.BASE_URL)

    def button_click(self, element):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(element)).click()

    def enter_input(self, element, text):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(element)).send_keys(text)

    def get_text(self, element):
        web_element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(element))
        return web_element.text

    def is_page_opened(self):
        return self.driver.current_url == TestData.BASE_URL
