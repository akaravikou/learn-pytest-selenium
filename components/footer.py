
from selenium.webdriver.common.by import By

from page.abstractPage import AbstractPage


class Footer(AbstractPage):
    footer_vertical_row_links_list = ['Get to Know Us\n'
                                      'Careers\n'
                                      'Blog\n'
                                      'About Amazon\n'
                                      'Investor Relations\n'
                                      'Amazon Devices\n'
                                      'Amazon Science']

    def get_links_text(self):
        searched_result = self.driver.find_elements(By.XPATH, "(//*[@class='navFooterLinkCol navAccessibility'])[1]")
        text_list = list(map(lambda x: x.text, searched_result))
        return text_list



