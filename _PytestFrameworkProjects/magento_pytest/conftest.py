from selenium import webdriver


def set_up_and_tear_down():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("https://magento.softwaretestingboard.com/")
    yield
    driver.close()