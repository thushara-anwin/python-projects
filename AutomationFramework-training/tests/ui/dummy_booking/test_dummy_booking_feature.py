import pytest

from modules.ui.dummy_booking.dummy_booking_page_class import DummyBookingPage
from modules.ui.dummy_booking.dummy_booking_test_data import *


@pytest.mark.usefixtures("get_driver")
class TestDummyBooking:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.db = DummyBookingPage(self.driver)

    def test_dummy_booking_website(self):
        self.db.navigate_to_dummy_booking_website()
        self.db.enter_value_billing_name_field(billing_details['Name'])
        self.db.enter_value_billing_phone(billing_details['Phone'])
        self.db.enter_value_billing_email(billing_details['email'])
        self.db.select_country_name(billing_details['country'])



