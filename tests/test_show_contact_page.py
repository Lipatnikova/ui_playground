import allure
import pytest

from base.base_test import BaseTest


class TestShowContact(BaseTest):

    @pytest.mark.regression_tests
    @pytest.mark.xfail
    @allure.testcase('UI-2')
    @allure.title('Добавление заметки к контакту из списка контактов менеджера')
    @allure.description('''
    Цель задачи: протестировать функциональность добавления заметок клиентам в CRM системе. 
    Эта функция должна позволять менеджерам по продажам удобно хранить информацию 
    о своих взаимодействиях с клиентами.''')
    def test_add_note_to_contact(self):
        self.main_page.open_main_page()
        self.main_page.click_tab_contacts()
        self.contacts_page.click_random_contact()
        expected_text = self.show_contact_page.enter_text_to_textarea()
        self.show_contact_page.choose_status()
        self.show_contact_page.choose_data()
        self.show_contact_page.click_button_add_this_note()
        text_last_note = self.show_contact_page.extract_text_last_note()
        with allure.step('Проверить, что введеная заментка отображается первой в списке заметок контакта'):
            assert expected_text == text_last_note, \
                (f'Note with {expected_text} was not added.'
                 f'Actual text by the last note in list: {text_last_note}')

        with allure.step('Нажать вкладку "Dashboard" и проверить, что только что '
                         'добавленная заметка отображается в разделе "My Latest Notes"'):
            self.main_page.click_tab_dashboard()
            text_last_notes = self.main_page.extract_text_my_latest_notes()
            assert expected_text in text_last_notes, \
                (f'Note with {expected_text} was not added to main page.'
                 f'Actual text by My Latest Notes list: {text_last_notes}')
