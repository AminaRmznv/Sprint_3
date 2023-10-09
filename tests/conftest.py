import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from data import BASE_URL
from data import Credentials


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--window-size=1200,600")
    service = Service(ChromeDriverManager().install())
    browser = webdriver.Chrome(options=options, service=service)
    browser.get(BASE_URL)

    yield browser
    browser.quit()

@pytest.fixture
def auth(driver):
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from Locators import Locators
    driver.find_element(*Locators.LOGIN_BUTTON).click()
    driver.find_element(*Locators.USERNAME_FIELD).send_keys(Credentials.USERNAME)
    driver.find_element(*Locators.PASSWORD_FIELD).send_keys(Credentials.PASSWORD)
    driver.find_element(*Locators.SUBMIT_LOGIN_BUTTON).click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
        Locators.BURGER_INGREDIENTS_SECTION))