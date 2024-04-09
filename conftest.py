import pytest
from selenium import webdriver
import settings
import random
from data import ServiceTestData


@pytest.fixture(scope='function')
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.get(settings.URL)

    yield chrome_driver

    chrome_driver.quit()

@pytest.fixture(scope='function')
def random_email():
    email = "olgabelova7" + str(random.randrange(100,999)) +"@gmail.com"
    return email

@pytest.fixture(scope='function')
def random_password():
    password = str(random.randrange(100000,999999))
    return password
