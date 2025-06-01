from pages.checkout_page import CheckoutPage
from pages.products_page import ProductsPage
import logging
import pytest

logger = logging.getLogger(__name__)

class TestCheckout:
    @pytest.fixture(autouse=True)
    def setup(self, browser_setup):
        self.driver = browser_setup
        self.products_page = ProductsPage(self.driver)
        self.checkout_page = CheckoutPage(self.driver)

    def test_checkout_form(self):
        logger.info("Starting test: Checkout form submission")

        # Add product dulu
        self.products_page.add_to_cart("Sauce Labs Backpack")
        self.products_page.click_cart()

        # Klik checkout
        self.checkout_page.click_checkout()

        # Isi form
        self.checkout_page.fill_checkout_form("John", "Doe", "12345")

    def test_complete_checkout_process(self):
        logger.info("Starting test: Complete checkout process")

        # Step 1: Tambah produk
        self.products_page.add_to_cart("Sauce Labs Backpack")
        self.products_page.click_cart()

        # Step 2: Klik checkout
        self.checkout_page.click_checkout()

        # Step 3: Isi form dan continue
        self.checkout_page.fill_checkout_form("John", "Doe", "12345")
        self.checkout_page.click_continue()

        # Step 4: Klik finish
        self.checkout_page.click_finish()

        # Step 5: Verifikasi checkout selesai
        complete_title = self.checkout_page.get_complete_title()
        assert "THANK YOU FOR YOUR ORDER" in complete_title.upper(), \
            "Checkout not completed successfully"

    @pytest.mark.parametrize("products", [
        ["Sauce Labs Backpack",
        "Sauce Labs Bike Light", "Sauce Labs Onesie",
        "Sauce Labs Bolt T-Shirt", "Sauce Labs Fleece Jacket", "Test.allTheThings() T-Shirt (Red)"]
    ])
    def test_complete_checkout_process_with_parameterize(self, products):
        logger.info(f"Starting test: Complete checkout process with products: {products}")

        # Step 1: Tambahkan produk
        for product_name in products:
            self.products_page.add_to_cart(product_name)
        self.products_page.click_cart()

        # Step 2: Klik checkout
        self.checkout_page.click_checkout()

        # Step 3: Isi form dan continue
        self.checkout_page.fill_checkout_form("John", "Doe", "12345")
        self.checkout_page.click_continue()

        # Step 4: Klik finish
        self.checkout_page.click_finish()

        # Step 5: Verifikasi checkout selesai
        complete_title = self.checkout_page.get_complete_title()
        assert "THANK YOU FOR YOUR ORDER" in complete_title.upper(), \
            "Checkout not completed successfully"