from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Locators import Locators


class TestConstructorNavigation:
    def test_navigate_to_buns_section(self, driver):
        driver.find_element(*Locators.SAUCES_TAB).click()
        driver.find_element(*Locators.BUNS_TAB).click()
        assert WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(Locators.BURGER_INGREDIENTS_SECTION_BUNS)
        ).is_displayed()

    def test_navigate_to_sauces_section(self, driver):
        driver.find_element(*Locators.SAUCES_TAB).click()
        assert WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(Locators.BURGER_INGREDIENTS_SECTION_SAUCES)
        ).is_displayed()

    def test_navigate_to_fillings_section(self, driver):
        driver.find_element(*Locators.FILLINGS_TAB).click()
        assert WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(Locators.BURGER_INGREDIENTS_SECTION_FILLINGS)
        ).is_displayed()

