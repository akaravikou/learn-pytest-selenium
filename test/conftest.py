import pytest
from selenium import webdriver

from config.config import TestData


@pytest.fixture(scope='function')
def init_driver(request):
    web_driver = webdriver.Chrome(executable_path=TestData.CHROME_DRIVER_PATH)
    request.cls.driver = web_driver
    web_driver.implicitly_wait(10)
    yield
    web_driver.close()


# @pytest.fixture(scope='function')
# def check_value_in_list(value, list_of_values):
#     lower_list = list(map(lambda x: x.lower(), list_of_values))
#     list_of_containing_values = list(filter(lambda x: value in x, lower_list))
#     return True if len(list_of_values) == len(list_of_containing_values) else False
