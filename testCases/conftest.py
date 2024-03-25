import os.path

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from datetime import datetime

@pytest.fixture()
def setup(browser):
    # serv_obj = Service("C:\\Users\\hp\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")
    # driver = webdriver.Chrome(service=serv_obj)
    # return driver
    if browser=='edge':
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
        print("Launching Edge browser..........")
    elif browser=='firefox':
        driver=webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        print("Launching Firefox browser.........")
    else:
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
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