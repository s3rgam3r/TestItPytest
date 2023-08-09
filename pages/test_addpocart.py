import pytest
from selenium.webdriver.common.by import By

class Cart:
    URL = "http://testshop.sedtest-school.ru/"
    ADD_CART = (By.ID, "in_cart_link_31")
    OPEN_CART = (By.CSS_SELECTOR,  "[href^='/mycart/']")
    CLEAR_CART = (By.CSS_SELECTOR,  "body > div.container > div > div.col-md-10 > div > div > div > div > div:nth-child(4) > a")

    def __init__(self, driver):
        self.driver = driver

    def load(self):
        self.driver.get(self.URL)

    def addcart(self):
        self.driver.find_element(*self.ADD_CART).click()

    def opencart(self):
        self.driver.find_element(*self.OPEN_CART).click()


    def clearcart(self):
        self.driver.find_element(*self.CLEAR_CART).click()


