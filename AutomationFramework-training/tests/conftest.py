import pytest
from base.WebdriverFactory import WebdriverFactory
import logging
import logging.config

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default=None, help='Browser to initiate the automation')
    parser.addoption("--headless", action="store", default=None, help='GUI automation option')

@pytest.fixture(scope='session', autouse=True)
def configure_logging():
    logging.config.fileConfig('logging.conf')
    logger = logging.getLogger('testLogger')
    logger.info('Logging is configured.')


@pytest.fixture(scope="class")
def get_driver(request, pytestconfig):
    #wf = WebdriverFactory('Chrome')
    browser1 = pytestconfig.getoption("browser")
    headless1 = pytestconfig.getoption("headless")
    wf = WebdriverFactory(browser1)
    if headless1 is not None:
        driver = wf.get_driver_instance(headless1)
    else:
        driver = wf.get_driver_instance()
    request.cls.driver = driver
    yield
    driver.close()
