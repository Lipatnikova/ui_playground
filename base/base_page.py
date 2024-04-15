import allure
from allure_commons.types import AttachmentType
from typing import List
import random

from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as Wait
from config.config import Config


class BasePage:
    def __init__(self, driver):
        """This method initializes the BasePage object"""
        self.driver = driver

    def open(self, url) -> None:
        """This method opens a browser by the provided link"""
        self.driver.get(url)

    def element_is_clickable(
            self, locator: WebElement or tuple[str, str], timeout: int = Config.WAIT_TIMEOUT
    ) -> WebElement:
        """
        This method expects to verify that the element is visible, displayed on the page, and enabled.
        The element is present in the DOM tree.
        Locator - is used to find the element.
        Timeout - the duration it will wait for.
        """
        return Wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def element_is_present(
            self, locator: WebElement or tuple[str, str], timeout: int = Config.WAIT_TIMEOUT
    ) -> WebElement:
        """
        This method expects to verify that the element is present in the DOM tree,
        but not necessarily visible and displayed on the page.
        Locator - is used to find the element.
        Timeout - the duration it will wait for.
        """
        return Wait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def element_is_visible(
            self, locator: WebElement or tuple[str, str], timeout: int = Config.WAIT_TIMEOUT
    ) -> WebElement:
        """
        This method expects to verify that the element is present in the DOM tree, visible, and displayed on the page.
        Visibility means that the element is not only displayed but also has a height and width greater than 0.
        Locator - is used to find the element.
        Timeout - the duration it will wait for.
        """
        self.go_to_element(self.element_is_present(locator))
        return Wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def elements_are_visible(
            self, locator: WebElement or tuple[str, str], timeout: int = Config.WAIT_TIMEOUT) -> List[WebElement]:
        """
        This method expects to verify that the elements are present in the DOM tree, visible and displayed on the page.
        Visibility means that the elements are not only displayed but also have a height and width greater than 0.
        Locator - is used to find the elements.
        Timeout - the duration it will wait for.
        """
        return Wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))

    def go_to_element(self, element: WebElement or tuple[str, str]) -> None:
        """ This method scrolls the page to the selected element, making it visible to the user. """
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def send_keys_in_input(self, locator: WebElement or tuple[str, str], key: str) -> None:
        """ This method sends the key in the field. """
        self.element_is_visible(locator).send_keys(key)

    def fill_in_input(self, locator: WebElement or tuple[str, str], key: str) -> None:
        """This method fills in a specified field with provided value"""
        input_field = self.element_is_visible(locator)
        input_field.click()
        input_field.clear()
        input_field.send_keys(key)

    def click_button(self, locator: WebElement or tuple[str, str]) -> None:
        """
        This method expects to verify that the element is visible,
        displayed on the page, and enabled. The element is present in the DOM tree.
        After clicking the element, the page scrolls to the element.
        """
        self.element_is_clickable(locator).click()

    def click_element(self, locator: WebElement or tuple[str, str]) -> None:
        """This method clicks on the element"""
        self.element_is_visible(locator).click()

    def get_text(self, locator: WebElement or tuple[str, str], timeout: int = Config.WAIT_TIMEOUT):
        """This method gets element text"""
        return self.element_is_visible(locator, timeout).text

    def make_screenshot(self, screenshot_name) -> None:
        """This method makes screenshot and attachments on allure-report"""
        allure.attach(
            body=self.driver.get_screenshot_as_png(),
            name=screenshot_name,
            attachment_type=AttachmentType.PNG
        )

    def extract_names_elements(self, locator: WebElement or tuple[str, str]) -> List[str]:
        """Extracts names of elements found by the given locator"""
        elements = self.elements_are_visible(locator)
        return [element.text for element in elements]

    @staticmethod
    def random_choice(items):
        """This method makes a random choice from elements"""
        return random.choice(items)

    def click_random_element(self, locator: WebElement or tuple[str, str]) -> None:
        """This method makes a random choice from elements and clicks the random element"""
        elements = self.elements_are_visible(locator)
        self.random_choice(elements).click()
