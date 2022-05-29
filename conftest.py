from pytest import fixture
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@fixture()
def browser():
    browser = webdriver.Chrome(service=Service("C:/Chromedriver/chromedriver.exe"))
    yield browser
    browser.close()
