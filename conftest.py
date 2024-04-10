import pytest
from selenium import webdriver
import settings
from locators import Locators
from data import ServiceTestData
from selenium.webdriver.support import expected_conditions as EC, expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import random


@pytest.fixture(scope='function')
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.get(settings.URL)

    yield chrome_driver

    chrome_driver.quit()




