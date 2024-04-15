import allure

from typing import List
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

    def click_sort_by(self) -> None:
        with allure.step('Нажать кнопку SORT_BY'):
            self.click_element(Locator.SORT_BY)

    def choose_data_sort(self, sort_by) -> None:
        with allure.step('Выбрать тип сортировки контактов'):
            choices = {
                'last_name': Locator.SORT_BY_LAST_NAME,
                'first_name': Locator.SORT_BY_FIRST_NAME,
                'last_seen': Locator.SORT_BY_LAST_SEEN
            }
            self.click_element(choices[sort_by])

    def wait_for_sorting(self) -> None:
        with allure.step('Подождать сортировку списка контактов'):
            self.elements_are_visible(Locator.CONTACT)

    def click_export(self) -> None:
        with allure.step('Нажать кнопку EXPORT'):
            self.click_element(Locator.EXPORT)
