from pages.main_page import MainPage
from allure_commons.types import AttachmentType
import allure


@allure.description("Accessories tab was opened in Product Finder")
@allure.severity(severity_level="CRITICAL")
def test_user_can_open_finder_accessories(browser):
    link = "https://hiab.com/en"
    main_page = MainPage(browser, link)
    main_page.open(link)
    main_page.open_finder_accessories()
    with allure.step('Do screenshot'):
        allure.attach(browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)


@allure.description("From the main Hiab site we can get through the 'Store' button to the Hiab webshop page")
@allure.severity(severity_level="MEDIUM")
def test_user_can_open_shop(browser):
    link = "https://hiab.com/en"
    main_page = MainPage(browser, link)
    main_page.open(link)
    main_page.open_shop_link()
    with allure.step('Do screenshot'):
        allure.attach(browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)


@allure.description("Check the choice of Italian language on the Hiab page")
@allure.severity(severity_level="MAJOR")
def test_user_can_choose_language(browser):
    link = "https://hiab.com/en"
    main_page = MainPage(browser, link)
    main_page.open(link)
    main_page.can_choose_language()
    with allure.step('Do screenshot'):
        allure.attach(browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)


# # def test_user_can_fill_search_field(browser):
# #     link = "https://hiab.com/en"
# #     main_page = MainPage(browser, link)
# #     main_page.open(link)
# #     main_page.fill_search_field()
# #     with allure.step('Do screenshot'):
# #         allure.attach(browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)


@allure.description("Check items in the footer. Go to page 'About us'. It's opened")
@allure.severity(severity_level="TRIVIAL")
def test_user_can_open_about_us_page(browser):
    link = "https://hiab.com/en"
    main_page = MainPage(browser, link)
    main_page.open(link)
    main_page.about_us_page_is_opened()
    with allure.step('Do screenshot'):
        allure.attach(browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)


# ПРОПУСТИМ ДАННЫЙ ТЕСТ (ИДЕНТИЧЕН С ПРЕДЫДУЩИМ)
# @allure.description("Validation for the main things") # использование Алюра
# @allure.story('Open Finder Accessories page')
# @allure.severity(severity_level="NORMAL")
# def test_user_can_open_sustainability_page(browser):
#     link = "https://hiab.com/en"
#     main_page = MainPage(browser, link)
#     main_page.open(link)
#     main_page.sustainability_page_is_opened()
#     with allure.step('Do screenshot'):
#         allure.attach(browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)


@allure.description("Find a Dealer (Open the map) via the 'Find a Dealer' button from Mega-menu")
@allure.severity(severity_level="MINOR")
def test_user_can_open_careers_page(browser):
    link = "https://hiab.com/en"
    main_page = MainPage(browser, link)
    main_page.open(link)
    main_page.find_a_dealer()
    with allure.step('Do screenshot'):
        allure.attach(browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)


# @allure.description("Validation for the main things") # использование Алюра
# @allure.story('Open Finder Accessories page')
# @allure.severity(severity_level="TRIVIAL")
# def test_user_can_open_media_page(browser):
#     link = "https://hiab.com/en"
#     main_page = MainPage(browser, link)
#     main_page.open(link)
#     main_page.media_page_is_opened()
#     with allure.step('Do screenshot'):
#         allure.attach(browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
#     print('Media page is opened')
#
#
# @allure.description("Validation for the main things") # использование Алюра
# @allure.story('Open Finder Accessories page')
# @allure.severity(severity_level="MINOR")
# def test_user_can_open_club_shop_page(browser):
#     link = "https://hiab.com/en"
#     main_page = MainPage(browser, link)
#     main_page.open(link)
#     main_page.club_shop_page_is_opened()
#     with allure.step('Do screenshot'):
#         allure.attach(browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
#     print('Club shop page is opened')
#
#
# @allure.description("Validation for the main things") # использование Алюра
# @allure.story('Open Finder Accessories page')
# @allure.severity(severity_level="NORMAL")
# def test_user_can_open_hiconnect_page_page(browser):
#     link = "https://hiab.com/en"
#     main_page = MainPage(browser, link)
#     main_page.open(link)
#     main_page.hiconnect_page_is_opened()
#     with allure.step('Do screenshot'):
#         allure.attach(browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
#     print('Hiconnect page is opened')
