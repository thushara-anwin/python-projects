from base.SeleniumBase import SeleniumBase
from .login_locators import *

class LoginPage(SeleniumBase):
    def __init__(self, driver):
        super().__init__(driver=driver)
    def click_sign_in(self):
        self.click_element(sign_in_locator)


    def enter_value_to_email_field(self, search_value):
        self.enter_value(search_value, email_field_locator)

    def enter_value_to_password_field(self, search_value):
        self.enter_value(search_value, password_field_locator)

    def click_sign_in_button(self,):
        self.click_element(sign_in_button_locator)

    def sign_in_success(self):
        el = self.get_element(sign_in_success_locator )
        return el

    def invalid_email_message(self):
        element =self.get_element(invalid_email_password_error_message_locator)
        return element

    def invalid_password_message(self):
        element =self.get_element(invalid_email_password_error_message_locator)
        return element

    def empty_email_field(self):
        element = self.get_element(email_field_required_locator)
        return element

    def empty_password_field(self):
        element = self.get_element(password_field_required_locator)
        return element