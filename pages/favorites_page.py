from pages.base_page import BasePage
from splinter import Browser


class FavoritesPage(BasePage):
    """Favorites Page"""

    locators = {
        "favorited_product_container": {
            "by": "xpath",
            "value": "//div[contains(@class, 'favored-product-container')]" },
        "favorited_product": {
            "by": "xpath",
            "value": "//div[contains(@class, 'p-card-wrppr')]" },
        "unfavorite_button": {
            "by": "xpath",
            "value": "//div[contains(@class, 'ufvrt-btn-wrppr')]" },
        "add_to_basket_button": {
            "by": "xpath",
            "value": "//div[contains(@class, 'basket-button')]" },
    }
    unique_text = "Tüm Favoriler"

    def __init__(self, browser: Browser) -> None:
        super().__init__(browser, "https://www.trendyol.com/Hesabim/Favoriler")


    def get_favorited_products_count(self) -> int:
        """Get the count of favorited products

        Returns:
            int: Count of favorited products
        """
        favorited_container = self.find_element("favorited_product_container")
        return len(self.find_element("favorited_product", parent_container=favorited_container))


    def add_favorited_product_to_basket(self, index: int) -> None:
        """Add favorited product to basket

        Args:
            index (int): Index of the product to add to basket
        """
        favorited_container = self.find_element("favorited_product_container")
        first_product = self.find_element("favorited_product", parent_container=favorited_container)[index]
        self.click("add_to_basket_button", parent_container=first_product)


    def clear_favorites(self) -> None:
        """Clear all favorited products"""
        self.visit()
        if not self.is_element_present("favorited_product_container", wait_time=5):
            return
        favorited_container = self.find_element("favorited_product_container")
        favorited_products = self.find_element("favorited_product", parent_container=favorited_container)
        for product in favorited_products:
            self.click("unfavorite_button", parent_container=product)
