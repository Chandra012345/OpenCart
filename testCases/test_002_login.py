import pytest
from pageObjects.HomePage import HomePage
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import os

class Test_Login:
    import time

    baseURL=ReadConfig.getApplicationURL()
    logger=LogGen.loggen()
    user=ReadConfig.getUseremail()
    pasword=ReadConfig.getPassword()


    def test_login(self,setup):

        self.logger.info("*******  starting test_002_login ******")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.hp=HomePage(self.driver)
        self.hp.clikMyAccount()
        self.hp.clickLogin()

        self.lp=LoginPage(self.driver)
        self.lp.setEmail(self.user)
        self.lp.setPassword(self.pasword)
        self.lp.clickLogin()
        self.targetpage=self.lp.getConfirmationMsg()
        self.time.sleep(5)
        if self.targetpage==True:
            assert True
        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir)+"\\screenshots\\"+"test_login.png")
            assert False

        self.driver.close()
        self.logger.info("****** End of test_002_login ********")


