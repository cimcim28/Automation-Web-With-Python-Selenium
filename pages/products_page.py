import logging
from selenium.webdriver.common.by import By
from locators.products_locator import ProductsLocator
from pages.base_page import BasePage
from selenium.common.exceptions import NoSuchElementException

logger = logging.getLogger(__name__)

class ProductsPage(BasePage):
    """Products page class with all product-related actions"""

    def __init__(self, driver):
        super().__init__(driver)
        self.locators = ProductsLocator

    def add_to_cart(self, product_name):
        product_id = product_name.lower().replace(" ", "-")
        data_test = f"add-to-cart-{product_id}"
        try:
            logger.info(f"Adding product to cart: {product_name}")
            self.driver.find_element(By.CSS_SELECTOR, f"[data-test='{data_test}']").click()
        except NoSuchElementException:
            logger.error(f"Add to cart button for '{product_name}' not found.")
            raise

    def remove_from_cart(self, product_name):
        """Click the Remove button for the given product"""
        try:
            logger.info(f"Removing product from cart: {product_name}")
            product_id = product_name.lower().replace(" ", "-")
            data_test = f"remove-{product_id}"
            self.driver.find_element(By.CSS_SELECTOR, f"[data-test='{data_test}']").click()
        except NoSuchElementException:
            logger.error(f"Remove button for '{product_name}' not found.")
            raise

    def click_cart(self):
        """Click cart"""
        self.click_element(ProductsLocator.SHOPPING_CART_LINK)

    def get_cart_product_names(self):
        """Return list of product names currently in the cart overview page"""
        logger.info("Getting product names from cart overview")
        product_elements = self.driver.find_elements(By.CLASS_NAME, "inventory_item_name")
        return [element.text for element in product_elements]

    def is_product_in_cart(self, product_name):
        """Check if product is in cart by checking cart badge count"""
        try:
            badge = self.driver.find_element(*self.locators.SHOPPING_CART_BADGE)
            if badge.is_displayed() and int(badge.text) > 0:
                logger.info(f"{product_name} is in the cart.")
                return True
        except NoSuchElementException:
            logger.warning("Cart badge not found or product not in cart.")
        return False