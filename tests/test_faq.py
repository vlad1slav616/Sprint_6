import allure
import pytest

from data import TestDataset
from pages.main_page import MainPage


class TestFaqSection:

    @allure.title(
        "Проверка отображения корректного ответа в разделе FAQ"
    )
    @pytest.mark.parametrize(
        "question_index, expected_text",
        TestDataset.FAQ_CASES
    )
    def test_faq_displays_expected_answer(
            self,
            browser,
            question_index,
            expected_text
    ):
        home_page = MainPage(browser)

        home_page.open()
        home_page.accept_cookies()

        home_page.open_faq_question(
            question_index
        )

        faq_answer = (
            home_page.fetch_faq_answer(
                question_index
            )
        )

        assert expected_text in faq_answer