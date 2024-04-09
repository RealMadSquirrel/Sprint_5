import time
import re
import settings
from locators import Locators
from data import ServiceTestData
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from test_login import TestLogin

class TestConstructor:

    def test_go_to_filling(self, driver):
        TestLogin.test_login_to_account(self, driver)
        account_button = driver.find_element(*Locators.PERSONAL_BUTTON)
        account_button.click()
        constructor_button = driver.find_element(*Locators.CONSTRUCTOR_BUTTON)
        constructor_button.click()
        (WebDriverWait(driver, settings.MAX_WAIT_TIME)
         .until(EC.text_to_be_present_in_element(Locators.CHECKOUT_BUTTON,
                                                 'Оформить заказ')))
        filling_button = driver.find_element(*Locators.FILLING_BUTTON)
        filling_button.click()

        assert driver.find_element(*Locators.FILLING_BUTTON_TEST).text == "Начинки"

    def test_go_to_sauce(self, driver):
        TestLogin.test_login_to_account(self, driver)
        account_button = driver.find_element(*Locators.PERSONAL_BUTTON)
        account_button.click()
        constructor_button = driver.find_element(*Locators.CONSTRUCTOR_BUTTON)
        constructor_button.click()
        (WebDriverWait(driver, settings.MAX_WAIT_TIME)
         .until(EC.text_to_be_present_in_element(Locators.CHECKOUT_BUTTON,
                                                 'Оформить заказ')))
        sauce_button = driver.find_element(*Locators.SAUCE_BUTTON)
        sauce_button.click()

        assert driver.find_element(*Locators.SAUCE_BUTTON_TEST).text == "Соусы"

    def test_go_to_bun(self, driver):
        TestLogin.test_login_to_account(self, driver)
        account_button = driver.find_element(*Locators.PERSONAL_BUTTON)
        account_button.click()
        constructor_button = driver.find_element(*Locators.CONSTRUCTOR_BUTTON)
        constructor_button.click()

        (WebDriverWait(driver, settings.MAX_WAIT_TIME)
         .until(EC.text_to_be_present_in_element(Locators.CHECKOUT_BUTTON,
                                                 'Оформить заказ')))
        sauce_button = driver.find_element(*Locators.SAUCE_BUTTON)
        sauce_button.click()
        time.sleep(3)
        bun_button = driver.find_element(*Locators.BUN_BUTTON)
        bun_button.click()

        assert driver.find_element(*Locators.BUN_BUTTON_TEST).text == "Булки"