import time
import settings
from locators import Locators
from data import ServiceTestData
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class TestLogin:

    def test_login_to_account(self, driver):
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

        assert driver.find_element(*Locators.CHECKOUT_BUTTON).text == "Оформить заказ"

    def test_login_to_personal_area(self, driver):
        driver.get(settings.URL)
        registration_button = driver.find_element(*Locators.PERSONAL_BUTTON)
        registration_button.click() #переход по кнопке личный кабинет
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

        assert driver.find_element(*Locators.CHECKOUT_BUTTON).text == "Оформить заказ"

    def test_login_to_registration_button(self, driver):
        driver.get(settings.URL + "/register")
        registration_button = driver.find_element(*Locators.LOGIN_BUTTON)
        registration_button.click()

        email_input = driver.find_element(*Locators.LOGIN_EMAIL_INPUT)
        email_input.send_keys(ServiceTestData.AUTH_EMAIL)

        password_input = driver.find_element(*Locators.LOGIN_PASSWORD_INPUT)
        password_input.send_keys(ServiceTestData.AUTH_PASSWORD)

        go_to_button = driver.find_element(*Locators.BUTTON_GO)
        go_to_button.click()

        (WebDriverWait(driver, settings.MAX_WAIT_TIME)
         .until(EC.text_to_be_present_in_element(Locators.CHECKOUT_BUTTON,
                                                 'Оформить заказ')))

        assert driver.find_element(*Locators.CHECKOUT_BUTTON).text == "Оформить заказ"

    def test_login_to_forgot_password(self, driver):
        driver.get(settings.URL + "/login")
        registration_button = driver.find_element(*Locators.FORGOT_PASSWORD_BUTTON)
        registration_button.click()

        login_button = driver.find_element(*Locators.LOGIN_BUTTON)
        login_button.click()

        email_input = driver.find_element(*Locators.LOGIN_EMAIL_INPUT)
        email_input.send_keys(ServiceTestData.AUTH_EMAIL)

        password_input = driver.find_element(*Locators.LOGIN_PASSWORD_INPUT)
        password_input.send_keys(ServiceTestData.AUTH_PASSWORD)

        login_button = driver.find_element(*Locators.BUTTON_GO)
        login_button.click()

        (WebDriverWait(driver, settings.MAX_WAIT_TIME)
         .until(EC.text_to_be_present_in_element(Locators.CHECKOUT_BUTTON,
                                                 'Оформить заказ')))

        assert driver.find_element(*Locators.CHECKOUT_BUTTON).text == "Оформить заказ"







