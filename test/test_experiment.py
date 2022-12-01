import sys

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestExperiment:

    @pytest.mark.experiment
    def test_experiment(self):
        driver = webdriver.Chrome(executable_path="/Users/akaravikou/Documents/chromedriver107...M1/chromedriver")
        driver.get("https://www.amazon.com/s?k=iphone&crid=2AALZKAMJ6TM1&sprefix=iphone%2Caps%2C190&ref=nb_sb_noss_1")
        searched_result = driver.find_elements(By.XPATH, "//span[@data-component-type = 's-search-results']")
        for result in searched_result:
            result = (str(result.text)).lower()
            assert result.__contains__("iphone")
            print(result)

