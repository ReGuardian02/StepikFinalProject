from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_EMAIL = (By.CSS_SELECTOR, '[name="login-username"]')
    LOGIN_PASSWORD = (By.CSS_SELECTOR, '[name="login-password"]')
    REGISTRATION_EMAIL = (By.CSS_SELECTOR, '[name="registration-email"]')
    REGISTRATION_PASSWORD_1 = (By.CSS_SELECTOR, '[name="registration-password1"]')
    REGISTRATION_PASSWORD_2 = (By.CSS_SELECTOR, '[name="registration-password2"]')


class BookPageLocators:
    ADD_TO_CART_BUTTON = (By.CLASS_NAME, 'btn-add-to-basket')
    SUCCESS_MESSAGE_NAME = (By.CSS_SELECTOR, '#messages :nth-child(1) .alertinner strong')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main :nth-child(1)')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.product_main .price_color')
    CART_PRICE = (By.CSS_SELECTOR, '#messages :nth-child(3) .alertinner :nth-child(1) :nth-child(1)')
    SUCCESS_MESSAGE = (By.XPATH, "//strong[text()='Coders at Work']")
