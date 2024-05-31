from base.SeleniumBase import SeleniumBase
from .dummy_booking_page_locator import *
from .dummy_booking_test_data import *
import logging

log = logging.getLogger('testLogger')


class DummyBookingPage(SeleniumBase):
    def __init__(self, driver):
        super().__init__(driver=driver)

    def navigate_to_dummy_booking_website(self):
        log.debug(f"Navigating to URL : {dummy_web_site_url}")
        self.driver.get(dummy_web_site_url)

    def enter_value_billing_name_field(self, billing_name):
        self.enter_value(billing_name, billing_name_field_locator)
        log.critical(f"enter billing name : {billing_name}")

    def enter_value_billing_phone(self, phone):
        self.enter_value(phone, billing_phone_field_locator)
        log.error(f"enter billing phone number : {phone}")

    def enter_value_billing_email(self, email):
        self.enter_value(email, billing_email_field_locator)
        log.warning(f"enter billing email : {email}")

    def select_country_name(self, country_name):
        self.select_dropdown_value(country_name, country_dropdown_locator)
        log.info(f"select country name : {country_name}")
