from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import BookPageLocators
from selenium.common.exceptions import NoAlertPresentException
import math
import time

class BookPage(BasePage):
    def vseRabotaet(self):
        self.should_be_correct_success_message()
        self.solve_quiz_and_get_code()
        self.should_be_correct_product_name()

    def should_be_correct_success_message(self):
        add_to_cart_button = self.browser.find_element(*BookPageLocators.ADD_TO_CART_BUTTON)
        add_to_cart_button.click()
    
    def should_be_correct_product_name(self):
        success_message = self.browser.find_element(*BookPageLocators.SUCCESS_MESSAGE)
        book_name = self.browser.find_element(*BookPageLocators.PRODUCT_NAME).text
        assert book_name in success_message.text 
    
    def should_be_correct_cart_price(self):
        book_price = self.browser.find_element(*BookPageLocators.PRODUCT_PRICE).text.split('&')[1]
        cart_price = self.browser.find_element(*BookPageLocators.CART_PRICE).text.split('&')[1]
        assert book_price == cart_price

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
            #time.sleep(100000)
        except NoAlertPresentException:
            print("No second alert presented")