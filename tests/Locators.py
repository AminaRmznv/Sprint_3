from selenium.webdriver.common.by import By


class Locators:

    LOGIN_BUTTON = (By.XPATH, '//button[text()="Войти в аккаунт"]')
    SUBMIT_LOGIN_BUTTON = (By.XPATH, '//button[text()="Войти"]')


    PRIVATE_ACCOUNT_TEXT = (By.XPATH, '//p[text()="Личный Кабинет"]')

    PLACE_ORDER = (By.XPATH, '//button[text()="Оформить заказ"]')


    USERNAME_FIELD = (By.NAME, "name")
    PASSWORD_FIELD = (By.NAME, "Пароль")


    REGISTER_LINK = (By.XPATH, '//a[text()="Зарегистрироваться"]')
    LOGIN_LINK = (By.XPATH, '//a[text()="Войти"]')
    FORGOT_PASSWORD_LINK = (By.XPATH, '//a[text()="Восстановить пароль"]')


    BURGER_INGREDIENTS_SECTION = (By.XPATH, "//section[contains(@class, 'BurgerIngredients_ingredients')]")

    ACCOUNT_NAV = (By.XPATH, "//nav[contains(@class, 'Account_nav')]")

    LOGOUT_BUTTON = (By.XPATH, "//button[text() = 'Выход']")
    LOGIN_HEADER = (By.XPATH, "//h2[text() = 'Вход']")

    REGISTRATION_NAME_FIELD = (By.XPATH, "(//input[@name='name'])[1]")
    REGISTRATION_EMAIL_FIELD = (By.XPATH, "(//input[@name='name'])[2]")
    REGISTRATION_PASSWORD_FIELD = (By.NAME, "Пароль")
    REGISTER_BUTTON = (By.XPATH, '//button[text()="Зарегистрироваться"]')
    INCORRECT_PASSWORD_ERROR = (By.XPATH, "//p[text() = 'Некорректный пароль']")

    CONSTRUCTOR_BUTTON = (By.XPATH, '//p[text()="Конструктор"]')

    BUNS_TAB = (By.XPATH, "//span[text()='Булки']")
    SAUCES_TAB = (By.XPATH, "//span[text()='Соусы']")
    FILLINGS_TAB = (By.XPATH, "//span[text()='Начинки']")

    BURGER_INGREDIENTS_SECTION_ACTIVE = (By.XPATH, "//div[contains(@class,'tab_tab_type_current')]")

