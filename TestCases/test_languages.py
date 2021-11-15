from PageObjects.LoginPage import loginpage
from PageObjects.Qualifications import Qualifications
from utilities.customlogger import logGen
from utilities.ReadProperties import ReadConfig
from PageObjects.MyInfo import MyInfo
import pytest

class Test_011_Languages():
    baseurl = ReadConfig.GetAplicationUrl()
    username = ReadConfig.getusername()
    password  = ReadConfig.getpassword()
    logger = logGen.logger()
    
    @pytest.mark.regression
    @pytest.mark.sanity
    def test_languages(self, setup):
        self.logger.info("*** Test_011_Languages ***")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.lp = loginpage(self.driver)
        self.lp.setusername(self.username)
        self.lp.setpassword(self.password)
        self.lp.click_login()
        
        self.logger.info("*** Succesfully logged ***")
        self.logger.info("*** Started Languages Test ***")
        self.editcategory = MyInfo(self.driver)
        self.editcategory.ClickOnMyInfo()
        self.editcategory.ClickOnQualifications()
        
        # Languages
        self.logger.info("*** Adding Language ***")
        self.languages = Qualifications(self.driver)
        self.languages.ClickOnAddLanguages()
        self.languages.SetLanguage("3")
        self.languages.SetLanguageFluency("1")
        self.languages.SetLanguageCompetency("3")
        self.languages.SetLanguageComment("This is another comment!!")
        self.languages.ClickOnSaveLanguage()

        self.logger.info("*** Saving Language ***")
        self.savelanguages = self.driver.find_element_by_css_selector("#tblLanguage > div.inner > div").text
        self.logger.info("*** Deleting Languages ***")
        self.languages.SelectAllLanguages()
        self.languages.ClickOnDeleteLanguages()
        self.deletelanguages = self.driver.find_element_by_css_selector("#tblLanguage > div.inner > div").text

        self.logger.info("*** Languages Test Validation Started ***")
        if self.savelanguages == "Successfully Saved" and self.deletelanguages == "Successfully Deleted":
            self.logger.info("*** Languages Test Passed ***")
            assert True
        elif self.savelanguages == "Successfully Saved" and self.deletelanguages != "Successfully Deleted":
            self.logger.error("*** Languages Test Failed ***")
            self.logger.error("*** Adding Language Worked but deleting of the Languages Failed ***")
            self.driver.save_screenshot("..\\Screenshots\\" + "test_languages.png")
            assert False
        else:
            self.logger.error("*** Languages Test Failed ***")
            self.logger.error("*** Adding Language Failed ***")
            self.driver.save_screenshot("..\\Screenshots\\" + "test_languages.png")
            assert False
        
        self.driver.close()
        self.logger.info("*** Ending Languages test ***")