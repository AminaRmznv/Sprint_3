from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Locators import Locators


class TestLogin:
    def test_go_to_personal_account(self, driver):
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        driver.find_element(*Locators.USERNAME_FIELD).send_keys("aminaramazanova1333@yandex.by")
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys("aA123456")
        driver.find_element(*Locators.SUBMIT_LOGIN_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
            Locators.BURGER_INGREDIENTS_SECTION))
        driver.find_element(*Locators.PRIVATE_ACCOUNT_TEXT).click()

        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(
            Locators.ACCOUNT_NAV))
        assert driver.find_element(*Locators.ACCOUNT_NAV).is_displayed()
