import allure
import pytest

from base.base_test import BaseTest


class TestCreateContactsPage(BaseTest):
    @pytest.mark.regression_tests
    @allure.testcase('UI-1')
    @allure.title('Добавление нового контакта в список менеджера')
    @allure.description('''
    Цель задачи: протестировать функциональность добавления новых контактов в систему CRM. 
    Эта функция должна позволять менеджерам по продажам добавлять новых клиентов в список 
    контактов для дальнейшего взаимодействия с ними.''')
    def test_create_contact_page(self, reset_bd):
        self.main_page.open_main_page()
        self.main_page.click_tab_contacts()
        self.contacts_page.click_btn_new_contact()
        first_name = self.create_contact_page.enter_first_name()
        last_name = self.create_contact_page.enter_last_name()
        title = self.create_contact_page.enter_title()
        email = self.create_contact_page.enter_email()
        manager_name = self.create_contact_page.choose_account_manager()
        expected_full_name = f'{first_name} {last_name}'
        expected_contact = [expected_full_name, title, email, manager_name]
        self.create_contact_page.click_btn_save()
        full_name = self.show_contact_page.extract_full_name_contact()
        expected_title = self.show_contact_page.extract_title_contact()
        with allure.step('Проверить, что полное имя созданного контакта соответствует '
                         'данным введенным при создании контакта'):
            assert full_name in expected_contact, \
                (f"Show contact page hasn't expected full name: {expected_full_name}."
                 f"Actual full name: {full_name}.")
        with allure.step('Проверить, что title созданного контакта соответствует '
                         'данным введенным при создании контакта'):
            assert title in expected_contact, \
                (f"Show contact page hasn't expected title: {title}."
                 f"Actual title: {expected_title}.")
        with allure.step('Проверить, что добавленный контакт отображается в списке контактов'):
            self.main_page.click_tab_contacts()
            list_contacts = self.contacts_page.extract_full_names_contacts()
            assert expected_full_name in list_contacts, \
                f'The created user: {expected_full_name} is missing from the contacts list: {list_contacts}.'
