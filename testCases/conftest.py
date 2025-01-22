import os.path
import pytest
from selenium import webdriver
from datetime import datetime


@pytest.fixture
def setup(request):
    browser = request.config.getoption("--browser")  # Get the browser from the command line
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "edge":
        driver = webdriver.Edge()
    else:
        raise ValueError(f"Unsupported browser: {browser}")

    yield driver
    driver.quit()

def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",  # Default browser
        help="Browser to run tests: chrome, firefox, edge"
    )




############# Pytest HTML Report ####################
def pytest_configure(config):
    config.metadata['Project Name']= 'Opencart'
    config.metadata['Module Name']= 'CustRegistration'
    config.metadata['Tester']='Manish'

@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA_Home", None)
    metadata.pop("Plugins", None)

@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    config.option.htmlpath=os.path.abspath(os.curdir)+"\\reports\\"+datetime.now().strftime("%d-%m-%y  %H-%M-%S")+".html"