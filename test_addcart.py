import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.test_addpocart import Cart




driver = webdriver.Chrome()
cart = Cart(driver)
@pytest.fixture()
def pre_test(request):
    cart.load()

def teardown_module(module):
    driver.close()


def cart_empty():
    empty = driver.find_element(By.CSS_SELECTOR, 'div > h1').text
    assert "Ваша корзина пуста" in empty, 'корзина пуста'
def check_add():
    textpr = driver.find_element(By.CSS_SELECTOR, "[href^='/product/31']").text
    assert "Монокуляр Veber 7-21x21W ZOOM" in textpr, 'buy ok'

def prcount1():
    countpr = driver.find_element(By.CLASS_NAME, "form-control")
    valpr = countpr.get_attribute('value')
    assert int(valpr) == 1

def changepr():
    driver.find_element(By.CLASS_NAME, "form-control").click()
    driver.find_element(By.CLASS_NAME, "form-control").send_keys(2)
    var = driver.find_element(By.CSS_SELECTOR, "body > div.container > div > div.col-md-2 > span:nth-child(3)").text
    assert var == '3998.0 р'

def clearcart():
    driver.find_element(By.LINK_TEXT, "Удалить").click()

def test_auth_positive(pre_test):
    cart.load()
    cart.addcart()
    cart.opencart()
    check_add()
    prcount1()
    changepr()
    clearcart()
    cart_empty()
