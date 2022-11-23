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
