import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from helpers import testconfig

pytest_plugins = [
 "testcases.tc_surplus_login"
]

@pytest.fixture
def driver(scope="module"):
    if testconfig.browser.lower() == "chrome":
        wdriver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    if testconfig.browser.lower() == "edge":
        wdriver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
    return wdriver