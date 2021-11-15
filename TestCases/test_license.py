from PageObjects.LoginPage import loginpage
from PageObjects.Qualifications import Qualifications
from utilities.customlogger import logGen
from utilities.ReadProperties import ReadConfig
from PageObjects.MyInfo import MyInfo
import pytest

class Test_012_License():
    baseurl = ReadConfig.GetAplicationUrl()
    username = ReadConfig.getusername()
    password  = ReadConfig.getpassword()
    logger = logGen.logger()
    
    @pytest.mark.regression
    @pytest.mark.sanity
    def test_license(self, setup):
        self.logger.info("*** Test_012_License ***")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.lp = loginpage(self.driver)
        self.lp.setusername(self.username)
        self.lp.setpassword(self.password)
        self.lp.click_login()
        
        self.logger.info("*** Succesfully logged ***")
        self.logger.info("*** Started License Test ***")
        self.editcategory = MyInfo(self.driver)
        self.editcategory.ClickOnMyInfo()
        self.editcategory.ClickOnQualifications()
        
        # License
        self.logger.info("*** Adding License ***")
        self.license = Qualifications(self.driver)
        self.license.ClickOnAddLicense()
        self.license.SetLicenseType("3")
        self.license.SetLicenseNumber("2314543")
        self.license.SetLicenseIssuedDate("2018-03-26")
        self.license.SetLicenseExpireDate("2026-05-12")
        self.license.ClickOnSaveLicense()

        self.logger.info("*** Saving License ***")
        self.savelicenses = self.driver.find_element_by_css_selector("#tblLicense > div.inner > div").text
        self.logger.info("*** Deleting Licenses ***")
        self.license.SelectAllLicenses()
        self.license.ClickOnDeleteLicenses()
        self.deletelicenses = self.driver.find_element_by_css_selector("#tblLicense > div.inner > div").text
        
        self.logger.info("*** License Test Validation Started ***")
        if self.savelicenses == "Successfully Saved" and self.deletelicenses == "Successfully Deleted":
            self.logger.info("*** Licence Test Passed ***")
            assert True
        elif self.savelicenses == "Successfully Saved" and self.deletelicenses != "Successfully Deleted":
            self.logger.error("*** Licence Test Failed ***")
            self.logger.error("*** Adding Licence Worked but deleting of the Licence Failed ***")
            self.driver.save_screenshot("..\\Screenshots\\" + "test_license.png")
            assert False
        else:
            self.logger.error("*** Licence Test Failed ***")
            self.logger.error("*** Adding Licence Failed ***")
            self.driver.save_screenshot("..\\Screenshots\\" + "test_license.png")
            assert False
        
        self.driver.close()
        self.logger.info("*** Ending Licence test ***")