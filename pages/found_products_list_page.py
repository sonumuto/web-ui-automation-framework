from pages.base_page import BasePage
from splinter import Browser
import logging


class FoundProductListPage(BasePage):
    """Search Found Products Page"""

    locators = {
        "filter_list": {
            "by": "xpath",
            "value": "//*[@id='sticky-aggregations']/div" },
        "brand_dropdown": {
            "by": "xpath",
            "value": "//*[@id='sticky-aggregations']/div/div[2]/div[1]" },
        "brand_list": {
            "by": "xpath",
            "value": "//*[@id='sticky-aggregations']/div/div[2]/div[3]/div/div" },
        "price_dropdown": {
            "by": "text",
            "value": "Fiyat" },
        "price_min": {
            "by": "xpath",
            "value": "//input[@placeholder='En Az']" },
        "price_max": {
            "by": "xpath",
            "value": "//input[@placeholder='En Çok']"},
        "price_apply": {
            "by": "xpath",
            "value": "//button[contains(@class, 'fltr-srch-prc-rng-src')]" },
        "first_product": {
            "by": "xpath",
            "value": "//div[contains(@class, 'prdct-cntnr-wrppr')]/div[contains(@class, 'p-card-wrppr with-campaign-view')][1]" },
        "overlay_close": {
            "by": "xpath",
            "value": "//div[contains(@class, 'popup-heading')]" },
    }
    unique_text = "sonuç listeleniyor"

    def __init__(self, browser: Browser) -> None:
        super().__init__(browser, "")


    def dismiss_overlay(self) -> None:
        """Dismiss the overlay"""
        if self.is_element_present("overlay_close", wait_time=1):
            logging.info("Overlay is visible. Dismissing...")
            self.click("overlay_close")


    def filter_by_brand(self, brand: str) -> None:
        """Filter the found products by brand

        Args:
            brand (str): Brand name
        """
        # If brand list is not visible, click the brand dropdown to extend the list
        if self.is_not_visible("brand_list"):
            self.click("brand_dropdown")

        brand_list = self.find_element("brand_list")
        brand_list.find_by_text(brand).first.click()


    def filter_by_price(self, min_price: str, max_price: str) -> None:
        """Filter the found products by price

        Args:
            min_price (str): Minimum price
            max_price (str): Maximum price
        """
        # If price dropdown is not visible, click the price dropdown to extend the list
        if self.is_not_visible("price_min"):
            filter_list = self.find_element("filter_list")
            self.click("price_dropdown", parent_container=filter_list)

        self.send_keys("price_min", min_price)
        self.send_keys("price_max", max_price)
        self.click("price_apply")


    def go_to_first_product(self) -> None:
        """Go to the first product in the list"""
        self.click("first_product")

        # Close the old tab
        self.browser.windows[0].close()
