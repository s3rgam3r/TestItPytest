import pytest
from selenium import webdriver
import urllib
from selenium.webdriver.common.by import By
from pages.test_po_s import SearchPage

driver = webdriver.Chrome()
search = SearchPage(driver)
@pytest.fixture()

def pre_test(request):
    search.load()

def teardown_module(module):
    driver.close()
def check_auth(phrase):
    assert "search="+phrase in driver.current_url, 'Url changed'


def test_searchMain(pre_test):
    search.searchinput('ручка')
    check_auth(urllib.parse.quote('ручка'))

def test_searchCat(pre_test):
    search.searchinput('яблоко')
    check_auth(urllib.parse.quote('яблоко'))



