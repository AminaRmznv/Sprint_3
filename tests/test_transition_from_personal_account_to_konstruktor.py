from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Locators import Locators


class TestTransitionToKonstruktor:
    def test_from_personal_account_to_konstruktor(self, driver, auth):
        driver.find_element(*Locators.PRIVATE_ACCOUNT_TEXT).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(
            Locators.ACCOUNT_NAV))
        driver.find_element(*Locators.CONSTRUCTOR_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
            Locators.BURGER_INGREDIENTS_SECTION))

        assert driver.find_element(*Locators.BURGER_INGREDIENTS_SECTION).is_displayed()
