import sys

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestExperiment:

    def test_experiment(self):
        footer_vertical_row_links_list = ['Get to Know Us\n'
                                          'Careers\n'
                                          'Blog\n'
                                          'About Amazon\n'
                                          'Investor Relations\n'
                                          'Amazon Devices\n'
                                          'Amazon Science']
        driver = webdriver.Chrome(executable_path="/Users/akaravikou/Documents/chromedriver107...M1/chromedriver")
        driver.get("https://www.amazon.com")
        searched_result = driver.find_elements(By.XPATH, "(//*[@class='navFooterLinkCol navAccessibility'])[1]")
        webelements_to_text = list(map(lambda x: x.text, searched_result))
        # print(webelements_to_text)
        # for result in searched_result:
        #     result = (str(result.text)).lower()
        #     assert result == title, "eRRo"
        assert webelements_to_text == footer_vertical_row_links_list
