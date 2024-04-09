import time
import settings
from locators import Locators
from data import ServiceTestData
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from test_login import TestLogin


class TestExitFromAccount:

    def test_exit(self, driver):
        driver.get(settings.URL)
        registration_button = driver.find_element(*Locators.LOGIN_TO_ACCOUNT_BUTTON)
        registration_button.click()
        (WebDriverWait(driver, settings.MAX_WAIT_TIME)
         .until(EC.text_to_be_present_in_element(Locators.BUTTON_GO,
                                                 'Войти')))

        email_input = driver.find_element(*Locators.LOGIN_EMAIL_INPUT)
        email_input.send_keys(ServiceTestData.AUTH_EMAIL)

        password_input = driver.find_element(*Locators.LOGIN_PASSWORD_INPUT)
        password_input.send_keys(ServiceTestData.AUTH_PASSWORD)

        go_to_button = driver.find_element(*Locators.BUTTON_GO)
        go_to_button.click()

        (WebDriverWait(driver, settings.MAX_WAIT_TIME)
         .until(EC.text_to_be_present_in_element(Locators.CHECKOUT_BUTTON,
                                                 'Оформить заказ')))
        account_button = driver.find_element(*Locators.PERSONAL_BUTTON)
        account_button.click()
        (WebDriverWait(driver, settings.MAX_WAIT_TIME)
         .until(EC.text_to_be_present_in_element(Locators.EXIT_BUTTON,
                                                 'Выход')))
        constructor_button = driver.find_element(*Locators.EXIT_BUTTON)
        constructor_button.click()
        (WebDriverWait(driver, settings.MAX_WAIT_TIME)
         .until(EC.text_to_be_present_in_element(Locators.BUTTON_GO,
                                                 'Войти')))
        time.sleep(3)
        assert driver.find_element(*Locators.BUTTON_GO).text == "Войти"