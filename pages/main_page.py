import allure
from typing import List
from base.base_page import BasePage
from locators.main_locators import MainLocatorsLocators as Locator
from config.links import Links


class MainPage(BasePage):
    def open_main_page(self) -> None:
        with allure.step('Открыть страницу qa-playground'):
            self.open(Links.HOST)

    def click_tab_dashboard(self) -> None:
        with allure.step('Нажать на вкладку DASHBOARD'):
            self.click_element(Locator.TAB_DASHBOARD)

    def click_tab_contacts(self) -> None:
        with allure.step('Нажать на вкладку CONTACTS'):
            self.click_element(Locator.TAB_CONTACTS)

    # reset_bd
    def click_reset_bd(self) -> None:
        with allure.step('Нажать на значок Очистить базу данных Reset_bd'):
            self.click_element(Locator.BTN_RESET_BD)

    def click_reset_bd_confirm(self) -> None:
        with allure.step('Подтвердить сброс базы данных (нажать кнопку CONFIRM'):
            self.click_element(Locator.BTN_CONFIRM)

    def extract_text_my_latest_notes(self) -> List[str]:
        with allure.step('Получить список заметок из раздела My Latest Notes'):
            return self.extract_names_elements(Locator.NOTES)
