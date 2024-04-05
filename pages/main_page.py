import allure

from base.base_page import BasePage
from locators.main_locators import MainLocatorsLocators as Locator
from config.links import Links


class MainPage(BasePage):
    def open_main_page(self) -> None:
        with allure.step("Открыть страницу qa-playground"):
            self.open(Links.HOST)

    def click_tab_contacts(self) -> None:
        self.click_element(Locator.TAB_CONTACTS)

    # reset_bd
    def click_reset_bd(self) -> None:
        self.click_element(Locator.BTN_RESET_BD)

    def click_reset_bd_confirm(self) -> None:
        self.click_element(Locator.BTN_CONFIRM)

    def click_reset_bd_cancel(self) -> None:
        self.click_element(Locator.BTN_CANCEL)
