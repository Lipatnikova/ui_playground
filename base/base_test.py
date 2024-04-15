import pytest

from helpers.file_handler import FileHandler
from pages.main_page import MainPage
from pages.contacts_page import ContactsPage
from pages.create_contact_page import CreateContactPage
from pages.show_contact_page import ShowContact


class BaseTest:
    main_page: MainPage
    contacts_page: ContactsPage
    create_contact_page: CreateContactPage
    show_contact_page: ShowContact
    file_handler: FileHandler

    @pytest.fixture(autouse=True)
    def setup(self, request, driver):
        request.cls.driver = driver
        request.cls.main_page = MainPage(driver)
        request.cls.contacts_page = ContactsPage(driver)
        request.cls.create_contact_page = CreateContactPage(driver)
        request.cls.show_contact_page = ShowContact(driver)
        request.cls.file_handler = FileHandler()
