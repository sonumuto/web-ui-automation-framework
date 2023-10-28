from pages.base_page import BasePage
from splinter import Browser


class AddedToBasketPage(BasePage):
    """Added to Basket Page"""

    locators = {
        "go_to_basket_button": {
            "by": "xpath",
            "value": "//*[@id='product-detail-app']/div/div[3]/div/div/div[2]/div/div[1]/div[2]/div/div/div[1]/h1/a" },
    }
    unique_text = "Ürün Sepete Eklendi!"

    def __init__(self, browser: Browser) -> None:
        super().__init__(browser, "")
