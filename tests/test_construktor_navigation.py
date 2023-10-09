from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Locators import Locators


class TestConstructorNavigation:
    def test_navigate_to_buns_section(self, driver):
        driver.find_element(*Locators.SAUCES_TAB).click()
        driver.find_element(*Locators.BUNS_TAB).click()
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(Locators.BURGER_INGREDIENTS_SECTION_ACTIVE)
        ).is_displayed()
        assert driver.find_element(*Locators.BURGER_INGREDIENTS_SECTION_ACTIVE).text == "Булки"

    def test_navigate_to_sauces_section(self, driver):
        driver.find_element(*Locators.SAUCES_TAB).click()
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(Locators.BURGER_INGREDIENTS_SECTION_ACTIVE)
        ).is_displayed()
        assert driver.find_element(*Locators.BURGER_INGREDIENTS_SECTION_ACTIVE).text == "Соусы"

    def test_navigate_to_fillings_section(self, driver):
        driver.find_element(*Locators.FILLINGS_TAB).click()
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(Locators.BURGER_INGREDIENTS_SECTION_ACTIVE)
        ).is_displayed()
        assert driver.find_element(*Locators.BURGER_INGREDIENTS_SECTION_ACTIVE).text == "Начинки"
