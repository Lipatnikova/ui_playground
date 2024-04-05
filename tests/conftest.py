import time

import pytest

from pages.main_page import MainPage


@pytest.fixture
def reset_bd(driver):
    def reset_bd():
        main_page = MainPage(driver)
        main_page.click_reset_bd()
        main_page.click_reset_bd_confirm()

    yield reset_bd
