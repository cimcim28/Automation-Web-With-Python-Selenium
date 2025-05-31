import logging
import pytest
from pages.products_page import ProductsPage

logger = logging.getLogger(__name__)

class TestProducts:
    """Test cases for Products page functionality"""

    @pytest.fixture(autouse=True)
    def setup(self, browser_setup):
        """Setup for each test method"""
        self.driver = browser_setup
        self.products_page = ProductsPage(self.driver)


    def add_multiple_products(self, products):
        """Helper to add multiple products and go to cart page"""
        for product_name in products:
            self.products_page.add_to_cart(product_name)
        self.products_page.click_cart()

    def test_add_product_to_cart(self):
        """Test adding a single product to cart"""
        logger.info("Starting test: add product to cart")

        product_name = "Sauce Labs Backpack"
        self.products_page.add_to_cart(product_name)
        self.products_page.click_cart()

        assert self.products_page.is_product_in_cart(product_name), \
            f"{product_name} was not added to cart"

    def test_remove_product_to_cart(self):
        """Test removing a single product from cart"""
        logger.info("Starting test: remove product from cart")

        product_name = "Sauce Labs Backpack"
        self.add_multiple_products([product_name])  # add and go to cart

        # Ensure it appears in cart first
        assert self.products_page.is_product_in_cart(product_name), \
            f"{product_name} was not found in cart after adding."

        # Remove and verify it's gone
        self.products_page.remove_from_cart(product_name)

        assert not self.products_page.is_product_in_cart(product_name), \
            f"{product_name} was not removed from cart"

    def test_add_multiple_products_to_cart(self):
        """Test adding multiple products to cart"""
        logger.info("Starting test: add multiple products to cart")

        products_to_add = [
            "Sauce Labs Backpack",
            "Sauce Labs Bike Light",
            "Sauce Labs Bolt T-Shirt"
        ]
        self.add_multiple_products(products_to_add)

        for product_name in products_to_add:
            assert self.products_page.is_product_in_cart(product_name), \
                f"{product_name} was not found in the cart"

    @pytest.mark.parametrize("products_to_add", [
        ["Sauce Labs Backpack", "Sauce Labs Bike Light"],
        ["Sauce Labs Bolt T-Shirt", "Sauce Labs Onesie"],
        ["Sauce Labs Fleece Jacket", "Sauce Labs Backpack", "Test.allTheThings() T-Shirt (Red)"]
    ])
    def test_add_multiple_products_to_cart_parameterize(self, products_to_add):
        """Test adding multiple products to cart (parametrized)"""
        logger.info(f"Starting test: add multiple products to cart: {products_to_add}")

        self.add_multiple_products(products_to_add)

        for product_name in products_to_add:
            assert self.products_page.is_product_in_cart(product_name), \
                f"{product_name} was not found in the cart"

    def test_remove_multiple_products_to_cart(self):
        """Test removing multiple products from cart"""
        logger.info("Starting test: remove multiple products from cart")

        products_to_remove = [
            "Sauce Labs Backpack",
            "Sauce Labs Bike Light",
            "Sauce Labs Bolt T-Shirt"
        ]
        self.add_multiple_products(products_to_remove)  # add all first

        # Remove all products one by one
        for product_name in products_to_remove:
            self.products_page.remove_from_cart(product_name)

        # Verify all removed
        for product_name in products_to_remove:
            assert not self.products_page.is_product_in_cart(product_name), \
                f"{product_name} was not removed from the cart"
