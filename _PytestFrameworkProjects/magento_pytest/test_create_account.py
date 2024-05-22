import random
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@pytest.fixture()
def set_up_and_tear_down():
    global driver
    driver=webdriver.Chrome()
    driver.get("https://magento.softwaretestingboard.com/")
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield
    driver.close()


def test_create_account_with_required_fields(set_up_and_tear_down):
    driver.find_element(By.XPATH,"//a[@href='https://magento.softwaretestingboard.com/customer/account/create/']").click()
    driver.find_element(By.CSS_SELECTOR,"input#firstname").send_keys("Alaaya")
    driver.find_element(By.CSS_SELECTOR,"input#lastname").send_keys("Latta")
    driver.find_element(By.CSS_SELECTOR,"input#email_address").send_keys(random_email())
    driver.find_element(By.CSS_SELECTOR,"input#password").send_keys("south_middle_123")
    driver.find_element(By.CSS_SELECTOR,"input#password-confirmation").send_keys("south_middle_123")
    driver.find_element(By.CSS_SELECTOR, "button.action.submit.primary").click()
    assert driver.find_element(By.CSS_SELECTOR, "div[data-ui-id='message-success']").is_displayed()
 

def test_create_account_with_duplicate_email(set_up_and_tear_down):
    driver.find_element(By.XPATH,"//a[@href='https://magento.softwaretestingboard.com/customer/account/create/']").click()
    driver.find_element(By.CSS_SELECTOR,"input#firstname").send_keys("Alaya")
    driver.find_element(By.CSS_SELECTOR,"input#lastname").send_keys("Latta")
    driver.find_element(By.CSS_SELECTOR,"input#email_address").send_keys("thushara@gmail.com")
    driver.find_element(By.CSS_SELECTOR,"input#password").send_keys("south_middle_123")
    driver.find_element(By.CSS_SELECTOR,"input#password-confirmation").send_keys("south_middle_123")
    driver.find_element(By.CSS_SELECTOR, "button.action.submit.primary").click()
    assert driver.find_element(By.CSS_SELECTOR, "div[data-ui-id='message-error']").is_displayed()


def test_create_account_with_different_confirmation_password(set_up_and_tear_down):
    driver.find_element(By.XPATH,"//a[@href='https://magento.softwaretestingboard.com/customer/account/create/']").click()
    driver.find_element(By.CSS_SELECTOR,"input#firstname").send_keys("Alaya")
    driver.find_element(By.CSS_SELECTOR,"input#lastname").send_keys("Latta")
    driver.find_element(By.CSS_SELECTOR,"input#email_address").send_keys("lattaalaya@gmail.com")
    driver.find_element(By.CSS_SELECTOR,"input#password").send_keys("south_middle_123")
    driver.find_element(By.CSS_SELECTOR,"input#password-confirmation").send_keys("south_middle")
    driver.find_element(By.CSS_SELECTOR, "button.action.submit.primary").click()
    #expected_warning_message="password-confirmation-error"
    assert driver.find_element(By.CSS_SELECTOR, "div#password-confirmation-error").is_displayed()


def test_create_account_without_required_fields(set_up_and_tear_down):
    driver.find_element(By.XPATH,"//a[@href='https://magento.softwaretestingboard.com/customer/account/create/']").click()
    driver.find_element(By.CSS_SELECTOR,"input#firstname").send_keys("")
    driver.find_element(By.CSS_SELECTOR,"input#lastname").send_keys("")
    driver.find_element(By.CSS_SELECTOR,"input#email_address").send_keys("")
    driver.find_element(By.CSS_SELECTOR,"input#password").send_keys("")
    driver.find_element(By.CSS_SELECTOR,"input#password-confirmation").send_keys("")
    driver.find_element(By.CSS_SELECTOR, "button.action.submit.primary").click()
    assert driver.find_element(By.CSS_SELECTOR, "div#firstname-error").is_displayed()
    assert driver.find_element(By.CSS_SELECTOR, "div#lastname-error").is_displayed()
    assert driver.find_element(By.CSS_SELECTOR, "input#email_address+div").is_displayed()
    assert driver.find_element(By.CSS_SELECTOR, "div#password-error").is_displayed()
    assert driver.find_element(By.CSS_SELECTOR, "input#password-confirmation+div").is_displayed()


def random_email():
    num = random.randint(10,90)
    num =str(num)
    return 'alayalatta'+ num +'@gmail.com'

