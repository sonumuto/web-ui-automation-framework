from pages.base_page import BasePage
from splinter import Browser


class HomePage(BasePage):
    """Trendyol Home Page"""

    locators = {
        "modal_view_close": {
            "by": "xpath",
            "value": "div[contains(@class, 'modal-close')]" },
        "user_button": {
            "by": "xpath",
            "value": "//*[@id='account-navigation-container']/div/div[@class='account-nav-item user-login-container']" },
        "search_text_box": {
            "by": "xpath",
            "value": "//*[@id='sfx-discovery-search-suggestions']/div/div[1]/input" },
        "search_button": {
            "by": "xpath",
            "value": "//*[@id='sfx-discovery-search-suggestions']/div/div/i" },
    }
    unique_text = "Sana Özel"

    def __init__(self, browser: Browser) -> None:
        super().__init__(browser, "https://www.trendyol.com")


    def search_product(self, product: str) -> None:
        """Search the given product

        Args:
            product (str): Product name
        """
        self.send_keys("search_text_box", product)
        self.click("search_button")
