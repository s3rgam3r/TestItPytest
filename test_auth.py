import pytest
from selenium import webdriver
from pages.test_po_auth import AuthPage
driver = webdriver.Chrome()
auth = AuthPage(driver)

@pytest.fixture()
def pre_test(request):
    auth.load()

def teardown_module(module):
    driver.close()
def check_auth(phrase):
    assert phrase in driver.title

def test_auth_positive(pre_test):
    auth.auth_all('shabakovsergei@yandex.ru', '123456')
    check_auth('TestGym')

def test_auth_negative(pre_test):
    auth.auth_all('Meow', 'Purr')
    check_auth('Авторизация')









