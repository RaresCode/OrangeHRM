from PageObjects.LoginPage import loginpage
from utilities.customlogger import logGen
from utilities.ReadProperties import ReadConfig
from PageObjects.MyInfo import MyInfo
from PageObjects.Immigration import Immigration
import pytest

class Test_007_Immigration():
    baseurl = ReadConfig.GetAplicationUrl()
    username = ReadConfig.getusername()
    password = ReadConfig.getpassword()
    logger = logGen.logger()
    
    @pytest.mark.regression
    def test_immigration(self, setup):
        self.logger.info("*** Test_007_Immigration ***")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.lp = loginpage(self.driver)
        self.lp.setusername(self.username)
        self.lp.setpassword(self.password)
        self.lp.click_login()
        
        self.logger.info("*** Succesfully logged ***")
        self.logger.info("*** Started Immigration Test ***")
        self.editcategory = MyInfo(self.driver)
        self.editcategory.ClickOnMyInfo()
        self.editcategory.ClickOnImmigration()
        
        # Immigration Records
        self.logger.info("*** Adding Immigration Record ***")
        self.immigration = Immigration(self.driver)
        self.immigration.ClickOnAddImmigrationRecord()
        self.immigration.SetDocumentType("Visa")
        self.immigration.SetNumber("44345253")
        self.immigration.SetIssuedDate("2010-03-22")
        self.immigration.SetExpireDate("2011-05-25")
        self.immigration.SetEligibleStatus("Immigrant")
        self.immigration.SetIssuedBy("RO")
        self.immigration.SetEligibleReviewDate("2010-06-27")
        self.immigration.SetComment("This is a comment!!")
        self.immigration.ClickOnSaveImmigrationRecord()
        
        self.logger.info("*** Saving Immigrant Record ***")
        self.msg1 = self.driver.find_element_by_css_selector("#immidrationList > div.inner > div").text
        
        self.logger.info("*** Deleting Immigrant Record ***")
        self.immigration.SelectAllImmigrationRecords()
        self.immigration.ClickOnDeleteAllImmigrations()
        self.msg2 = self.driver.find_element_by_css_selector("#immidrationList > div.inner > div").text
        
        self.logger.info("*** Immigration Test Validation Started ***")
        if self.msg1 == "Successfully Saved" and self.msg2 == "Successfully Deleted":
            self.logger.info("*** Immigration Test Passed ***")
            assert True
        elif self.msg1 == "Successfully Saved" and self.msg2 != "Successfully Deleted":
            self.logger.error("*** Immigration Test Failed ***")
            self.logger.error("*** Adding a Immigration Record Passed but deleting of the Immigration Failed ***")
            self.driver.save_screenshot("..\\Screenshots\\" + "test_Immigration.png")
            assert False
        else:
            self.logger.error("*** Immigration Test Failed ***")
            self.logger.error("*** Adding a Immigration Record Failed ***")
            self.driver.save_screenshot("..\\Screenshots\\" + "test_Immigration.png")
            assert False
        
        self.driver.close()
        self.logger.info("*** Ending Immigration test ***")
        
        
        