from PageObjects.LoginPage import loginpage
from utilities.customlogger import logGen
from utilities.ReadProperties import ReadConfig
from PageObjects.MyInfo import MyInfo
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
        self.checkifpageworks("My Info")

        self.myinfo.ClickOnPhotoChange()
        self.checkifpageworks("Profile Picture")

        self.myinfo.ClickOnContactDetails()
        self.checkifpageworks("Contact Details")

        self.myinfo.ClickOnEmergencyContacts()
        self.checkifpageworks("Emergency Contacts")

        self.myinfo.ClickOnDependents()
        self.checkifpageworks("Dependents")

        self.myinfo.ClickOnImmigration()
        self.checkifpageworks("Immigration")

        self.myinfo.ClickOnJob()
        self.checkifpageworks("Job")

        self.myinfo.ClickOnSalary()
        self.checkifpageworks("Salary")

        self.myinfo.ClickOnTaxExemptions()
        self.checkifpageworks("Tax Exemptions")

        self.myinfo.ClickOnReportTo()
        self.checkifpageworks("Report To")
        
        self.myinfo.ClickOnQualifications()
        self.checkifpageworks("Qualifications")

        self.myinfo.ClickOnMembership()
        self.checkifpageworks("Memberships")

        
        # End of the test
        self.driver.close()
        self.logger.info("*** MyInfo Test Passed ***")
        self.logger.info("*** All Categories Succesfully Loaded ***")
        self.logger.info("*** Ending MyInfo Test ***")
        assert True
        
        
        
        
        
        