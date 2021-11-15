from PageObjects.LoginPage import loginpage
from utilities.customlogger import logGen
from utilities.ReadProperties import ReadConfig
from PageObjects.MyInfo import MyInfo
from PageObjects.Dependents import Dependents
import pytest

class Test_006_Dependents():
    baseurl = ReadConfig.GetAplicationUrl()
    username = ReadConfig.getusername()
    password = ReadConfig.getpassword()
    logger = logGen.logger()
    
    @pytest.mark.regression
    def test_dependents(self, setup):
        self.logger.info("*** Test_006_Dependents ***")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.lp = loginpage(self.driver)
        self.lp.setusername(self.username)
        self.lp.setpassword(self.password)
        self.lp.click_login()

        self.logger.info("*** Succesfully logged ***")
        self.logger.info("*** Started Dependents Test ***")
        self.opencategory = MyInfo(self.driver)
        self.opencategory.ClickOnMyInfo()
        self.opencategory.ClickOnDependents()
        self.dependents = Dependents(self.driver)
        
        # Adding a dependent
        self.logger.info("*** Adding Dependent ***")
        self.dependents.ClickOnAddDependent()
        self.dependents.SetName("Ionut")
        self.dependents.SetRelationship("child")
        self.dependents.SetDob("2007-02-02")
        self.dependents.ClickOnSaveDependent()
        
        self.logger.info("*** Saving Dependent ***")
        self.msg1 = self.driver.find_element_by_css_selector("#listing > div.inner > div").text
        
        self.logger.info("*** Deleting Dependent ***")
        self.dependents.SelectAllDependents()
        self.dependents.ClickOnDeleteDependents()
        self.msg2 = self.driver.find_element_by_css_selector("#listing > div.inner > div").text
        
        self.logger.info("*** Dependent Test Validation Started ***")
        if self.msg1 == "Successfully Saved" and self.msg2 == "Successfully Deleted":
            self.logger.info("*** Dependent Test Passed ***")
            assert True
        elif self.msg1 == "Successfully Saved" and self.msg2 != "Successfully Deleted":
            self.logger.error("*** Dependent Test Failed ***")
            self.logger.error("*** Adding a Dependent Passed but deleting of the Dependents Failed ***")
            self.driver.save_screenshot("..\\Screenshots\\" + "test_dependent.png")
            assert False
        else:
            self.logger.error("*** Dependent Test Failed ***")
            self.logger.error("*** Adding a Dependent Failed ***")
            self.driver.save_screenshot("..\\Screenshots\\" + "test_dependent.png")
            assert False
        
        self.driver.close()
        self.logger.info("*** Ending Dependent test ***")
        