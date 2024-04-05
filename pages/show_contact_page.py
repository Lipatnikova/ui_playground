from base.base_page import BasePage
from locators.show_contact_locators import ShowContactLocators as Locator


class ShowContact(BasePage):
    def extract_full_name(self):
        return self.get_text(Locator.FULL_NAME)

    def extract_title(self):
        return self.get_text(Locator.TITLE)[:-3]
