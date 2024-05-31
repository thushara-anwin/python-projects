
import pytest
from base.WebdriverFactory import WebdriverFactory


@pytest.fixture(scope="class")
def set_up_and_tear_down(request):
    wf = WebdriverFactory('Chrome')
    driver = wf.get_driver_instance()
    driver.get("https://magento.softwaretestingboard.com/")
    request.cls.driver = driver
    yield
    driver.close()

