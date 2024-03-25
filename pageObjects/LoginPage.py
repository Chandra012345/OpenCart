from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    txt_email_xpath="//input[@name='email']"
    txt_password_xpath="//input[@name='password']"
    submit_xpath="//button[@type='submit']"
    msg_myaccount_xpath="//h2[normalize-space()='My Account']"

    def __init__(self,driver):
        self.driver=driver

    def setEmail(self,email):
        self.driver.find_element(By.XPATH,self.txt_email_xpath).send_keys(email)

    def setPassword(self,pwd):
        self.driver.find_element(By.XPATH,self.txt_password_xpath).send_keys(pwd)

    def clickLogin(self):
        self.driver.find_element(By.XPATH,self.submit_xpath).click()

    def getConfirmationMsg(self):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, self.msg_myaccount_xpath))
            )
            return element.is_displayed()
        except:
            return False


