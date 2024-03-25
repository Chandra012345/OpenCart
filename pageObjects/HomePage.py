import pytest
from selenium.webdriver.common.by import By


class HomePage:
    my_account_xpath="//span[normalize-space()='My Account']"
    register_link_text="Register"
    login_link_text="Login"



    def __init__(self,driver):
        self.driver=driver


    def clikMyAccount(self):
        self.driver.find_element(By.XPATH,self.my_account_xpath).click()

    def clickRegister(self):
        self.driver.find_element(By.LINK_TEXT,self.register_link_text).click()

    def clickLogin(self):
        self.driver.find_element(By.LINK_TEXT,self.login_link_text).click()