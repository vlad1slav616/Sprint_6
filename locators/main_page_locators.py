from selenium.webdriver.common.by import By


class MainPageLocators:
    YANDEX_LOGO = (
        By.CLASS_NAME,
        'Header_LogoYandex__3TSOI'
    )

    SCOOTER_LOGO = (
        By.CLASS_NAME,
        'Header_LogoScooter__3lsAR'
    )

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

    @staticmethod
    def get_question_locator(question_number):
        return (
            By.ID,
            f"accordion__heading-{question_number}"
        )

    @staticmethod
    def get_answer_locator(question_number):
        return (
            By.ID,
            f"accordion__panel-{question_number}"
        )