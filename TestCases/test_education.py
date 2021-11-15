from PageObjects.LoginPage import loginpage
from PageObjects.Qualifications import Qualifications
from utilities.customlogger import logGen
from utilities.ReadProperties import ReadConfig
from PageObjects.MyInfo import MyInfo
import pytest

class Test_009_Education():
    baseurl = ReadConfig.GetAplicationUrl()
    username = ReadConfig.getusername()
    password  = ReadConfig.getpassword()
    logger = logGen.logger()
    
    @pytest.mark.regression
    @pytest.mark.sanity
    def test_education(self, setup):
        self.logger.info("*** Test_009_Education ***")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.lp = loginpage(self.driver)
        self.lp.setusername(self.username)
        self.lp.setpassword(self.password)
        self.lp.click_login()
        
        self.logger.info("*** Succesfully logged ***")
        self.logger.info("*** Started Education Test ***")
        self.editcategory = MyInfo(self.driver)
        self.editcategory.ClickOnMyInfo()
        self.editcategory.ClickOnQualifications()
        
        self.logger.info("*** Adding Education ***")
        self.education = Qualifications(self.driver)
        self.education.ClickOnAddEducation()
        self.education.SetEducationLevel("2")
        self.education.SetEducationInstitute("Whale Gulch University")
        self.education.SetEducationMajor("Economic Geography")
        self.education.SetEducationYear("4")
        self.education.SetEducationGPA("3.5")
        self.education.SetEducationStartDate("2008-02-12")
        self.education.SetEducationEndDate("2012-02-23")
        self.education.ClickOnSaveEducation()

        self.logger.info("*** Saving Education ***")
        self.saveeducation = self.driver.find_element_by_css_selector("#content > div > div:nth-child(7) > div.inner > div").text
        self.logger.info("*** Deleting Education ***")
        self.education.SelectAllEducation()
        self.education.ClickOnDeleteEducation()
        self.deleteeducation = self.driver.find_element_by_css_selector("#content > div > div:nth-child(7) > div.inner > div").text
        
        self.logger.info("*** Education Test Validation Started ***")
        if self.saveeducation == "Successfully Saved" and self.deleteeducation == "Successfully Deleted":
            self.logger.info("*** Education Test Passed ***")
            assert True
        elif self.saveeducation == "Successfully Saved" and self.deleteeducation != "Successfully Deleted":
            self.logger.error("*** Education Test Failed ***")
            self.logger.error("*** Adding Education Worked but deleting of Education Failed ***")
            self.driver.save_screenshot("..\\Screenshots\\" + "test_education.png")
            assert False
        else:
            self.logger.error("*** Education Test Failed ***")
            self.logger.error("*** Adding Education Failed ***")
            self.driver.save_screenshot("..\\Screenshots\\" + "test_education.png")
            assert False
        
        self.driver.close()
        self.logger.info("*** Ending Education test ***")
