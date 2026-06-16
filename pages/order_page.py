import allure
from selenium.webdriver.common.keys import Keys

from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators


class OrderPage(BasePage):

    @allure.step("Заполнить персональные данные")
    def enter_customer_info(
            self,
            first_name,
            last_name,
            address,
            metro_station,
            phone_number
    ):
        self.type_text(
            OrderPageLocators.FIELD_NAME,
            first_name
        )

        self.type_text(
            OrderPageLocators.FIELD_LAST_NAME,
            last_name
        )

        self.type_text(
            OrderPageLocators.FIELD_ADDRESS,
            address
        )

        self.click_element(
            OrderPageLocators.FIELD_METRO
        )

        self.type_text(
            OrderPageLocators.FIELD_METRO,
            metro_station
        )

        self.click_element(
            OrderPageLocators.METRO_STATION_OPTION
        )

        self.type_text(
            OrderPageLocators.FIELD_PHONE,
            phone_number
        )

        self.click_element(
            OrderPageLocators.NEXT_STEP_BUTTON
        )

    @allure.step("Заполнить параметры аренды")
    def enter_rental_details(
            self,
            delivery_date,
            rental_period,
            scooter_color,
            delivery_comment
    ):
        date_input = self.get_element(
            OrderPageLocators.FIELD_DELIVERY_DATE
        )

        date_input.send_keys(delivery_date)
        date_input.send_keys(Keys.ENTER)

        self.click_element(
            OrderPageLocators.RENT_PERIOD_DROPDOWN
        )

        self.click_element(
            OrderPageLocators.get_period_locator(
                rental_period
            )
        )

        self.click_element(
            OrderPageLocators.get_color_locator(
                scooter_color
            )
        )

        self.type_text(
            OrderPageLocators.FIELD_COMMENT,
            delivery_comment
        )

        self.click_element(
            OrderPageLocators.SUBMIT_ORDER_BUTTON
        )

        self.click_element(
            OrderPageLocators.CONFIRM_ORDER_BUTTON
        )

    @allure.step("Получить текст успешного оформления заказа")
    def get_order_confirmation_text(self):
        return self.get_element_text(
            OrderPageLocators.SUCCESS_MODAL_HEADER
        )