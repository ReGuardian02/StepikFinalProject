from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_correct_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_correct_login_url(self):
        assert "login" in self.browser.current_url, "You're on the wrong page"

    def should_be_login_form(self):
        login_email_field = self.browser.find_element(*LoginPageLocators.LOGIN_EMAIL)
        login_password_field = self.browser.find_element(*LoginPageLocators.LOGIN_PASSWORD)
        assert login_email_field and login_password_field is not None, 'No/not all login fields were found'

    def should_be_register_form(self):
        registration_email_field = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL)
        registration_password_1_field = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD_1)
        registration_password_2_field = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD_2)
        assert registration_email_field and registration_password_1_field and registration_password_2_field is not None, 'No/not all registration fields were found'