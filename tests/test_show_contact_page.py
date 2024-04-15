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

    sort_by = ['last_name', 'first_name', 'last_seen']

    @pytest.mark.regression_tests
    @allure.testcase('UI-5')
    @allure.title('Экспорт списка контактов в файл формата .csv')
    @allure.description('''
    Цель задачи: протестировать функциональность экспорта выбранных контактов в файл CSV, 
    позволяющее передавать определенные наборы контактов в другие системы CRM.''')
    @pytest.mark.parametrize('sort_by', sort_by)
    def test_export_contact_list_to_csv_file(self, sort_by):
        self.main_page.open_main_page()
        self.main_page.click_tab_contacts()
        self.contacts_page.click_sort_by()
        self.contacts_page.choose_data_sort(sort_by)
        self.contacts_page.wait_for_sorting()
        self.contacts_page.click_export()
        self.file_handler.wait_for_file_downloads()
        if sort_by == 'first_name':
            first_names = self.file_handler.extract_first_names_by_csv()
            with allure.step('Проверить, что в выгруженном файле .csv была применена сортировка по first_name'):
                assert first_names == sorted(first_names)
        elif sort_by == 'last_name':
            last_names = self.file_handler.extract_last_names_by_csv()
            with allure.step('Проверить, что в выгруженном файле .csv была применена сортировка по last_name'):
                assert last_names == sorted(last_names)
        elif sort_by == 'last_seen':
            last_seen = self.file_handler.extract_last_seen_by_csv()
            with allure.step('Проверить, что в выгруженном файле .csv была применена сортировка по last_seen'):
                assert last_seen == sorted(last_seen)

        self.file_handler.delete_downloaded_file()
