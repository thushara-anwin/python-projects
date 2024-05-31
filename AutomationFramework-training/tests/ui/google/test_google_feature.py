import pytest

from modules.ui.google.google_page_class import GooglePage
from modules.ui.google.google_test_data import *


@pytest.mark.usefixtures("get_driver")
class TestGoogleSeach:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.gp = GooglePage(self.driver)
        self.gp.open_google_website(google_url)

    def test_search_on_google(self):
        self.gp.enter_value_to_search_field(search_value)
        self.gp.click_search_button()



