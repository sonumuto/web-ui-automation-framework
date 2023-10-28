import logging
import pytest
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.found_products_list_page import FoundProductListPage
from pages.product_detail_page import ProductDetailPage
from pages.added_to_basket_page import AddedToBasketPage
from pages.favorites_page import FavoritesPage


class TestProductUserAction:
    """Class for Tests of Product Search and User Actions on Products"""


    @pytest.mark.user_actions
    def test_product_search_basket(self, browser, teardown_product, config: dict[str, str]):
        """Test for searching products with filters and adding them to basket"""

        # Product filters
        brand = "Monster"
        min_price = 25000
        max_price = 30000

        LoginPage(browser).login(config["email"], config["password"])

        assert HomePage(browser).unique_text_visible(), "Login is not successful. Home page is not opened."

        logging.info("Searching for 'Oyuncu Bilgisayarı'...")
        HomePage(browser).search_product("Oyuncu Bilgisayarı")

        assert FoundProductListPage(browser).unique_text_visible(), "Search is not successful. Found products page is not opened."

        FoundProductListPage(browser).dismiss_overlay()

        logging.info(f"Filtering by brand: {brand} and price: {min_price} - {max_price}...")
        FoundProductListPage(browser).filter_by_brand(brand)
        FoundProductListPage(browser).filter_by_price(min_price, max_price)

        FoundProductListPage(browser).go_to_first_product()
        assert ProductDetailPage(browser).unique_text_visible(), "Product detail page is not opened."

        ProductDetailPage(browser).dismiss_campaign()

        logging.info("Verifying product details...")
        product_details = ProductDetailPage(browser).get_product_details()
        assert product_details["brand"] == brand, f"Product brand is not {brand}."
        assert product_details["price"] > min_price, f"Product price is under {min_price} TL."
        assert product_details["price"] < max_price, f"Product price is over {max_price} TL."

        logging.info("Adding product to basket...")
        ProductDetailPage(browser).add_to_basket()

        assert AddedToBasketPage(browser).unique_text_visible(), "Product is not added to basket."


    @pytest.mark.user_actions
    def test_product_search_favorite(self, browser, teardown_product, config: dict[str, str]):
        """Test for searching products, favoriting and adding them to basket"""
        LoginPage(browser).login(config["email"], config["password"])

        assert HomePage(browser).unique_text_visible(), "Login is not successful. Home page is not opened."

        logging.info("Searching for 'Gömlek'...")
        HomePage(browser).search_product("Gömlek")

        assert FoundProductListPage(browser).unique_text_visible(), "Search is not successful. Found products page is not opened."

        FoundProductListPage(browser).dismiss_overlay()

        FoundProductListPage(browser).go_to_first_product()
        assert ProductDetailPage(browser).unique_text_visible(), "Product detail page is not opened."

        ProductDetailPage(browser).dismiss_campaign()

        logging.info("Adding product to favorites...")
        ProductDetailPage(browser).add_to_favorites()
        assert ProductDetailPage(browser).is_element_present("unfavorite_button")

        logging.info("Verifying product is added to favorites...")
        FavoritesPage(browser).visit()

        logging.info("Adding favorited product to basket...")
        FavoritesPage(browser).add_favorited_product_to_basket(index=0)
        assert FavoritesPage(browser).is_text_present("Sepete Eklendi"), "Product is not added to basket."
