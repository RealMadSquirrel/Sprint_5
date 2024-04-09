from selenium.webdriver.common.by import By


class Locators:
    REGISTRATION_BUTTON = (By.XPATH, "//a[text() = 'Зарегистрироваться']") #ссылка для регистрации

    LOGIN_NAME_INPUT = (By.XPATH, "//label[text()='Имя']/following-sibling::input[@type = 'text']") #поле для ввода имени
    LOGIN_EMAIL_INPUT = (By.XPATH, "//label[text() = 'Email']/following-sibling::input[@type = 'text']") #поле для ввода почты
    LOGIN_PASSWORD_INPUT = (By.XPATH, "//input[@type='password' and @name='Пароль']") #поле для ввода пароля
    LOGIN_SUBMIT = (By.XPATH, "//button[text() = 'Зарегистрироваться']") # кнопка регистрации
    BUTTON_GO= (By.XPATH, "//button[text() = 'Войти']") #кнопка Войти
    REG_FALSE = (By.XPATH, "//p[text() = 'Такой пользователь уже существует']") #поле Такой пользователь уже существует

    LOGIN_TO_ACCOUNT_BUTTON = (By.XPATH, "//button[text() = 'Войти в аккаунт']") #войти в аккаунт
    CHECKOUT_BUTTON = (By.XPATH, "//button[text() = 'Оформить заказ']") #кнопка Оформить заказ
    PERSONAL_BUTTON = (By.XPATH, "//a[@href = '/account']") # ссылка на Личный Кабинет
    LOGIN_BUTTON = (By.XPATH, "//a[@href = '/login']") # Ссылка на Войти
    FORGOT_PASSWORD_BUTTON = (By.XPATH, "//a[text() = 'Восстановить пароль']") #Восстановить пароль
    PROFILE = (By.XPATH, "//a[text() = 'Профиль']") # Профиль
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text() = 'Конструктор']/parent::a") # Переход в раздел конструктор
    EXIT_BUTTON = (By.XPATH, "//button[text() = 'Выход']") # Выход из аккаунта

    FILLING_BUTTON = (By.XPATH, "//span[text() = 'Начинки']")
    FILLING_BUTTON_TEST = (By.XPATH, "//h2[text() = 'Начинки']")

    SAUCE_BUTTON = (By.XPATH, "//span[text() = 'Соусы']")
    SAUCE_BUTTON_TEST = (By.XPATH, "//h2[text() = 'Соусы']")

    BUN_BUTTON =(By.XPATH, "//span[text() = 'Булки']")
    BUN_BUTTON_TEST = (By.XPATH, "//h2[text() = 'Булки']")