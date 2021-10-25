from selenium.webdriver.common.by import By

class BasePageLocators:
    SPINNER_LOCATOR = (By.XPATH, '//*[contains(@class,"spinner_")]')
    STATISTICS_BUTTON_LOCATOR = (By.XPATH, '//*[@href="/statistics"]')
    TOOLS_BUTTON_LOCATOR = (By.XPATH, '//*[@href="/tools"]')

class LoginPageLocators:
    LOGIN_BUTTON_LOCATOR = (By.XPATH, '//*[contains(@class,"responseHead-module-button")]')
    LOGIN_LOCATOR = (By.NAME, "email")
    PASSWORD_LOCATOR = (By.NAME, "password")
    INPUT_BUTTON_LOCATOR = (By.XPATH, '//*[contains(@class,"authForm-module-button")]')

class DashboardPageLocators:
    ACCOUNT_BUTTON_LOCATOR = (By.XPATH, '//*[contains(@class,"right-module-rightButton")]')
    OUTPUT_BUTTON_LOCATOR = (By.XPATH, '//*[contains(@href, "/logout")]')

class ProfilePageLocators:
    GO_TO_PROFILE_BUTTON_LOCATOR = (By.XPATH, '//*[@href="/profile"]')
    CHANGE_FIO_LOCATOR = (By.XPATH, '//*[@data-name="fio"]/div/input')
    CHANGE_PHONE_LOCATOR = (By.XPATH, '//*[@data-name="phone"]/div/input')
    SAVE_CHANGES_BUTTON_LOCATOR = (By.XPATH, '//*[starts-with(@class,"button__text")]')