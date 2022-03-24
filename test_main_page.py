from pages.main_page import MainPage


def test_user_can_open_finder_accessories(browser):  # browser =
    # webdriver.Chrome() #убрали его отсюда, т.к. поместили в conftest.py
    link = "https://hiab.com/en"
    main_page = MainPage(browser, link)
    main_page.open(link)
    main_page.open_finder_accessories()
    print('Can open Finder Accessories')


def test_user_can_open_shop(browser):
    link = "https://hiab.com/en"
    main_page = MainPage(browser, link)
    main_page.open(link)
    main_page.open_shop_link()
    print('Can open Hiab Webshop')


def test_user_can_choose_language(browser):
    link = "https://hiab.com/en"
    main_page = MainPage(browser, link)
    main_page.open(link)
    main_page.can_choose_language()
    print('Site with DE language is opened')  # Hiab webshop is opened


def test_user_can_fill_search_field(browser):
    link = "https://hiab.com/en"
    main_page = MainPage(browser, link)
    main_page.open(link)
    main_page.fill_search_field()


def test_user_can_open_about_us_page(browser):
    link = "https://hiab.com/en"
    main_page = MainPage(browser, link)
    main_page.open(link)
    main_page.about_us_page_is_opened()
    print('About Us page is opened')


def test_user_can_open_sustainability_page(browser):
    link = "https://hiab.com/en"
    main_page = MainPage(browser, link)
    main_page.open(link)
    main_page.sustainability_page_is_opened()
    print('Sustainability page is opened')


def test_user_can_open_careers_page(browser):
    link = "https://hiab.com/en"
    main_page = MainPage(browser, link)
    main_page.open(link)
    main_page.careers_page_is_opened()
    print('Careers page is opened')


def test_user_can_open_media_page(browser):
    link = "https://hiab.com/en"
    main_page = MainPage(browser, link)
    main_page.open(link)
    main_page.media_page_is_opened()
    print('Media page is opened')


def test_user_can_open_club_shop_page(browser):
    link = "https://hiab.com/en"
    main_page = MainPage(browser, link)
    main_page.open(link)
    main_page.club_shop_page_is_opened()
    print('Club shop page is opened')


def test_user_can_open_hiconnect_page_page(browser):
    link = "https://hiab.com/en"
    main_page = MainPage(browser, link)
    main_page.open(link)
    main_page.hiconnect_page_is_opened()
    print('Hiconnect page is opened')
