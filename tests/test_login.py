from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Locators import Locators

class TestLogin:
    def test_login_via_button_enter_account(self, driver):
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        driver.find_element(*Locators.USERNAME_FIELD).send_keys("aminaramazanova1333@yandex.by")
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys("aA123456")
        driver.find_element(*Locators.SUBMIT_LOGIN_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
                    Locators.BURGER_INGREDIENTS_SECTION))

        assert driver.find_element(*Locators.PRIVATE_ACCOUNT_TEXT).is_displayed()

    def test_login_via_private_account(self, driver):
        driver.find_element(*Locators.PRIVATE_ACCOUNT_TEXT).click()
        driver.find_element(*Locators.USERNAME_FIELD).send_keys("aminaramazanova1333@yandex.by")
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys("aA123456")
        driver.find_element(*Locators.SUBMIT_LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located(Locators.BURGER_INGREDIENTS_SECTION))

        assert driver.find_element(*Locators.PRIVATE_ACCOUNT_TEXT).is_displayed()

    def test_login_via_registration_page(self, driver):
        driver.find_element(*Locators.PRIVATE_ACCOUNT_TEXT).click()
        driver.find_element(*Locators.REGISTER_LINK).click()
        driver.find_element(*Locators.LOGIN_LINK).click()
        driver.find_element(*Locators.USERNAME_FIELD).send_keys("aminaramazanova1333@yandex.by")
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys("aA123456")
        driver.find_element(*Locators.SUBMIT_LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(
                EC.visibility_of_element_located(
                    Locators.BURGER_INGREDIENTS_SECTION))

        assert driver.find_element(*Locators.PRIVATE_ACCOUNT_TEXT).is_displayed()

    def test_login_via_forgot_password_page(self, driver):
        driver.find_element(*Locators.PRIVATE_ACCOUNT_TEXT).click()
        driver.find_element(*Locators.FORGOT_PASSWORD_LINK).click()
        driver.find_element(*Locators.LOGIN_LINK).click()
        driver.find_element(*Locators.USERNAME_FIELD).send_keys("aminaramazanova1333@yandex.by")
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys("aA123456")
        driver.find_element(*Locators.SUBMIT_LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(
                EC.visibility_of_element_located(
                    Locators.BURGER_INGREDIENTS_SECTION))

        assert driver.find_element(*Locators.PRIVATE_ACCOUNT_TEXT).is_displayed()
