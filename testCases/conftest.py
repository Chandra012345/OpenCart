import os.path
import pytest
from selenium import webdriver
from datetime import datetime

@pytest.fixture()
def setup(browser):
    if browser=='edge':
        driver = webdriver.Edge()
        print("Launching Edge browser..........")
    elif browser=='firefox':
        driver=webdriver.Firefox()
        print("Launching Firefox browser.........")
    else:
        driver = webdriver.Chrome()
        print("Launching Chrome browser..........")

    return driver

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


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