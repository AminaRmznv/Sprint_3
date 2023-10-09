from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Locators import Locators


class TestPersonalAccount:
    def test_go_to_personal_account(self, driver, auth):
        driver.find_element(*Locators.PRIVATE_ACCOUNT_TEXT).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(
            Locators.ACCOUNT_NAV))

        assert driver.find_element(*Locators.ACCOUNT_NAV).is_displayed()
