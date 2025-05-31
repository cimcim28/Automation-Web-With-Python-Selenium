from pages.base_page import BasePage
from locators.login_locator import LoginLocators
from configuration.config import config
import logging

logger = logging.getLogger(__name__)


class LoginPage(BasePage):
    """Login page object"""

    def __init__(self, driver):
        super().__init__(driver)

    def open(self):
        """Open login page"""
        self.visit(config.BASE_URL)
        self.wait_for_page_load()

    def enter_username(self, username):
        """Enter username"""
        self.input_text(LoginLocators.USERNAME, username)

    def enter_password(self, password):
        """Enter password"""
        self.input_text(LoginLocators.PASSWORD, password)

    def click_login_button(self):
        """Click login button"""
        self.click_element(LoginLocators.LOGIN_BUTTON)

    def login(self, username, password):
        """Perform complete login action"""
        logger.info(f"Attempting to login with username: {username}")
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()

    def is_products_page_displayed(self):
        """Check if products page is displayed after login"""
        return self.is_element_present(LoginLocators.PRODUCTS_TITLE)

    def get_products_title(self):
        """Get products page title"""
        return self.get_text(LoginLocators.PRODUCTS_TITLE)

    def is_error_message_displayed(self):
        """Check if error message is displayed"""
        return self.is_element_present(LoginLocators.ERROR_MESSAGE, timeout=5)

    def get_error_message(self):
        """Get error message text"""
        return self.get_text(LoginLocators.ERROR_MESSAGE)
