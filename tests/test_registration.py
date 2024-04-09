import time
import re
import settings
from locators import Locators
from data import ServiceTestData
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class TestRegistration:

    def test_registration_positive(self, driver,random_email,random_password):
        driver.get(settings.URL + "/login")
        registration_button = driver.find_element(*Locators.REGISTRATION_BUTTON)
        registration_button.click()

        name_input = driver.find_element(*Locators.LOGIN_NAME_INPUT)
        name_input.send_keys(ServiceTestData.AUTH_NAME)

        email_input = driver.find_element(*Locators.LOGIN_EMAIL_INPUT)
        email_input.send_keys(random_email)

        password_input = driver.find_element(*Locators.LOGIN_PASSWORD_INPUT)
        password_input.send_keys(random_password)

        (WebDriverWait(driver, settings.MAX_WAIT_TIME)
         .until(EC.text_to_be_present_in_element(Locators.LOGIN_SUBMIT,
                                                 'Зарегистрироваться')))
        driver.find_element(*Locators.LOGIN_SUBMIT).click()
        (WebDriverWait(driver, settings.MAX_WAIT_TIME)
         .until(EC.text_to_be_present_in_element(Locators.BUTTON_GO,
                                                 'Войти')))

        assert driver.find_element(*Locators.BUTTON_GO).text == "Войти"

    def test_registration_negative(self, driver):
        driver.get(settings.URL + "/login")
        registration_button = driver.find_element(*Locators.REGISTRATION_BUTTON)
        registration_button.click()

        name_input = driver.find_element(*Locators.LOGIN_NAME_INPUT)
        name_input.send_keys(ServiceTestData.AUTH_NAME)

        email_input = driver.find_element(*Locators.LOGIN_EMAIL_INPUT)
        email_input.send_keys(ServiceTestData.AUTH_EMAIL)

        password_input = driver.find_element(*Locators.LOGIN_PASSWORD_INPUT)
        password_input.send_keys(ServiceTestData.AUTH_PASSWORD)

        driver.find_element(*Locators.LOGIN_SUBMIT).click()
        (WebDriverWait(driver, settings.MAX_WAIT_TIME)
         .until(EC.text_to_be_present_in_element(Locators.REG_FALSE,
                                                 'Такой пользователь уже существует')))

        assert driver.find_element(*Locators.REG_FALSE).text == ServiceTestData.REG_FALSE
