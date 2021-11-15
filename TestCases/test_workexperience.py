from PageObjects.LoginPage import loginpage
from PageObjects.Qualifications import Qualifications
from utilities.customlogger import logGen
from utilities.ReadProperties import ReadConfig
from PageObjects.MyInfo import MyInfo
import pytest

class Test_008_Work_Experience():
    baseurl = ReadConfig.GetAplicationUrl()
    username = ReadConfig.getusername()
    password  = ReadConfig.getpassword()
    logger = logGen.logger()
    
    @pytest.mark.regression
    @pytest.mark.sanity
    def test_work_experience(self, setup):
        self.logger.info("*** Test_008_Work_Experience ***")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.lp = loginpage(self.driver)
        self.lp.setusername(self.username)
        self.lp.setpassword(self.password)
        self.lp.click_login()
        
        self.logger.info("*** Succesfully logged ***")
        self.logger.info("*** Started Work Experience Test ***")
        self.editcategory = MyInfo(self.driver)
        self.editcategory.ClickOnMyInfo()
        self.editcategory.ClickOnQualifications()
        
        # Work Experience
        self.logger.info("*** Adding Work Experience ***")
        self.experience = Qualifications(self.driver)
        self.experience.ClickOnAddExperience()
        self.experience.SetExpCompany("Amazon")
        self.experience.SetJobTitle("QA")
        self.experience.SetExpFromDate("2012-03-22")
        self.experience.SetExpToDate("2014-05-21")
        self.experience.SetExpComment("This is a comment!!")
        self.experience.ClickOnSaveExp()
        
        self.logger.info("*** Saving Work Experience ***")
        self.saveexp = self.driver.find_element_by_css_selector("#sectionWorkExperience > div.inner > div").text
        self.logger.info("*** Deleting Work Experience ***")
        self.experience.SelectAllExp()
        self.experience.ClickOnDeleteExp()
        self.deleteexp = self.driver.find_element_by_css_selector("#sectionWorkExperience > div.inner > div").text
        
        self.logger.info("*** Work Experience Test Validation Started ***")
        if self.saveexp == "Successfully Saved" and self.deleteexp == "Successfully Deleted":
            self.logger.info("*** Work Experience Test Passed ***")
            assert True
        elif self.saveexp == "Successfully Saved" and self.deleteexp != "Successfully Deleted":
            self.logger.error("*** Work Experience Test Failed ***")
            self.logger.error("*** Adding Work Experience Worked but deleting of Work Experience Failed ***")
            self.driver.save_screenshot("..\\Screenshots\\" + "test_work_experience.png")
            assert False
        else:
            self.logger.error("*** Work Experience Test Failed ***")
            self.logger.error("*** Adding Work Experience Failed ***")
            self.driver.save_screenshot("..\\Screenshots\\" + "test_work_experience.png")
            assert False
        
        self.driver.close()
        self.logger.info("*** Ending Work Experience test ***")
