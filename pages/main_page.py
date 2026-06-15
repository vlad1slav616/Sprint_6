import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class MainPage(BasePage):
    YANDEX_LOGO = (By.CLASS_NAME, 'Header_LogoYandex__3TSOI')
    SCOOTER_LOGO = (By.CLASS_NAME, 'Header_LogoScooter__3lsAR')

    TOP_ORDER_BUTTON = (
        By.XPATH,
        './/button[text()="Заказать"]'
    )

    BOTTOM_ORDER_BUTTON = (
        By.XPATH,
        ".//div[contains(@class, 'Home_ThirdPart')]//button[text()='Заказать']"
    )

    ACCEPT_COOKIE_BUTTON = (
        By.ID,
        'rcc-confirm-button'
    )

    def get_question_locator(self, question_number):
        return (
            By.ID,
            f"accordion__heading-{question_number}"
        )

    def get_answer_locator(self, question_number):
        return (
            By.ID,
            f"accordion__panel-{question_number}"
        )

    @allure.step("Принять использование cookies")
    def accept_cookies(self):
        self.click_element(self.ACCEPT_COOKIE_BUTTON)

    @allure.step("Нажать верхнюю кнопку оформления заказа")
    def click_top_order_button(self):
        self.click_element(self.TOP_ORDER_BUTTON)

    @allure.step("Нажать нижнюю кнопку оформления заказа")
    def click_bottom_order_button(self):
        self.scroll_to_element(self.BOTTOM_ORDER_BUTTON)
        self.click_element(self.BOTTOM_ORDER_BUTTON)

    @allure.step("Открыть вопрос FAQ №{question_number}")
    def open_faq_question(self, question_number):
        question_locator = self.get_question_locator(question_number)

        self.scroll_to_element(question_locator)
        self.click_element(question_locator)

    @allure.step("Получить ответ FAQ №{question_number}")
    def fetch_faq_answer(self, question_number):
        answer_locator = self.get_answer_locator(question_number)

        return self.get_element_text(answer_locator)

    @allure.step("Нажать на логотип Самокат")
    def click_scooter_logo(self):
        self.click_element(self.SCOOTER_LOGO)

    @allure.step("Нажать на логотип Яндекс")
    def click_yandex_logo(self):
        self.click_element(self.YANDEX_LOGO)