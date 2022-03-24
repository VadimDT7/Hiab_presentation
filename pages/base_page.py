import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

# базовая страница, откоторой будут созданы все остальные
class BasePage:
    def __init__(self, driver, url): # добавляем конструктор
        self.driver = driver
        self.driver.implicitly_wait(5)  # ожидание открытия страницы 5 секунд
        self.url = url

    def open(self, url):
        self.driver.get(url)

    def is_element_present(self, locate_by, selector): # проверка, есть ли такой элемент
        pass

    def is_clickable(self, locator, selector, timeout=10):
        element = WebDriverWait(self.driver, timeout).until(
            ec.element_to_be_clickable((locator, selector)))
        return element

    def switch_to_window(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

    def send_delayed_keys(self, element, text, delay=0.3):
        for c in text:
            endtime = time.time() + delay
            element.send_keys(c)
            time.sleep(endtime - time.time())

    def element_is_present(self):
        try:
            self.driver.find_element_by_css_selector(self)
        except NoSuchElementException:
            return False
        return True

    def is_selected(self, locator, selector, timeout=10):
        element = WebDriverWait(self.driver, timeout).until(
            ec.element_to_be_selected((locator, selector)))
        return element
