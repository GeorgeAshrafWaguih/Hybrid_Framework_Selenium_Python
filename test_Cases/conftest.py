import pytest
from selenium import webdriver


@pytest.fixture
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
        print("Launching Chrome browser ---------")
    elif browser == 'firefox':
        driver = webdriver.Firefox()
        print("Launching Firefox browser ---------")
    else:
        driver = webdriver.Chrome()  # This will be the default browser
    return driver


def pytest_addoption(parser):       # This will get the value from CLI ?hooks
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):       # This will return the Browser value to setup method
    return request.config.getoption("--browser")


# --------------- Pytest HTML Report ---------------
# Hook for adding Environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'Hybrid Framework'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'George'


# Hook for delete/modify Environment info to HTML Report
@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
