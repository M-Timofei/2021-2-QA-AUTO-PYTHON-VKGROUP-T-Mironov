from selenium.webdriver.common.by import By

class LoginPageLocators:
    CREATE_ACCOUNT_BUTTON = (By.XPATH, '//a[@href="/reg"]')
    INPUT_USERNAME = (By.XPATH, '//input[@id="username"]')
    INPUT_PASSWORD = (By.XPATH, '//input[@id="password"]')
    LOGIN_BUTTON = (By.XPATH, '//input[@id="submit"]')
    ERROR_MASSAGE = (By.XPATH, '//div[@id="flash"]')

class RegistrationPageLocators:
    INPUT_USERNAME = (By.XPATH, '//input[@id="username"]')
    INPUT_EMAIL = (By.XPATH, '//input[@id="email"]')
    INPUT_PASSWORD = (By.XPATH, '//input[@id="password"]')
    INPUT_PASSWORD_CONFIRM = (By.XPATH, '//input[@id="confirm"]')
    CHECKBOX = (By.XPATH, '//input[@id="term"]')
    REGISTRATION_BUTTON = (By.XPATH, '//input[@id="submit"]')
    ERROR_MASSAGE = (By.XPATH, '//div[@id="flash"]')

class MainPageLocators:
    LOGGED_AS = (By.XPATH, '//div[@id="login-name"]/ul/li[1]')
    VK_ID = (By.XPATH, '//div[@id="login-name"]/ul/li[2][contains(text(), "VK ID")]')
    LOGOUT_BUTTON = (By.XPATH, '//a[@href="/logout"]')
    BRAND_BUTTON = (By.XPATH, '//a[contains(@class, "uk-navbar-brand")]')
    HOME_BUTTON = (By.XPATH, '//a[text()="HOME"]')
    PYTHON_BUTTON = (By.XPATH, '//a[@href="https://www.python.org/"]')
    PYTHON_HISTORY_BUTTON = (By.XPATH, '//a[text()="Python history"]')
    PYTHON_FLASK_LOCATOR = (By.XPATH, '//a[text()="About Flask"]')
    LINUX_BUTTON = (By.XPATH, '//a[text()="Linux"]')
    LINUX_BUTTON_CENTOS = (By.XPATH, '//a[text()="Download Centos7"]')
    NETWORK_BUTTON = (By.XPATH, '//a[text()="Network"]')
    NETWORK_BUTTON_NEWS = (By.XPATH, '//a[text()="News"]')
    NETWORK_BUTTON_DOWNLOAD = (By.XPATH, '//a[text()="Download"]')
    NETWORK_BUTTON_EXAMPLES = (By.XPATH, '//a[text()="Examples "]')
    WHAT_IS_AN_API_BUTTON = (By.XPATH, '//a[contains(@href, "Application_programming_interface")]')
    FUTURE_OF_INTERNET_BUTTON = (By.XPATH, '//a[contains(@href, "future-of-the-internet")]')
    SMTP_BUTTON = (By.XPATH, '//a[contains(@href, "SMTP")]')
    PYTHON_ZEN = (By.XPATH, '//footer//p[2]')

class InvalidPageLocators:
    ERROR_MASSAGE = (By.XPATH, '//span[@id="text"]')


