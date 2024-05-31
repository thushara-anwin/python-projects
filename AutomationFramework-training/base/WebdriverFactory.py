from selenium import webdriver
from data.session_data import *
class WebdriverFactory:
    def __init__(self, browser):
        self.browser = browser

    def get_driver_instance(self, headless=False):
        driver = None
        if self.browser.lower() == 'chrome':
            crm_option = webdriver.ChromeOptions()
            if headless:
                crm_option.add_argument('--headless')
            driver = webdriver.Chrome(options=crm_option)

        elif self.browser.lower() == 'firefox':
            driver = webdriver.Firefox()

        elif self.browser.lower() == 'edge':
            driver = webdriver.Edge()
        driver.maximize_window()
        return driver
