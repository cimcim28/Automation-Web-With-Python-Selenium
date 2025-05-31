from selenium.webdriver.common.by import By

class ProductsLocator:
    """Locators for products page elements"""
    # Header elements
    PRODUCTS_TITLE = (By.CLASS_NAME, "title")
    SHOPPING_CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    SHOPPING_CART_LINK = (By.CLASS_NAME, "shopping_cart_link")

    # Product grid
    INVENTORY_LIST = (By.CLASS_NAME, "inventory_list")
    INVENTORY_ITEMS = (By.CLASS_NAME, "inventory_item")

    # Product item elements
    PRODUCT_NAME = (By.CLASS_NAME, "inventory_item_name")
    PRODUCT_DESCRIPTION = (By.CLASS_NAME, "inventory_item_desc")
    PRODUCT_PRICE = (By.CLASS_NAME, "inventory_item_price")
    PRODUCT_IMAGE = (By.CLASS_NAME, "inventory_item_img")

    # Menu
    MENU_BUTTON = (By.ID, "react-burger-menu-btn")
    LOGOUT_LINK = (By.ID, "logout_sidebar_link")

