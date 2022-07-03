import time
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.implicitly_wait(10)
    elif browser == 'firefox':
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        driver.maximize_window()
        driver.implicitly_wait(10)
    else:
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.implicitly_wait(10)
    return driver


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


def pytest_configure(config):
    config._metadata['Project Name'] = 'Roshen'
    config._metadata['Module Name'] = 'FULL AUTOMATION'
    config._metadata['Tester'] = 'Petar Nikolov'


@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)