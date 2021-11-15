from PageObjects.LoginPage import loginpage
from utilities.customlogger import logGen
from utilities.ReadProperties import ReadConfig
from PageObjects.MyInfo import MyInfo
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import pytest


class Test_000_MyInfo_Pages():
    baseurl = ReadConfig.GetAplicationUrl()
    username = ReadConfig.getusername()
    password = ReadConfig.getpassword()
    logger = logGen.logger()
    
    # Function to check Every Category Page using an existing element
    def checkifpageworks(self, categoryname):
        if self.driver.find_element_by_id("menu_pim_viewMyDetails").is_displayed() != True:
            self.logger.error("*** MyInfo Test Failed ***")
            self.logger.error("*** {0} Category Failed to load ***").format(categoryname)
            self.driver.save_screenshot("..\\Screenshots\\" + "test_MyInfo.png")
            assert False
            
    @pytest.mark.sanity
    def test_MyInfo(self, setup):
        self.logger.info("*** Test_000_MyInfo_Page_Categories ***")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.lp = loginpage(self.driver)
        self.lp.setusername(self.username)
        self.lp.setpassword(self.password)
        self.lp.click_login()
        
        self.logger.info("*** Succesfully logged ***")
        self.logger.info("*** Started MyInfo Page Categories Testing ***")
        self.myinfo = MyInfo(self.driver)
        
        
        # Verifying every page
        self.myinfo.ClickOnMyInfo()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID , "profile-pic")))
        self.checkifpageworks("My Info")

        self.myinfo.ClickOnPhotoChange()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID , "profile-pic")))
        self.checkifpageworks("Profile Picture")

        self.myinfo.ClickOnContactDetails()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID , "profile-pic")))
        self.checkifpageworks("Contact Details")

        self.myinfo.ClickOnEmergencyContacts()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID , "profile-pic")))
        self.checkifpageworks("Emergency Contacts")

        self.myinfo.ClickOnDependents()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID , "profile-pic")))
        self.checkifpageworks("Dependents")

        self.myinfo.ClickOnImmigration()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID , "profile-pic")))
        self.checkifpageworks("Immigration")

        self.myinfo.ClickOnJob()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID , "profile-pic")))
        self.checkifpageworks("Job")

        self.myinfo.ClickOnSalary()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID , "profile-pic")))
        self.checkifpageworks("Salary")

        self.myinfo.ClickOnTaxExemptions()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID , "profile-pic")))
        self.checkifpageworks("Tax Exemptions")

        self.myinfo.ClickOnReportTo()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID , "profile-pic")))
        self.checkifpageworks("Report To")
        
        self.myinfo.ClickOnQualifications()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID , "profile-pic")))
        self.checkifpageworks("Qualifications")

        self.myinfo.ClickOnMembership()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID , "profile-pic")))
        self.checkifpageworks("Memberships")

        
        # End of the test
        self.driver.close()
        self.logger.info("*** MyInfo Test Passed ***")
        self.logger.info("*** All Categories Succesfully Loaded ***")
        self.logger.info("*** Ending MyInfo Test ***")
        assert True
        
        
        
        
        
        