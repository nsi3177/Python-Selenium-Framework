import pytest
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="Chrome", help="browser options: Chrome, Firefox or Safari")


@pytest.fixture(scope='class')
def browser_setup(request):
    browser_name = request.config.getoption("browser")
    if browser_name == "Chrome" or browser_name == "chrome":
        driver = webdriver.Chrome('/Users/ninadingale/PycharmProjects/chromedriver')
        driver.set_window_size(1500, 800)
        driver.get('https://rahulshettyacademy.com/angularpractice/')
    elif browser_name == "Firefox" or browser_name == "firefox":
        cap = DesiredCapabilities.FIREFOX
        cap["marionette"] = True
        driver = webdriver.Firefox(desired_capabilities=cap, executable_path='/Users/ninadingale/PycharmProjects/geckodriver')
        driver.set_window_size(1500, 800)
        driver.get('https://rahulshettyacademy.com/angularpractice/')
    request.cls.driver = driver
    yield
    driver.close()


