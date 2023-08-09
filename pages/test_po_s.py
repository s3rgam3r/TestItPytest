import pytest
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
class SearchPage:
    URL = "http://testshop.sedtest-school.ru/"
    SEARCH_INPUT = (By.CSS_SELECTOR, '[name="search"]')
    HEADER = (By.CSS_SELECTOR, "#firstHeading")

    def __init__(self, driver):
        self.driver = driver
    def load(self):
        self.driver.get(self.URL)

    @pytest.mark.slow
    def searchinput(self, phrase):
        self.driver.find_element(*self.SEARCH_INPUT).send_keys(phrase)
        self.driver.find_element(*self.SEARCH_INPUT).send_keys(Keys.ENTER)