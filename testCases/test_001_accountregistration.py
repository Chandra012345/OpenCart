from pageObjects.HomePage import HomePage
from pageObjects.AccountRegistrationPage import AccountRegistrationPage
from utilities import randomstring
import os
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen



class Test_001_AccountReg:
    import time
    base_url=ReadConfig.getApplicationURL()
    logger=LogGen.loggen()
    def test_account_reg(self,setup):
        self.logger.info("*** test_001_AccountRegistration started ***"
                         "")
        self.driver=setup
        self.driver.get(self.base_url)

        self.logger.info("Launching application")
        self.driver.maximize_window()
        self.hp=HomePage(self.driver)

        self.logger.info("clicking on My account : Register ")
        self.hp.clikMyAccount()
        self.hp.clickRegister()

        self.logger.info("Providing custome details")
        self.regpage=AccountRegistrationPage(self.driver)
        self.regpage.setFirstName("Ram")
        self.regpage.setLastName("Chandra")
        self.email=randomstring.random_string_generator()+'@gmail.com'
        self.regpage.setEmail(self.email)
        self.regpage.setPassword("ramchandra")

        self.regpage.checkSubscribe()
        self.regpage.checkPolicy()
        self.regpage.clickButton()
        self.time.sleep(5)
        self.confmsg=self.regpage.getConfirmation()
        if self.confmsg=="Your Account Has Been Created!":
            self.logger.info("Account registration is passed")
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir)+"\\screenshots\\"+"test_account_reg.png")
            self.logger.error("Account registration is failed ")
            self.driver.close()
            assert False
            




