import allure

from base.base_page import BasePage
from locators.show_contact_locators import ShowContactLocators as Locator


class ShowContact(BasePage):
    def extract_full_name_contact(self):
        with allure.step('Получить полное имя контакта'):
            return self.get_text(Locator.FULL_NAME)

    def extract_title_contact(self):
        with allure.step('Получить title контакта'):
            return self.get_text(Locator.TITLE)[:-3]
