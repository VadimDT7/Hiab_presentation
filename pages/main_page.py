import time
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver



class MainPage(BasePage):
    def open_finder_accessories(self):  # checking click on ProductFinderAccessories
        finder_accessories = self.driver.find_element(*MainPageLocators.FINDER_ACCESSORIES_LINK)
        finder_accessories.click()
        accessories_button = self.driver.find_element(*MainPageLocators.ACCESSORIES_BUTTON)
        accessories_button.click()

    def open_shop_link(self):  # checking shop change and clicking log HIAB
        store_link = self.driver.find_element(*MainPageLocators.STORE_LINK)
        store_link.click()
        hiab_shop_link = self.driver.find_element(*MainPageLocators.HIAB_SHOP_LNK)
        hiab_shop_link.click()
        self.switch_to_window()
        assert self.is_clickable(*MainPageLocators.HIAB_LOGO_LNK)

    def can_choose_language(self):  # language selection and display
        language_button = self.driver.find_element(*MainPageLocators.LANGUAGE_BUTTON)
        language_button.click()
        choose_language = self.driver.find_element(*MainPageLocators.CHOOSE_LANGUAGE_IT)
        choose_language.click()
        assert self.driver.find_element(*MainPageLocators.IT_ELEMENT)

    # def fill_search_field(self, send_delayed_keys):  # enter text in the search field and open search page
    #     search_field = self.driver.find_element(*MainPageLocators.SEARCH_BUTTON)
    #     search_field.click()
    #     search_field.send_keys('moffett')
    #     # print('Search button works')
    #     # time.sleep(2)
    #     # downloaded_search_field = self.driver.find_element(*MainPageLocators.DOWNLOADED_SEARCH_FIELD)
    #     # time.sleep(2)
    #     # downloaded_search_field.click()
    #     # time.sleep(2)
    #     # search_field.send_keys('hiab')
    #     print('Hiab is entered')
        # time.sleep(2)
        # submit_button = self.driver.find_element(*MainPageLocators.SUBMIT_BUTTON)
        # submit_button.click()
        # # search_field.sendKeys(Keys.ENTER)
        # time.sleep(2)
        # value = self.driver.find_element(*MainPageLocators.RESULTS_IN_ALL_TAB)
        # if value >= 1:
        #     print(value.text)

#  opening pages from header
    def about_us_page_is_opened(self):
        about_us_page = self.driver.find_element(*MainPageLocators.ABOUT_US_PAGE)
        about_us_page.click()
        assert self.driver.find_element(*MainPageLocators.ABOUT_US_BREADCRUMB)

    def sustainability_page_is_opened(self):
        sustainability_page = self.driver.find_element(*MainPageLocators.SUSTAINABILITY_PAGE)
        sustainability_page.click()
        assert self.driver.find_element(*MainPageLocators.SUSTAINABILITY_BREADCRUMB)

    def careers_page_is_opened(self):
        careers_page = self.driver.find_element(*MainPageLocators.CAREERS_PAGE)
        careers_page.click()
        assert self.driver.find_element(*MainPageLocators.CAREERS_BREADCRUMB)

    def media_page_is_opened(self):
        media_page = self.driver.find_element(*MainPageLocators.MEDIA_PAGE)
        media_page.click()
        assert self.driver.find_element(*MainPageLocators.MEDIA_BREADCRUMB)

    def club_shop_page_is_opened(self):
        club_shop_page = self.driver.find_element(*MainPageLocators.CLUB_SHOP_PAGE)
        club_shop_page.click()
        time.sleep(5)
        self.switch_to_window()
        assert self.is_clickable(*MainPageLocators.CUSTOMER_BUTTON)
        # assert self.driver.current_url == self.driver.find_element(*MainPageLocators.CLUB_SHOP_DESIRED_URL)

    def hiconnect_page_is_opened(self):
        hiconnect_page = self.driver.find_element(*MainPageLocators.HICONNECT_PORTAL_PAGE)
        hiconnect_page.click()
        time.sleep(3)
        self.switch_to_window()
        # time.sleep(3)
        element = self.driver.find_element(*MainPageLocators.HICONNECT_LOGIN_BUTTON)
        element.click()

    def find_a_dealer(self):
        contact_mega_menu = self.driver.find_element(*MainPageLocators.CONTACT_MEGA_MENU)
        contact_mega_menu.click()
        find_a_dealer_button = self.driver.find_element(*MainPageLocators.FIND_A_DEALER)
        find_a_dealer_button.click()
        assert self.is_clickable(*MainPageLocators.OUR_BRANDS)
