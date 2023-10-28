import logging
import pytest
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.signup_page import SignUpPage


class TestSignUp:
    """Class for Sign Up Tests
    Note: Sign Up test is not added to the test suite as captcha is not handled."""


    @pytest.mark.signup
    def test_sign_up_elements(self, browser):
        """Sign Up Page Elements Verification Test"""

        logging.info("Visiting home page...")
        HomePage(browser).visit()

        # Close modal view if it appears
        if HomePage(browser).is_element_present("modal_view_close", wait_time=10):
            logging.info("Closing modal view...")
            HomePage(browser).click("modal_view_close")

        logging.info("Navigating to login page...")
        HomePage(browser).click("user_button")

        assert LoginPage(browser).unique_text_visible(), "Login page is not loaded"

        logging.info("Navigating to sign up page...")
        LoginPage(browser).click("sign_up_tab")

        assert SignUpPage(browser).unique_text_visible(), "Sign Up page is not loaded"

        logging.info("Verifying sign up page elements...")
        assert SignUpPage(browser).is_visible("e_mail_text_box"), "E-mail text box is not visible"
        assert SignUpPage(browser).is_visible("password_text_box"), "Password text box is not visible"

        assert SignUpPage(browser).is_visible("gender_women_button"), "Women button is not visible"
        assert SignUpPage(browser).is_visible("gender_men_button"), "Men button is not visible"

        assert SignUpPage(browser).is_visible("first_checkbox"), "First checkbox is not visible"
        assert SignUpPage(browser).is_visible("second_checkbox"), "Second checkbox is not visible"

        assert SignUpPage(browser).find_element("sign_up_button").text == "ÜYE OL", "Sign Up button is not visible"
