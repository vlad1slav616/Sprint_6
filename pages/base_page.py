import time
import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from urls import Urls


class BasePage:
    DEFAULT_TIMEOUT = 5

    def __init__(self, browser):
        self.browser = browser
        self.start_url = Urls.BASE_URL

    @allure.step("Открыть стартовую страницу")
    def open(self):
        self.browser.get(self.start_url)

    def get_element(self, locator):
        return WebDriverWait(
            self.browser,
            self.DEFAULT_TIMEOUT
        ).until(
            EC.presence_of_element_located(locator)
        )

    @allure.step("Нажать на элемент")
    def click_element(self, locator):
        web_element = WebDriverWait(
            self.browser,
            self.DEFAULT_TIMEOUT
        ).until(
            EC.element_to_be_clickable(locator)
        )

        time.sleep(0.3)
        web_element.click()

    @allure.step("Ввести значение в поле")
    def type_text(self, locator, value):
        web_element = self.get_element(locator)
        web_element.clear()
        web_element.send_keys(value)

    @allure.step("Получить текст элемента")
    def get_element_text(self, locator):
        return self.get_element(locator).text

    @allure.step("Прокрутить страницу до элемента")
    def scroll_to_element(self, locator):
        web_element = self.get_element(locator)

        self.browser.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            web_element
        )
        self.browser.execute_script("window.scrollBy(0, -150);")

    @allure.step("Переключиться на последнюю вкладку")
    def switch_to_last_tab(self):
        self.browser.switch_to.window(
            self.browser.window_handles[-1]
        )

    @allure.step("Дождаться появления текста в URL: {text}")
    def wait_until_url_contains(self, text):
        return WebDriverWait(
            self.browser,
            self.DEFAULT_TIMEOUT
        ).until(
            EC.url_contains(text)
        )

    @allure.step("Получить текущий URL")
    def get_current_url(self):
        return self.browser.current_url