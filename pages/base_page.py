import re
from splinter import Browser
from splinter.element_list import ElementList
from splinter.exceptions import ElementDoesNotExist
from utils.logger import Logger


class BasePage:
    """Base class for all Pages

    Attributes:
        browser (Browser): Browser object.
        url (str): URL of the page.
        locators (dict[str, dict[str, str]]): Locators of the elements on the page.
        unique_text (str): Unique text to check if the page is loaded.
    """

    locators: dict[str, dict[str, str]] = {}
    unique_text: str = ""

    def __init__(self, browser: Browser, url: str) -> None:
        """
        Initialize the BasePage class. This class is inherited by all other Page classes.
        It holds the common properties and methos.

        Args:
            browser (Browser): Browser object
            url (str): URL of the page
        """
        self.url = url
        self.browser: Browser = browser


    def visit(self) -> None:
        """Visit the page URL"""
        self.browser.visit(self.url)
        self.accept_notification_permission()


    @Logger.interaction_logger
    def find_element(self, locator: str, parent_container=None) -> ElementList:
        """Find element by locator

        Args:
            locator (str): Locator of the element.
            parent_container (WebElement, optional): Parent container of the element to chain.
                Defaults to None.

        Returns:
            ElementList: List of found elements.
        """

        by = self.locators.get(locator).get("by")
        value = self.locators.get(locator).get("value")
        # If container is not given, use browser as container
        container = self.browser if parent_container is None else parent_container
        match by:
            case "id":
                return container.find_by_id(value)
            case "name":
                return container.find_by_name(value)
            case "xpath":
                return container.find_by_xpath(value)
            case "css":
                return container.find_by_css(value)
            case "text":
                return container.find_by_text(value)
            case _:
                raise ValueError("Invalid locator")


    @Logger.matcher_logger
    def is_element_present(self, locator: str, parent_container=None, wait_time=30) -> bool:
        """Check if the element is present on the current page

        Args:
            locator (str): Locator of the element
            parent_container (WebElement, optional): Parent container of the element to chain.
                Defaults to None.

        Returns:
            bool: True if element is present, False otherwise
        """
        by = self.locators.get(locator).get("by")
        value = self.locators.get(locator).get("value")
        # If container is not given, use browser as container
        container = self.browser if parent_container is None else parent_container
        match by:
            case "id":
                return container.is_element_present_by_id(value, wait_time=wait_time)
            case "name":
                return container.is_element_present_by_name(value, wait_time=wait_time)
            case "xpath":
                return container.is_element_present_by_xpath(value, wait_time=wait_time)
            case "css":
                return container.is_element_present_by_css(value, wait_time=wait_time)
            case _:
                raise ValueError("Invalid locator")


    @Logger.interaction_logger
    def click(self, locator: str, parent_container=None) -> None:
        """Click element by locator

        Args:
            locator (str): Locator of the element
            parent_container (WebElement, optional): Parent container of the element to chain.
                Defaults to None.
        """
        self.find_element(locator, parent_container=parent_container).click()


    @Logger.interaction_logger
    def send_keys(self, locator: str, value: str, parent_container=None) -> None:
        """Send keys to element by locator

        Args:
            locator (str): Locator of the element
            value (str): Value to send
            parent_container (WebElement, optional): Parent container of the element to chain.
                Defaults to None.
        """
        self.find_element(locator, parent_container=parent_container).type(value)


    @Logger.matcher_logger
    def is_text_present(self, text: str, wait_time: int=15) -> bool:
        """Check if the text is present on the current page

        Args:
            text (str): Text to check
            wait_time (int, optional): Wait time in seconds. Defaults to 15.

        Returns:
            bool: True if text is present, False otherwise
        """
        return self.browser.is_text_present(text, wait_time=wait_time)


    @Logger.matcher_logger
    def is_text_not_present(self, text: str, wait_time: int=15) -> bool:
        """Check if the text is not present on the current page

        Args:
            text (str): Text to check
            wait_time (int, optional): Wait time in seconds. Defaults to 15.

        Returns:
            bool: True if text is not present, False otherwise
        """
        return self.browser.is_text_not_present(text, wait_time=wait_time)


    @Logger.matcher_logger
    def is_visible(self, locator: str) -> bool:
        """Check if the element is visible on the current page

        Args:
            locator (str): Locator of the element

        Returns:
            bool: True if element is visible, False otherwise
        """
        try:
            return self.find_element(locator).is_visible()
        except ElementDoesNotExist:
            return False


    @Logger.matcher_logger
    def is_not_visible(self, locator: str) -> bool:
        """Check if the element is not visible on the current page

        Args:
            locator (str): Locator of the element

        Returns:
            bool: True if element is not visible, False otherwise
        """
        try:
            return self.find_element(locator).is_not_visible()
        except ElementDoesNotExist:
            return True


    def accept_notification_permission(self) -> None:
        """Accept notification permission if it is asked"""
        try:
            self.browser.find_by_id("onetrust-accept-btn-handler").click()
        except ElementDoesNotExist:
            pass


    def unique_text_visible(self) -> bool:
        """Check if the unique text is visible on the current page
        This method is mainly used to check if the page is loaded.

        Returns:
            bool: True if unique text is visible, False otherwise
        """
        return self.is_text_present(self.unique_text, wait_time=30)


    def __str__(self) -> str:
        """String representation of the class

        Returns:
            str: Class name
        """
        words = re.findall(r'[A-Z][a-z]*', self.__class__.__name__)
        return " ".join(words)
