import os

import pytest
import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from configuration.config import config
from pages.login_page import LoginPage

# Configure clean logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s | %(levelname)-5s | %(name)-12s | %(message)s',
    datefmt='%H:%M:%S'
)

# Reduce selenium noise
logging.getLogger('selenium').setLevel(logging.WARNING)
logging.getLogger('urllib3').setLevel(logging.WARNING)


@pytest.fixture
def browser_setup():
    """Browser setup using installed ChromeDriver"""
    service = Service("/usr/local/bin/chromedriver")

    options = webdriver.ChromeOptions()
    options.add_argument("--remote-allow-origins=*")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-features=AutofillServerCommunication")
    options.add_argument("--disable-features=PasswordManagerOnboarding")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--enable-automation")

    # Equivalent to: options.setExperimentalOption("prefs", prefs);
    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.password_manager_leak_detection": False
    }
    options.add_experimental_option("prefs", prefs)
    options.add_experimental_option("excludeSwitches", ["enable-automation"])

    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(10)
    driver.maximize_window()

    # Perform login directly in fixture
    driver.get(config.BASE_URL)
    login_page = LoginPage(driver)
    login_page.login(config.STANDARD_USER, config.PASSWORD)

    yield driver
    driver.quit()

# Add clean separators for test logs
def pytest_runtest_setup(item):
    """Add separator before each test"""
    print(f"\n{'=' * 50}")
    print(f"🧪 TEST: {item.name}")
    print(f"{'=' * 50}")


def pytest_runtest_teardown(item, nextitem):
    """Add separator after each test"""
    print(f"{'=' * 50}")
    print("✅ TEST COMPLETED")
    print(f"{'=' * 50}\n")


# Pytest configuration
def pytest_configure(config):
    """Configure pytest settings"""
    config.addinivalue_line("markers", "smoke: Smoke tests")
    config.addinivalue_line("markers", "regression: Regression tests")
    config.addinivalue_line("markers", "slow: Slow running tests")