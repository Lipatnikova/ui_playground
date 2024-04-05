from base.base_page import BasePage
from locators.contacts_locators import ContactsLocators as Locator


class ContactsPage(BasePage):
    def click_btn_new_contact(self) -> None:
        self.click_element(Locator.BTN_NEW_CONTACT)
