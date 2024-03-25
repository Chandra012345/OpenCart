from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class AccountRegistrationPage:
    first_name_id="input-firstname"
    last_name_id="input-lastname"
    email_xpath="//input[@type='email']"
    password_xpath="//input[@type='password']"
    sub_xpath="//input[@class='form-check-input' and @id='input-newsletter']"
    policy_check_xpath="//input[@name='agree']"
    button_xpath="//button[normalize-space()='Continue']"
    confir_msg_xpath="//h1[normalize-space()='Your Account Has Been Created!']"

    def __init__(self,driver):
        self.driver=driver
        self.wait=WebDriverWait(driver,10)

    def setFirstName(self,fname):
        self.driver.find_element(By.ID,self.first_name_id).send_keys(fname)

    def setLastName(self,lname):
        self.driver.find_element(By.ID,self.last_name_id).send_keys(lname)

    def setEmail(self,email):
        self.driver.find_element(By.XPATH,self.email_xpath).send_keys(email)

    def setPassword(self,pwd):
        self.driver.find_element(By.XPATH,self.password_xpath).send_keys(pwd)

    def checkSubscribe(self):
        # self.driver.find_element(By.XPATH,self.sub_xpath).click()
        try:
            checkbox = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.sub_xpath)))
            self.driver.execute_script("arguments[0].click();", checkbox)

        except Exception as e:
            print(e)


    def checkPolicy(self):
        # self.driver.find_element(By.XPATH,self.policy_check_xpath).submit()
        try:
            checkbox = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.policy_check_xpath)))
            self.driver.execute_script("arguments[0].click();", checkbox)

        except Exception as e:
            print(e)


    def clickButton(self):
        # self.driver.find_element(By.XPATH,self.button_xpath).click()
        try:
            checkbox = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.button_xpath)))
            self.driver.execute_script("arguments[0].click();", checkbox)

        except Exception as e:
            print(e)

    def getConfirmation(self):
        try:
            return self.driver.find_element(By.XPATH,self.confir_msg_xpath).text
        except:
            return None