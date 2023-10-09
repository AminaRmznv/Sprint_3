from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Locators import Locators


class TestLogoutFromPersonalAccount:
    def test_go_to_personal_account(self, driver, auth):
        driver.find_element(*Locators.PRIVATE_ACCOUNT_TEXT).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(
            Locators.ACCOUNT_NAV))

        driver.find_element(*Locators.LOGOUT_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(
            Locators.LOGIN_HEADER))

        assert driver.find_element(*Locators.LOGIN_HEADER).is_displayed()
