import pytest
from pages.login_page import LoginPage
from configuration.config import config
import logging

logger = logging.getLogger(__name__)

class TestLogin:
    """Login test cases"""

    @pytest.fixture(autouse=True)
    def setup(self, browser_setup):
        """Setup for each test method"""
        self.driver = browser_setup
        self.login_page = LoginPage(self.driver)

    def test_successful_login(self):
        """Test successful login with valid credentials"""
        logger.info("Starting test: successful login")

        # Open login page
        self.login_page.open()

        # Perform login
        self.login_page.login(config.STANDARD_USER, config.PASSWORD)

        # Verify login success
        assert self.login_page.is_products_page_displayed(), "Products page not displayed after login"

        products_title = self.login_page.get_products_title()
        assert "Products" in products_title, f"Expected 'Products' in title, got: {products_title}"

        logger.info("Test completed: successful login")

    @pytest.mark.parametrize("username,password,expected_error", [
        ("", "", "Username is required"),
        ("", "valid_password", "Username is required"),
        ("valid_username", "", "Password is required"),
        ("invalid_user", "invalid_password", "do not match"),
        ("locked_out_user", config.PASSWORD, "locked out"),
        ("problem_user", "wrong_password", "do not match"),
    ])
    def test_login_with_invalid_credentials(self, username, password, expected_error):
        """Test login with various invalid credential scenarios"""
        logger.info(
            f"Starting test: login with credentials - username: '{username}', password: '{'*' * len(password)}'")

        # Open login page
        self.login_page.open()

        # Attempt login with provided credentials
        self.login_page.login(username, password)

        # Verify error message is displayed
        assert self.login_page.is_error_message_displayed(), "Error message not displayed"

        error_message = self.login_page.get_error_message()
        assert expected_error in error_message, f"Expected '{expected_error}' in error message, got: {error_message}"

        logger.info(f"Test completed: login with invalid credentials - {expected_error}")

    @pytest.mark.parametrize("valid_username", [
        config.STANDARD_USER,
        config.PERFORMANCE_GLITCH_USER,
        config.PROBLEM_USER,
        # Add more valid users if available
    ])
    def test_successful_login_multiple_users(self, valid_username):
        """Test successful login with multiple valid users"""
        logger.info(f"Starting test: successful login for user: {valid_username}")

        # Open login page
        self.login_page.open()

        # Perform login
        self.login_page.login(valid_username, config.PASSWORD)

        # Verify login success
        assert self.login_page.is_products_page_displayed(), f"Products page not displayed for user: {valid_username}"

        products_title = self.login_page.get_products_title()
        assert "Products" in products_title, f"Expected 'Products' in title for user {valid_username}, got: {products_title}"

        logger.info(f"Test completed: successful login for user: {valid_username}")