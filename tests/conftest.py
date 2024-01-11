import pytest
from selenium import webdriver

from locators import Locators
from pages.HomePage import HomePage


def pytest_addoption(parser):
    parser.addoption(
        '--browser_name', action='store', default='firefox'
    )


@pytest.fixture(scope="function")
def setup(request):
    browser_name = request.config.getoption('browser_name')
    if browser_name == 'chrome':
        driver = webdriver.Chrome()
    elif browser_name == 'firefox':
        driver = webdriver.Firefox()
    driver.get('https://practice.automationtesting.in/')
    driver.maximize_window()
    driver.find_element(*Locators.HomePageLocators.alert_window).click()

    request.cls.driver = driver
    yield
    driver.close()
