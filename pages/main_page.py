import allure

from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):

    @allure.step("Принять использование cookies")
    def accept_cookies(self):
        self.click_element(
            MainPageLocators.ACCEPT_COOKIE_BUTTON
        )

    @allure.step("Нажать верхнюю кнопку оформления заказа")
    def click_top_order_button(self):
        self.click_element(
            MainPageLocators.TOP_ORDER_BUTTON
        )

    @allure.step("Нажать нижнюю кнопку оформления заказа")
    def click_bottom_order_button(self):
        self.scroll_to_element(
            MainPageLocators.BOTTOM_ORDER_BUTTON
        )

        self.click_element(
            MainPageLocators.BOTTOM_ORDER_BUTTON
        )

    @allure.step("Открыть вопрос FAQ №{question_number}")
    def open_faq_question(self, question_number):
        question_locator = (
            MainPageLocators.get_question_locator(
                question_number
            )
        )

        self.scroll_to_element(question_locator)
        self.click_element(question_locator)

    @allure.step("Получить ответ FAQ №{question_number}")
    def fetch_faq_answer(self, question_number):
        answer_locator = (
            MainPageLocators.get_answer_locator(
                question_number
            )
        )

        return self.get_element_text(answer_locator)

    @allure.step("Нажать на логотип Самокат")
    def click_scooter_logo(self):
        self.click_element(
            MainPageLocators.SCOOTER_LOGO
        )

    @allure.step("Нажать на логотип Яндекс")
    def click_yandex_logo(self):
        self.click_element(
            MainPageLocators.YANDEX_LOGO
        )