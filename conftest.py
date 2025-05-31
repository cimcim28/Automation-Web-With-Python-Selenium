# conftest.py - Final clean version
import pytest
import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

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
    options.add_argument("--start-maximized")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-logging")
    options.add_argument("--log-level=3")

    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(10)

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