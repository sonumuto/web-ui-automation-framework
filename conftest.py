import configparser
import pytest
from splinter import Browser
from utils.browser_factory import BrowserFactory
from pages.basket_page import BasketPage
from pages.favorites_page import FavoritesPage


def pytest_addoption(parser):
    """Adds options to the pytest command line"""
    parser.addoption("--browser-name", action="store",
                     default="firefox", help="Select a browser. Ex: chrome, firefox")
    parser.addoption("--device-view", action="store",
                     default="desktop", help="Select a device view. Ex: desktop, tablet, mobile")
    parser.addoption("--headless", action="store",
                     default="False", help="Run the browser in headless mode.")


@pytest.fixture(scope="session")
def config() -> dict[str, str]:
    """Get config object from config.ini file"""
    config_object = configparser.ConfigParser()
    with open("config.ini", "r", encoding="utf-8") as config_file:
        config_object.read_file(config_file)
    return config_object["DEFAULT"]


@pytest.fixture(scope="function")
def browser(request) -> Browser:
    """Browser fixture"""
    browser_name = request.config.getoption("--browser-name")
    device_view = request.config.getoption("--device-view")
    headless = "true" in request.config.getoption("--headless").lower()

    browser_object = BrowserFactory.get_browser(browser_name=browser_name, device_view=device_view,
                                                headless=headless)

    yield browser_object
    browser_object.quit()


@pytest.fixture(scope="function")
def teardown_product(request, browser) -> None:
    """Remove all products from basket and favorites"""
    yield
    BasketPage(browser).clear_basket()
    FavoritesPage(browser).clear_favorites()
