from pytest import fixture
from selenium import webdriver


@fixture()
def browser():
    browser = webdriver.Chrome("C:/Chromedriver/chromedriver.exe")
    yield browser
    browser.close()
