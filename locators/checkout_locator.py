from selenium.webdriver.common.by import By

class CheckoutLocator:
    """Locators for checkout page elements"""
    BUTTON_CHECKOUT = (By.ID, "checkout")

    FIELD_FIRST_NAME = (By.ID, "first-name")
    FIELD_LAST_NAME = (By.ID, "last-name")
    FIELD_POSTAL_CODE = (By.ID, "postal-code")

    BUTTON_CONTINUE = (By.ID, "continue")
    BUTTON_FINISH = (By.ID, "finish")

    TITLE_COMPLETE = (By.CLASS_NAME, "complete-header")
