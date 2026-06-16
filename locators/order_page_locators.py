from selenium.webdriver.common.by import By


class OrderPageLocators:
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

    @staticmethod
    def get_period_locator(rental_period):
        return (
            By.XPATH,
            f".//div[@class='Dropdown-option' and text()='{rental_period}']"
        )

    @staticmethod
    def get_color_locator(scooter_color):
        return (
            By.ID,
            scooter_color
        )