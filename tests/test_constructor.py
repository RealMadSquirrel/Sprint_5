from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

import settings
from data import ServiceTestData
from locators import Locators


class TestConstructor:

    def test_go_to_filling(self, driver):
        driver.get(settings.URL)
        registration_button = driver.find_element(*Locators.LOGIN_TO_ACCOUNT_BUTTON)
        registration_button.click()

        WebDriverWait(driver, settings.MAX_WAIT_TIME).until(
            expected_conditions.element_to_be_clickable(Locators.BUTTON_GO))

        email_input = driver.find_element(*Locators.LOGIN_EMAIL_INPUT)
        email_input.send_keys(ServiceTestData.AUTH_EMAIL)

        password_input = driver.find_element(*Locators.LOGIN_PASSWORD_INPUT)
        password_input.send_keys(ServiceTestData.AUTH_PASSWORD)

        go_to_button = driver.find_element(*Locators.BUTTON_GO)
        go_to_button.click()
        account_button = driver.find_element(*Locators.PERSONAL_BUTTON)
        account_button.click()
        constructor_button = driver.find_element(*Locators.CONSTRUCTOR_BUTTON)
        constructor_button.click()

        WebDriverWait(driver, settings.MAX_WAIT_TIME).until(
            expected_conditions.element_to_be_clickable(Locators.CHECKOUT_BUTTON))

        filling_button = driver.find_element(*Locators.FILLING_BUTTON)
        filling_button.click()

        assert driver.find_element(*Locators.FILLING_BUTTON_TEST).text == "Начинки"

    def test_go_to_sauce(self, driver):
        driver.get(settings.URL)
        registration_button = driver.find_element(*Locators.LOGIN_TO_ACCOUNT_BUTTON)
        registration_button.click()

        WebDriverWait(driver, settings.MAX_WAIT_TIME).until(
            expected_conditions.element_to_be_clickable(Locators.BUTTON_GO))

        email_input = driver.find_element(*Locators.LOGIN_EMAIL_INPUT)
        email_input.send_keys(ServiceTestData.AUTH_EMAIL)

        password_input = driver.find_element(*Locators.LOGIN_PASSWORD_INPUT)
        password_input.send_keys(ServiceTestData.AUTH_PASSWORD)

        go_to_button = driver.find_element(*Locators.BUTTON_GO)
        go_to_button.click()
        account_button = driver.find_element(*Locators.PERSONAL_BUTTON)
        account_button.click()
        constructor_button = driver.find_element(*Locators.CONSTRUCTOR_BUTTON)
        constructor_button.click()
        WebDriverWait(driver, settings.MAX_WAIT_TIME).until(
            expected_conditions.element_to_be_clickable(Locators.CHECKOUT_BUTTON))
        sauce_button = driver.find_element(*Locators.SAUCE_BUTTON)
        sauce_button.click()

        assert driver.find_element(*Locators.SAUCE_BUTTON_TEST).text == "Соусы"

    def test_go_to_bun(self, driver):
        driver.get(settings.URL)
        registration_button = driver.find_element(*Locators.LOGIN_TO_ACCOUNT_BUTTON)
        registration_button.click()

        WebDriverWait(driver, settings.MAX_WAIT_TIME).until(
            expected_conditions.element_to_be_clickable(Locators.BUTTON_GO))

        email_input = driver.find_element(*Locators.LOGIN_EMAIL_INPUT)
        email_input.send_keys(ServiceTestData.AUTH_EMAIL)

        password_input = driver.find_element(*Locators.LOGIN_PASSWORD_INPUT)
        password_input.send_keys(ServiceTestData.AUTH_PASSWORD)

        go_to_button = driver.find_element(*Locators.BUTTON_GO)
        go_to_button.click()
        account_button = driver.find_element(*Locators.PERSONAL_BUTTON)
        account_button.click()
        constructor_button = driver.find_element(*Locators.CONSTRUCTOR_BUTTON)
        constructor_button.click()

        WebDriverWait(driver, settings.MAX_WAIT_TIME).until(
            expected_conditions.element_to_be_clickable(Locators.CHECKOUT_BUTTON))

        sauce_button = driver.find_element(*Locators.SAUCE_BUTTON)
        sauce_button.click()
        bun_button = driver.find_element(*Locators.BUN_BUTTON)
        bun_button.click()

        assert driver.find_element(*Locators.BUN_BUTTON_TEST).text == "Булки"
