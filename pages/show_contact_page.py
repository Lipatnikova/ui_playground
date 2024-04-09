import allure

from base.base_page import BasePage
from locators.show_contact_locators import ShowContactLocators as Locator
from generator.generator import random_datetime, create_contact


class ShowContact(BasePage):
    def extract_full_name_contact(self) -> str:
        with allure.step('Получить полное имя контакта'):
            return self.get_text(Locator.FULL_NAME)

    def extract_title_contact(self) -> str:
        with allure.step('Получить title контакта'):
            return self.get_text(Locator.TITLE)[:-3]

    def enter_text_to_textarea(self) -> str:
        with allure.step('Ввести текст заметки в поле Add note'):
            info = next(create_contact())
            note = info.note
            textarea = Locator.TEXTAREA
            self.click_element(textarea)
            self.send_keys_in_input(textarea, note)
            return note

    def choose_status(self) -> None:
        with allure.step('Выбрать рандомный статус для заметки'):
            self.click_element(Locator.SELECT_STATUS)
            self.click_random_element(Locator.SELECT_VALUE)

    def choose_data(self) -> None:
        with allure.step('Выбрать рандомную дату для заметки'):
            self.send_keys_in_input(Locator.CALENDAR, random_datetime())

    def click_button_add_this_note(self) -> None:
        with allure.step('Нажать кнопку ADD THIS NOTE'):
            self.click_button(Locator.BTN_ADD_THIS_NOTE)

    def extract_text_last_note(self) -> str:
        with allure.step('Получить у последней заметки'):
            return self.get_text(Locator.LAST_NOTE)
