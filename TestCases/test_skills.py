from PageObjects.LoginPage import loginpage
from PageObjects.Qualifications import Qualifications
from utilities.customlogger import logGen
from utilities.ReadProperties import ReadConfig
from PageObjects.MyInfo import MyInfo
import pytest

class Test_010_Skills():
    baseurl = ReadConfig.GetAplicationUrl()
    username = ReadConfig.getusername()
    password  = ReadConfig.getpassword()
    logger = logGen.logger()
    
    @pytest.mark.regression
    @pytest.mark.sanity
    def test_skills(self, setup):
        self.logger.info("*** Test_010_Skills ***")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.lp = loginpage(self.driver)
        self.lp.setusername(self.username)
        self.lp.setpassword(self.password)
        self.lp.click_login()
        
        self.logger.info("*** Succesfully logged ***")
        self.logger.info("*** Started Skills Test ***")
        self.editcategory = MyInfo(self.driver)
        self.editcategory.ClickOnMyInfo()
        self.editcategory.ClickOnQualifications()
        
        self.logger.info("*** Adding Skill ***")
        self.skills = Qualifications(self.driver)
        self.skills.ClickOnAddSkills()
        self.skills.SetSkill("2")
        self.skills.SetSkillYearOfExp("2")
        self.skills.SetSkillComment("This is another comment!")
        self.skills.ClickOnSaveSkill()

        self.logger.info("*** Saving Skill ***")
        self.saveskills = self.driver.find_element_by_css_selector("#tblSkill > div.inner > div").text
        self.logger.info("*** Deleting Skills ***")
        self.skills.SelectAllSkills()
        self.skills.ClickOnDeleteSkills()
        self.deleteskills = self.driver.find_element_by_css_selector("#tblSkill > div.inner > div").text

        self.logger.info("*** Skills Test Validation Started ***")
        if self.saveskills == "Successfully Saved" and self.deleteskills == "Successfully Deleted":
            self.logger.info("*** Skills Test Passed ***")
            assert True
        elif self.saveskills == "Successfully Saved" and self.deleteskills != "Successfully Deleted":
            self.logger.error("*** Skills Test Failed ***")
            self.logger.error("*** Adding Skill Worked but deleting of the Skill Failed ***")
            self.driver.save_screenshot("..\\Screenshots\\" + "test_skills.png")
            assert False
        else:
            self.logger.error("*** Skills Test Failed ***")
            self.logger.error("*** Adding Skill Failed ***")
            self.driver.save_screenshot("..\\Screenshots\\" + "test_skills.png")
            assert False
        
        self.driver.close()
        self.logger.info("*** Ending Skills test ***")