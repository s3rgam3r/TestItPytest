from selenium.webdriver.common.by import By


class CheckProduct:
    URL = "http://testshop.sedtest-school.ru/"
    SEARCH_PRODUCT = (By.CSS_SELECTOR, 'a > img')


    def __init__(self, driver):
        self.driver = driver

    def load(self, product_id):
        url = f"http://testshop.sedtest-school.ru/product/{product_id}/"
        self.driver.get(url)

    def searchproduct(self):
        self.driver.find_element(*self.SEARCH_PRODUCT).click()












