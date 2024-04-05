import allure
import pytest

from base.base_test import BaseTest


class TestCreateContactsPage(BaseTest):
    @pytest.mark.regression_tests
    @allure.testcase('UI-1')
    @allure.title('Добавление нового контакта в список менеджера')
    def test_create_contact_page(self, reset_bd):
        self.main_page.open_main_page()
        self.main_page.click_tab_contacts()
        self.contacts_page.click_btn_new_contact()
        first_name = self.create_contact_page.enter_first_name()
        last_name = self.create_contact_page.enter_last_name()
        title = self.create_contact_page.enter_title()
        email = self.create_contact_page.enter_email()
        manager_name = self.create_contact_page.choose_account_manager()
        expected_contact = [first_name + ' ' + last_name, title, email, manager_name]
        self.create_contact_page.click_btn_save()
        full_name = self.show_contact_page.extract_full_name()
        expected_title = self.show_contact_page.extract_title()
        assert full_name in expected_contact, \
            (f"Show contact page hasn't expected full name: {first_name + ' ' + last_name}."
             f"Actual full name: {full_name}.")
        assert title in expected_contact, \
            (f"Show contact page hasn't expected title: {title}."
             f"Actual title: {expected_title}.")
