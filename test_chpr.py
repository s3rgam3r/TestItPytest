import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.test_po_chpr import CheckProduct

driver = webdriver.Chrome()
check = CheckProduct(driver)

@pytest.fixture()

def teardown_module(module):
    driver.close()

def check_search(phrase):
    assert "http://testshop.sedtest-school.ru"+phrase in driver.current_url, 'Url changed'

def check_cardtitle(phrase):
    cardtitle = driver.find_element(By.CLASS_NAME, 'card-title').text
    assert phrase in cardtitle, 'card-title ok'

def check_txt(phrase):
    txt = driver.find_element(By.CSS_SELECTOR, 'p').text
    assert phrase in txt, 'card-title ok'

def check_buy():
    buy = driver.find_element(By.CSS_SELECTOR, "[href^='/add/in/?in=cart']").text
    assert "Добавить в корзину" in buy, 'buy ok'

def check_est():
    est = driver.find_elements(By.CSS_SELECTOR, "[href^='/product/rate']")
    assert len(est) == 5

def check_img():
    img = driver.find_element(By.CLASS_NAME, "col-md-6 > img")
    atImg = img.get_attribute('src')
    assert 'http://testshop.sedtest-school.ru/static/products' in (atImg)


def test_search_Main():
    check.load('31')
    check_search('/product/31/')
    check_cardtitle('Монокуляр Veber 7-21x21W ZOOM')
    check_txt('Монокуляр Veber 7-21x21W ZOOM')
    check_buy()
    check_est()
    check_img()

def test_search_Tw():
    check.load('29')
    check_search('/product/29/')
    check_cardtitle('Ручка Паркер')
    check_txt('Перо: нержавеющая сталь.')
    check_buy()
    check_est()
    check_img()


