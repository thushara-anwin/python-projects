from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select
import logging
log = logging.getLogger('testLogger')


class SeleniumBase:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.timeout = timeout
        self.wait = WebDriverWait(self.driver, self.timeout)

    def get_element(self, locator):
        try:
            log.info(f"finding element:{locator}")
            element = self.wait.until(ec.visibility_of_element_located(locator))
            return element
        except Exception as e:
            self.driver.save_screenshot("locator_file.png")
            raise

    def click_element(self, locator):
        log.info(f"click to element :{locator}")
        element = self.get_element(locator)
        element.click()

    def enter_value(self, data, locator):
        log.info(f"enter value {data} to element :{locator} ")
        element = self.get_element(locator)
        element.send_keys(data)

    def select_dropdown_value(self, value, locator):
        element = self.get_element(locator)
        obj = Select(element)
        obj.select_by_visible_text(value)
