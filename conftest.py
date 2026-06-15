import pytest
from selenium import webdriver


@pytest.fixture
def browser():
    browser_instance = webdriver.Firefox()

    browser_instance.maximize_window()

    yield browser_instance

    browser_instance.quit()