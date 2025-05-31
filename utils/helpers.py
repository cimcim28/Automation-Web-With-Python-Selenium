from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def wait_for_element(driver, locator, timeout=10):
    try:
        return WebDriverWait(driver, timeout).until(EC.presence_of_element_located(locator))
    except TimeoutException:
        print(f"Timeout: Element {locator} not found after {timeout} seconds.")
        return None

def wait_for_element_clickable(driver, locator, timeout=10):
    try:
        return WebDriverWait(driver, timeout).until(EC.element_to_be_clickable(locator))
    except TimeoutException:
        print(f"Timeout: Element {locator} not clickable after {timeout} seconds.")
        return None

def input_text(driver, by, locator, value, timeout=10):
    element = wait_for_element(driver, (by, locator), timeout)
    if element:
        element.clear()
        element.send_keys(value)

def click_element(driver, by, locator, timeout=10):
    element = wait_for_element_clickable(driver, (by, locator), timeout)
    if element:
        element.click()
