import logging
from pages.base_page import BasePage
from splinter import Browser


class ProductDetailPage(BasePage):
    """Product Detail Page"""

    locators = {
        "product_brand_text": {
            "by": "xpath",
            "value": "//a[contains(@class, 'product-brand-name-with-link')]" },
        "product_price_text": {
            "by": "xpath",
            "value": "//div[contains(@class, 'product-price-container')]" },
        "add_to_basket_button": {
            "by": "xpath",
            "value": "//div[contains(@class, 'add-to-basket-button-text')]" },
        "favorite_button": {
            "by": "xpath",
            "value": "//button[contains(@class, 'fv')]" },
        "unfavorite_button": {
            "by": "xpath",
            "value": "//button[contains(@class, 'fv')]/i[contains(@class, 'i-heart-orange')]" },
        "campaign_close": {
            "by": "xpath",
            "value": "//div[contains(@class, 'campaign-button bold')]" },
    }
    unique_text = "Sepete Ekle"

    def __init__(self, browser: Browser) -> None:
        super().__init__(browser, "")


    def dismiss_campaign(self) -> None:
        """Dismiss the campaign"""
        if self.is_element_present("campaign_close", wait_time=1):
            logging.info("Overlay is visible. Dismissing...")
            self.click("campaign_close")


    def get_product_details(self) -> dict[str, str]:
        """Get product details

        Returns:
            dict[str, str]: Product details
        """
        product_details = {
            "brand": self.find_element("product_brand_text").text,
            "price": int(self.find_element("product_price_text").text.split(" ")[0].replace(".", ""))
        }
        return product_details


    def add_to_basket(self) -> None:
        """Add product to basket"""
        self.click("add_to_basket_button")


    def add_to_favorites(self) -> None:
        """Add product to favorites"""
        self.click("favorite_button")
