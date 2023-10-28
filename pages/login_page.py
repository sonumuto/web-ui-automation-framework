from pages.base_page import BasePage
from splinter import Browser


class LoginPage(BasePage):
    """Trendyol Login Page"""

    locators = {
        "e_mail_text_box":{
            "by": "id",
            "value": "login-email" },
        "password_text_box": {
            "by": "id",
            "value": "login-password-input" },
        "login_button": {
            "by": "xpath",
            "value": "//*[@id='login-register']/div[3]/div[1]/form/button/span" },
        "sign_up_tab": {
            "by": "xpath",
            "value": "//*[@id='login-register']/div[2]/div/button[2]" },
    }
    unique_text = "Trendyol’a giriş yap veya hesap oluştur, indirimleri kaçırma!"

    def __init__(self, browser: Browser) -> None:
        super().__init__(browser, "https://www.trendyol.com/giris")


    def login(self, e_mail: str, password: str) -> None:
        """Login with given credentials

        Args:
            e_mail (str): E-mail address
            password (str): Password
        """
        self.visit()

        # Enter login credentials
        self.send_keys("e_mail_text_box", e_mail)
        self.send_keys("password_text_box", password)
        self.click("login_button")
