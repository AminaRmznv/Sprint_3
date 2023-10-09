from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Locators import Locators


class TestRegistration:
    def test_successful_registration(self, driver):
        driver.find_element(*Locators.PRIVATE_ACCOUNT_TEXT).click()
        driver.find_element(*Locators.REGISTER_LINK).click()
        WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located(Locators.REGISTRATION_NAME_FIELD))
        driver.find_element(*Locators.REGISTRATION_NAME_FIELD).send_keys("Amina Ramazanova")
        driver.find_element(*Locators.REGISTRATION_EMAIL_FIELD).send_keys("aminaramazanova1861@yandex.by")
        driver.find_element(*Locators.REGISTRATION_PASSWORD_FIELD).send_keys("pass123")
        driver.find_element(*Locators.REGISTER_BUTTON).click()
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(Locators.SUBMIT_LOGIN_BUTTON))

        assert driver.find_element(*Locators.SUBMIT_LOGIN_BUTTON).is_displayed()

    def test_incorrect_password_error(self, driver):
        driver.find_element(*Locators.PRIVATE_ACCOUNT_TEXT).click()
        driver.find_element(*Locators.REGISTER_LINK).click()
        WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located(Locators.REGISTRATION_NAME_FIELD))
        driver.find_element(*Locators.REGISTRATION_NAME_FIELD).send_keys("Amina Ramazanova")
        driver.find_element(*Locators.REGISTRATION_EMAIL_FIELD).send_keys("aminaramazanova1397@yandex.by")
        driver.find_element(*Locators.REGISTRATION_PASSWORD_FIELD).send_keys("123")
        driver.find_element(*Locators.REGISTER_BUTTON).click()

        INCORRECT_PASSWORD_ERROR = (By.XPATH, "//p[text() = 'Некорректный пароль']")
        assert driver.find_element(*INCORRECT_PASSWORD_ERROR).is_displayed()
