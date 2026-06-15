import pytest

from data import TestDataset
from pages.main_page import MainPage
from pages.order_page import OrderPage
from urls import Urls


class TestOrderCreation:

    @pytest.mark.parametrize(
        "order_button, first_name, last_name, address, metro_station, "
        "phone_number, delivery_date, rental_period, scooter_color, "
        "delivery_comment",
        TestDataset.ORDER_CASES
    )
    def test_user_can_create_order(
            self,
            browser,
            order_button,
            first_name,
            last_name,
            address,
            metro_station,
            phone_number,
            delivery_date,
            rental_period,
            scooter_color,
            delivery_comment
    ):
        home_page = MainPage(browser)
        order_page = OrderPage(browser)

        home_page.open()
        home_page.accept_cookies()

        home_page.scroll_to_element(order_button)
        home_page.click_element(order_button)

        order_page.enter_customer_info(
            first_name,
            last_name,
            address,
            metro_station,
            phone_number
        )

        order_page.enter_rental_details(
            delivery_date,
            rental_period,
            scooter_color,
            delivery_comment
        )

        confirmation_message = (
            order_page.get_order_confirmation_text()
        )

        assert "Заказ оформлен" in confirmation_message


class TestNavigationLogos:

    def test_click_on_scooter_logo_opens_home_page(
            self,
            browser
    ):
        home_page = MainPage(browser)

        home_page.open()
        home_page.accept_cookies()

        home_page.click_top_order_button()
        home_page.click_scooter_logo()

        assert (
            home_page.get_current_url()
            == Urls.BASE_URL
        )

    def test_click_on_yandex_logo_redirects_to_dzen(
            self,
            browser
    ):
        home_page = MainPage(browser)

        home_page.open()
        home_page.accept_cookies()

        home_page.click_yandex_logo()

        home_page.switch_to_last_tab()

        home_page.wait_until_url_contains(
            Urls.DZEN_DOMAIN
        )

        assert (
            Urls.DZEN_DOMAIN
            in home_page.get_current_url()
        )