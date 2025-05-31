from selenium.webdriver.common.by import By

class LoginLocators:
    """Locators for Login page elements"""
    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    PRODUCTS_TITLE = (By.CSS_SELECTOR, "[data-test='title']")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")