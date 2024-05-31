import pytest
from modules.ui.login.sign_in_page import LoginPage
from modules.ui.login.login_test_data import *
from utilities.random_email import RandomEmail


@pytest.mark.usefixtures("set_up_and_tear_down")
class TestLogin:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.lp = LoginPage(self.driver)
        self.re = RandomEmail()

    """"
    def test_login_with_valid_credential(self):
        lp = LoginPage(self.driver)
        lp.click_sign_in()
        lp.enter_value_to_email_field(valid_email)
        lp.enter_value_to_password_field(valid_password)
        lp.click_sign_in_button()
        element= lp.sign_in_success()
        assert element.is_displayed()
        #assert element.text.__contains__(sign_in_displayed_message)
    """

    def test_login_with_invalid_email_valid_password(self):
        re = RandomEmail()
        lp = LoginPage(self.driver)
        lp.click_sign_in()
        lp.enter_value_to_email_field(self.re.random_email())
        lp.enter_value_to_password_field(valid_password)
        lp.click_sign_in_button()
        element = lp.invalid_email_message()
        assert element.is_displayed()

    def test_login_with_valid_email_invalid_password(self):
        lp = LoginPage(self.driver)
        lp.click_sign_in()
        lp.enter_value_to_email_field(valid_email)
        lp.enter_value_to_password_field(invalid_password)
        lp.click_sign_in_button()
        # element = sb.get_element(invalid_email_password_error_message_locator)
        element = lp.invalid_email_message()
        assert element.is_displayed()

    def test_login_with_no_credentials(self):
        lp = LoginPage(self.driver)
        lp.click_sign_in()
        lp.enter_value_to_email_field("")
        lp.enter_value_to_password_field("")
        lp.click_sign_in_button()
        element = lp.empty_email_field()
        assert element.text.__contains__(no_credential_expected_warning_message)
        element1 = lp.empty_password_field()
        assert element1.is_displayed()


