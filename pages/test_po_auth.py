from selenium.webdriver.common.by import By

class AuthPage:
    URL = "http://testshop.sedtest-school.ru/users/auth/"
    EMAIL_INPUT = (By.ID, "id_email")
    PASSWORD_INPUT = (By.ID, "id_password")
    HEADER = (By.CSS_SELECTOR, "#firstHeading")
    AUTH_BUTTON = (By.CSS_SELECTOR, 'button')


    def __init__(self, driver):
        self.driver = driver
    def load(self):
        self.driver.get(self.URL)
    def auth_all(self, phrase, phrase1):
        self.driver.find_element(*self.EMAIL_INPUT).send_keys(phrase)
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(phrase1)
        self.driver.find_element(*self.AUTH_BUTTON).click()

   


