import time

import pytest
from helpers import testconfig
from helpers import commonmethods as helper
from testdata import td_surplus_login1 as testdata
from pageobjects import pg_surplus_login
@pytest.mark.smoke
def test_verify_title(driver):
    helper.maximize(driver)
    driver.get(testconfig.base_url)
    helper.verify_page_title(driver,testdata.webpage_title)
    pg_surplus_login.verify_text(driver)
    helper.close_browser(driver)

def test_gust_login(driver):
    helper.maximize(driver)
    driver.get(testconfig.base_url)
    helper.verify_page_title(driver,testdata.webpage_title)
    pg_surplus_login.verify_gust_login(driver)
    time.sleep(5)


