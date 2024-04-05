import allure

from base.base_page import BasePage
from generator.generator import create_contact
from locators.create_contact_locators import CreateContactLocators as Locator


class CreateContactPage(BasePage):

    def enter_first_name(self) -> str:
        with allure.step('Заполнить поле First name валидными данными'):
            info = next(create_contact())
            first_name = info.first_name
            self.fill_in_input(Locator.FIRST_NAME, first_name)
            return first_name

    def enter_last_name(self) -> str:
        with allure.step('Заполнить поле Last name валидными данными'):
            info = next(create_contact())
            last_name = info.last_name
            self.fill_in_input(Locator.LAST_NAME, last_name)
            return last_name

    def enter_title(self) -> str:
        with allure.step('Заполнить поле Title валидными данными'):
            info = next(create_contact())
            title = info.title
            self.fill_in_input(Locator.TITLE, title)
            return title

    def enter_email(self) -> str:
        with allure.step('Заполнить поле Email валидными данными'):
            info = next(create_contact())
            email = info.email
            self.fill_in_input(Locator.EMAIL, email)
            return email

    def choose_account_manager(self) -> str:
        with allure.step('Выбрать аккаунт менеджера из выпадающего списка'):
            name_manager = 'Jane Doe'
            self.click_element(Locator.ACCOUNT_MANAGER)
            self.click_element(Locator.MANAGER_NAME)
            return name_manager

    def click_btn_save(self) -> None:
        with allure.step('Нажать на кнопку SAVE'):
            self.click_element(Locator.BTN_SAVE)
