import logging
import pytest
from pages.home_page import HomePage
from pages.login_page import LoginPage


class TestLogin:
    """Class for Login Tests"""


    @pytest.mark.login
    def test_login(self, browser, config: dict[str, str]):
        """User Login Test"""
        logging.info("Visiting home page...")
        HomePage(browser).visit()

        # Close modal view if it appears
        if HomePage(browser).is_element_present("modal_view_close", wait_time=10):
            logging.info("Closing modal view...")
            HomePage(browser).click("modal_view_close")

        logging.info("Navigating to login page...")
        HomePage(browser).click("user_button")

        assert LoginPage(browser).unique_text_visible(), "Login page is not loaded"

        logging.info("Entering user credentials...")
        LoginPage(browser).send_keys("e_mail_text_box", config["email"])
        LoginPage(browser).send_keys("password_text_box", config["password"])
        LoginPage(browser).click("login_button")

        assert HomePage(browser).unique_text_visible(), "Login is not successful. Home page is not opened."
        assert HomePage(browser).find_element("user_button").text == "Hesabım", "Login is not successful. Login button is still visible."


    @pytest.mark.login
    def test_invalid_login(self, browser):
        """User Login Test with Invalid Credentials"""
        logging.info("Visiting home page...")
        HomePage(browser).visit()

        # Close modal view if it appears
        if HomePage(browser).is_element_present("modal_view_close", wait_time=10):
            logging.info("Closing modal view...")
            HomePage(browser).click("modal_view_close")

        logging.info("Navigating to login page...")
        HomePage(browser).click("user_button")

        assert LoginPage(browser).unique_text_visible(), "Login page is not loaded"

        logging.info("Entering invalid user credentials...")
        LoginPage(browser).send_keys("e_mail_text_box", "invalid@email.com")
        LoginPage(browser).send_keys("password_text_box", "123456789")
        LoginPage(browser).click("login_button")

        assert LoginPage(browser).is_text_present("E-posta adresiniz ve/veya şifreniz hatalı."), "Login is successful with invalid credentials."


    @pytest.mark.login
    def test_empty_email_login(self, browser):
        """User Login Test with Empty E-mail"""
        logging.info("Visiting home page...")
        HomePage(browser).visit()

        # Close modal view if it appears
        if HomePage(browser).is_element_present("modal_view_close", wait_time=10):
            logging.info("Closing modal view...")
            HomePage(browser).click("modal_view_close")

        logging.info("Navigating to login page...")
        HomePage(browser).click("user_button")

        assert LoginPage(browser).unique_text_visible(), "Login page is not loaded"

        LoginPage(browser).click("login_button")

        assert LoginPage(browser).is_text_present("Lütfen geçerli bir e-posta adresi giriniz."), "Empty email error is not displayed."


    @pytest.mark.login
    def test_invalid_email_login(self, browser, config: dict[str, str]):
        """User Login Test with Invalid E-mail"""
        logging.info("Visiting home page...")
        HomePage(browser).visit()

        # Close modal view if it appears
        if HomePage(browser).is_element_present("modal_view_close", wait_time=10):
            logging.info("Closing modal view...")
            HomePage(browser).click("modal_view_close")

        logging.info("Navigating to login page...")
        HomePage(browser).click("user_button")

        assert LoginPage(browser).unique_text_visible(), "Login page is not loaded"

        logging.info("Entering invalid email...")
        LoginPage(browser).send_keys("e_mail_text_box", "invalid_email")
        LoginPage(browser).send_keys("password_text_box", config["password"])
        LoginPage(browser).click("login_button")

        assert LoginPage(browser).is_text_present("Lütfen geçerli bir e-posta adresi giriniz."), "Invalid email error is not displayed."


    @pytest.mark.login
    def test_empty_password_login(self, browser, config: dict[str, str]):
        """User Login Test with Empty Password"""
        logging.info("Visiting home page...")
        HomePage(browser).visit()

        # Close modal view if it appears
        if HomePage(browser).is_element_present("modal_view_close", wait_time=10):
            logging.info("Closing modal view...")
            HomePage(browser).click("modal_view_close")

        logging.info("Navigating to login page...")
        HomePage(browser).click("user_button")

        assert LoginPage(browser).unique_text_visible(), "Login page is not loaded"

        logging.info("Entering email but leaving password empty...")
        LoginPage(browser).send_keys("e_mail_text_box", config["email"])
        LoginPage(browser).click("login_button")

        assert LoginPage(browser).is_text_present("Lütfen şifrenizi giriniz."), "Empty password error is not displayed."
