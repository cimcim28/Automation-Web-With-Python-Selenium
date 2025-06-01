import logging

from locators.checkout_locator import CheckoutLocator
from pages.base_page import BasePage

logger = logging.getLogger(__name__)

class CheckoutPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = CheckoutLocator

    def click_checkout(self):
        """Click checkout button"""
        self.click_element(CheckoutLocator.BUTTON_CHECKOUT)

    def fill_checkout_form(self, first_name, last_name, postal_code):
        """Fill in checkout form fields"""
        self.input_text(self.locators.FIELD_FIRST_NAME, first_name)
        self.input_text(self.locators.FIELD_LAST_NAME, last_name)
        self.input_text(self.locators.FIELD_POSTAL_CODE, postal_code)

    def click_continue(self):
        """Click the continue button after filling form"""
        self.click_element(self.locators.BUTTON_CONTINUE)

    def click_finish(self):
        """Click the finish button on the review page"""
        self.click_element(self.locators.BUTTON_FINISH)

    def get_complete_title(self):
        """Get title text after checkout is complete"""
        return self.get_text(self.locators.TITLE_COMPLETE)


