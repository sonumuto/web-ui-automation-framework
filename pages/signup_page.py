from pages.base_page import BasePage
from splinter import Browser


class SignUpPage(BasePage):
    """Trendyol Sign Up Page"""

    locators = {
        "e_mail_text_box":{
            "by": "id",
            "value": "register-email" },
        "password_text_box": {
            "by": "id",
            "value": "register-password-input" },
        "gender_women_button": {
            "by": "xpath",
            "value": "//*[@id='login-register']/div[2]/div/button[2]" },
        "gender_men_button": {
            "by": "xpath",
            "value": "//*[@id='login-register']/div[2]/div/button[2]" },
        "first_checkbox": {
            "by": "xpath",
            "value": "//*[@id='login-register']/div[3]/div[1]/form/div[4]/div/div[1]/div/div" },
        "second_checkbox": {
            "by": "xpath",
            "value": "//*[@id='login-register']/div[3]/div[1]/form/div[5]/div/div[1]/div/div" },
        "sign_up_button": {
            "by": "xpath",
            "value": "//*[@id='login-register']/div[3]/div[1]/form/button" },
    }
    unique_text = "Üye olmadan verilen siparişlerin takibi için"

    def __init__(self, browser: Browser) -> None:
        super().__init__(browser, "https://www.trendyol.com/giris")
