from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from configuration.config import config
import logging

logger = logging.getLogger(__name__)

class BasePage:
    """Base page class with common page operations"""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, config.EXPLICIT_WAIT)

    def visit(self, url):
        """Navigate to the specified URL"""
        logger.info(f"Navigating to: {url}")
        self.driver.get(url)

    def find_element(self, locator, timeout=None):
        """Find element with explicit wait"""
        try:
            timeout = timeout or config.EXPLICIT_WAIT
            return WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
        except TimeoutException:
            logger.error(f"Element not found: {locator}")
            raise NoSuchElementException(f"Element {locator} not found after {timeout} seconds")

    def find_clickable_element(self, locator, timeout=None):
        """Find clickable element with explicit wait"""
        try:
            timeout = timeout or config.EXPLICIT_WAIT
            return WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(locator)
            )
        except TimeoutException:
            logger.error(f"Element not clickable: {locator}")
            raise NoSuchElementException(f"Element {locator} not clickable after {timeout} seconds")

    def input_text(self, locator, text, timeout=None):
        """Input text into element"""
        element = self.find_element(locator, timeout)
        element.clear()
        element.send_keys(text)
        logger.info(f"Text entered into element: {locator}")

    def click_element(self, locator, timeout=None):
        """Click element"""
        element = self.find_clickable_element(locator, timeout)
        element.click()
        logger.info(f"Clicked element: {locator}")

    def get_text(self, locator, timeout=None):
        """Get text from element"""
        element = self.find_element(locator, timeout)
        return element.text

    def is_element_present(self, locator, timeout=3):
        """Check if element is present"""
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False

    def wait_for_page_load(self, timeout=None):
        """Wait for page to load completely"""
        timeout = timeout or config.EXPLICIT_WAIT
        WebDriverWait(self.driver, timeout).until(
            lambda driver: driver.execute_script("return document.readyState") == "complete"
        )