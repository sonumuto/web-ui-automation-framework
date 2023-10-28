import logging
from pages.base_page import BasePage
from splinter import Browser


class BasketPage(BasePage):
    """Basket Page"""

    locators = {
        "basket_item": {
            "by": "xpath",
            "value": "//div[contains(@class, 'pb-basket-item')]" },
        "trash_button": {
            "by": "xpath",
            "value": "//i[contains(@class, 'i-trash')]" },
        "overlay_close_button": {
            "by": "xpath",
            "value": "//div[contains(@class, 'tooltip-content')]/button" },
    }
    unique_text = "Sepeti Onayla"

    def __init__(self, browser: Browser) -> None:
        super().__init__(browser, "https://www.trendyol.com/sepet")


    def dismiss_overlay(self) -> None:
        """Dismiss the overlay"""
        if self.is_element_present("overlay_close_button", wait_time=5):
            logging.info("Overlay is visible. Dismissing...")
            self.click("overlay_close_button")


    def clear_basket(self) -> None:
        """Clear the basket"""
        self.visit()
        self.dismiss_overlay()
        if not self.is_element_present("basket_item", wait_time=5):
            return
        basket_products = self.find_element("basket_item").first
        self.click("trash_button", parent_container=basket_products)
        self.clear_basket()
