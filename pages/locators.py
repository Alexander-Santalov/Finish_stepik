from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    BASKET_BUTTON = (By.CSS_SELECTOR, "button[value='Add to basket']")
    NAME_BOOK = (By.CSS_SELECTOR, ".product_main h1")
    PRICE_BOOK = (By.CSS_SELECTOR, ".product_main p.price_color")
    PRICE_IN_BASKET = (By.CSS_SELECTOR, "#messages p strong")
    NAME_IN_BASKET = (By.CSS_SELECTOR, "#messages div:first-child strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages div:first-child")


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")