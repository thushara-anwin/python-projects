from base.SeleniumBase import SeleniumBase
from .create_account_locators import *

class CreateAccount(SeleniumBase):
    def __init__(self, driver):
        super().__init__(driver=driver)

    def click_create_account(self):
        self.click_element(create_account_locator)


    def enter_value_to_first_name_field(self, first_name):
        self.enter_value(first_name,first_name_locator)

    def enter_value_to_last_name_field(self, last_name):
        self.enter_value(last_name, last_name_locator)

    def enter_value_to_email_field(self, email):
        self.enter_value(email, email_locator)

    def enter_value_to_password_field(self, password):
        self.enter_value(password, password_locator)

    def enter_value_to_confirm_password_field(self, confirm_password):
        self.enter_value(confirm_password, confirmation_password_locator)

    def click_create_account_button(self):
        self.click_element(create_account_submit_button_locator)

    def message_displayed(self):
        el = self.get_element(success_message_locator)
        return el

    def duplicate_email(self):
        el=self.get_element(error_message_duplicate_email_locator)
        return el


    def confirm_password_error(self):
        el = self.get_element(error_confirm_password_locator)
        return el

    def firstname_error(self):
        el = self.get_element(firstname_error_locator)
        return el

    def lastname_error(self):
        el = self.get_element(lastname_error_locator)
        return el

    def email_error(self):
        el =self.get_element(email_error_locator)
        return el

    def password_error(self):
        el = self.get_element(password_error_locator)
        return el

    def confirm_pswd_error(self):
         el = self.get_element(confirm_password_error_locator)
         return el



