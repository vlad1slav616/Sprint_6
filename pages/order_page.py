import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from pages.base_page import BasePage


class OrderPage(BasePage):
    FIELD_NAME = (
        By.XPATH,
        ".//input[contains(@placeholder, 'Имя')]"
    )

    FIELD_LAST_NAME = (
        By.XPATH,
        ".//input[contains(@placeholder, 'Фамилия')]"
    )

    FIELD_ADDRESS = (
        By.XPATH,
        ".//input[contains(@placeholder, 'Адрес')]"
    )

    FIELD_METRO = (
        By.XPATH,
        ".//input[contains(@placeholder, 'Станция')]"
    )

    FIELD_PHONE = (
        By.XPATH,
        ".//input[contains(@placeholder, 'Телефон')]"
    )

    NEXT_STEP_BUTTON = (
        By.XPATH,
        './/button[text()="Далее"]'
    )

    FIELD_DELIVERY_DATE = (
        By.XPATH,
        './/input[contains(@placeholder, "Когда")]'
    )

    RENT_PERIOD_DROPDOWN = (
        By.CLASS_NAME,
        "Dropdown-placeholder"
    )

    METRO_STATION_OPTION = (
        By.CLASS_NAME,
        "select-search__row"
    )

    FIELD_COMMENT = (
        By.XPATH,
        './/input[contains(@placeholder, "Комментарий")]'
    )

    BLACK_COLOR_CHECKBOX = (
        By.ID,
        "black"
    )

    GREY_COLOR_CHECKBOX = (
        By.ID,
        "grey"
    )

    SELECTED_PERIOD = (
        By.CSS_SELECTOR,
        ".Dropdown-placeholder.is-selected"
    )

    SUBMIT_ORDER_BUTTON = (
        By.XPATH,
        ".//div[contains(@class, 'Order_Buttons')]//button[text()='Заказать']"
    )

    CONFIRM_ORDER_BUTTON = (
        By.XPATH,
        ".//button[text()='Да']"
    )

    SUCCESS_MODAL_HEADER = (
        By.CLASS_NAME,
        "Order_ModalHeader__3FDaJ"
    )

    RENT_PAGE_HEADER = (
        By.CLASS_NAME,
        "Order_Header__B1w_M"
    )

    def get_period_locator(self, rental_period):
        return (
            By.XPATH,
            f".//div[@class='Dropdown-option' and text()='{rental_period}']"
        )

    def get_color_locator(self, scooter_color):
        return (
            By.ID,
            scooter_color
        )

    @allure.step("Заполнить персональные данные")
    def enter_customer_info(
            self,
            first_name,
            last_name,
            address,
            metro_station,
            phone_number
    ):
        self.type_text(self.FIELD_NAME, first_name)
        self.type_text(self.FIELD_LAST_NAME, last_name)
        self.type_text(self.FIELD_ADDRESS, address)

        self.click_element(self.FIELD_METRO)
        self.type_text(self.FIELD_METRO, metro_station)
        self.click_element(self.METRO_STATION_OPTION)

        self.type_text(self.FIELD_PHONE, phone_number)

        self.click_element(self.NEXT_STEP_BUTTON)

    @allure.step("Заполнить параметры аренды")
    def enter_rental_details(
            self,
            delivery_date,
            rental_period,
            scooter_color,
            delivery_comment
    ):
        date_input = self.get_element(self.FIELD_DELIVERY_DATE)

        date_input.send_keys(delivery_date)
        date_input.send_keys(Keys.ENTER)

        self.click_element(self.RENT_PERIOD_DROPDOWN)
        self.click_element(
            self.get_period_locator(rental_period)
        )

        self.click_element(
            self.get_color_locator(scooter_color)
        )

        self.type_text(
            self.FIELD_COMMENT,
            delivery_comment
        )

        self.click_element(self.SUBMIT_ORDER_BUTTON)
        self.click_element(self.CONFIRM_ORDER_BUTTON)

    @allure.step("Получить текст успешного оформления заказа")
    def get_order_confirmation_text(self):
        return self.get_element_text(
            self.SUCCESS_MODAL_HEADER
        )