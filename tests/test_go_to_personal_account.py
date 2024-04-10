import time
import settings
from locators import Locators
from data import ServiceTestData
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestGoToAccount:

    def test_go_to_account(self, driver):
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

        WebDriverWait(driver, settings.MAX_WAIT_TIME).until(
            expected_conditions.element_to_be_clickable(Locators.CHECKOUT_BUTTON))

        account_button = driver.find_element(*Locators.PERSONAL_BUTTON)
        account_button.click()

        WebDriverWait(driver, settings.MAX_WAIT_TIME).until(
            expected_conditions.element_to_be_clickable(Locators.PROFILE))

        assert driver.find_element(*Locators.PROFILE).text == "Профиль"
