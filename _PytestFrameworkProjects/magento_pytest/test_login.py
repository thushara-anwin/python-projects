import random
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture()
def set_up_and_tear_down():
    global driver
    driver=webdriver.Chrome()
    driver.get("https://magento.softwaretestingboard.com/")
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield
    driver.close()


def test_login_with_valid_credential(set_up_and_tear_down):
    driver.find_element(By.XPATH,
                        "//ul[@class='header links']"
                        "//following::li[@data-label='or']/a[contains(text(),'Sign In')][1]").click()
    driver.find_element(By.CSS_SELECTOR, "input#email").send_keys('thushara@gmail.com')
    driver.find_element(By.CSS_SELECTOR, "input[name='login[password]']").send_keys('south_middle_123')
    driver.find_element(By.XPATH,"//div[@class='primary']"
                                 "/button[@id='send2' and @type ='submit' and @name ='send']/span").click()
    displayed_message = 'Welcome'
    assert driver.find_element(By.XPATH,"//span[contains(text(),'Welcome')]").text.__contains__(displayed_message)


def test_login_with_invalid_email_valid_password(set_up_and_tear_down):
    driver.find_element(By.CSS_SELECTOR,"li.authorization-link>a").click()
    driver.find_element(By.CSS_SELECTOR, "input#email").send_keys(random_email())
    driver.find_element(By.CSS_SELECTOR, "input[name='login[password]']").send_keys('south_middle_123')
    driver.find_element(By.CSS_SELECTOR,"div+div>div.primary>button#send2").click()
    assert driver.find_element(By.CSS_SELECTOR,"div[data-ui-id='message-error']").is_displayed()


def test_login_with_valid_email_invalid_password(set_up_and_tear_down):
    driver.find_element(By.CSS_SELECTOR,"li.authorization-link>a").click()
    driver.find_element(By.CSS_SELECTOR, "input#email").send_keys('thushara@gmail.com')
    driver.find_element(By.CSS_SELECTOR, "input[name='login[password]']").send_keys('123')
    driver.find_element(By.CSS_SELECTOR,"div+div>div.primary>button#send2").click()
    assert driver.find_element(By.CSS_SELECTOR,"div[data-ui-id='message-error']").is_displayed()


def test_login_with_no_credentials(set_up_and_tear_down):
    driver.find_element(By.CSS_SELECTOR,"li.authorization-link>a").click()
    driver.find_element(By.CSS_SELECTOR, "input#email").send_keys('')
    driver.find_element(By.CSS_SELECTOR, "input[name='login[password]']").send_keys('')
    expected_warning_message='This is a required field.'
    driver.find_element(By.CSS_SELECTOR,"div+div>div.primary>button#send2").click()
    assert driver.find_element(By.CSS_SELECTOR,"div#email-error").text.__contains__(expected_warning_message)
    assert driver.find_element(By.CSS_SELECTOR,"div#pass-error").is_displayed()


def random_email():
    num = random.randint(10,90)
    num =str(num)
    return 'thushara'+ num +'@gmail.com'

