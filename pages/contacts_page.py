from typing import List

import allure

from base.base_page import BasePage
from locators.contacts_locators import ContactsLocators as Locator


class ContactsPage(BasePage):
    def click_btn_new_contact(self) -> None:
        with allure.step('Нажать кнопку NEW CONTACT'):
            self.click_element(Locator.BTN_NEW_CONTACT)

    def extract_full_names_contacts(self) -> List[str]:
        with allure.step('Получить список полных имен из списка контактов менеджера'):
            return self.extract_names_elements(Locator.FULL_NAMES_CONTACTS)

    def click_random_contact(self) -> None:
        with allure.step('Выбрать и нажать рандомный контакт из списка контактов менеджера'):
            self.click_random_element(Locator.CONTACT)
