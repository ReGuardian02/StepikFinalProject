from selenium.webdriver.common.by import By
from pages.book_page import BookPage
import time

def test_adding_book_to_cart(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = BookPage(browser, link)
    page.open()
    page.vseRabotaet()