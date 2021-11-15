from PageObjects.LoginPage import loginpage
from utilities.customlogger import logGen
from utilities.ReadProperties import ReadConfig
from PageObjects.MyInfo import MyInfo
from PageObjects.Memberships import Memberships
import pytest

class Test_013_Memberships():
    baseurl = ReadConfig.GetAplicationUrl()
    username = ReadConfig.getusername()
    password  = ReadConfig.getpassword()
    logger = logGen.logger()
    
    @pytest.mark.regression
    @pytest.mark.sanity
    def test_Memberships(self, setup):
        self.logger.info("*** Test_013_Memberships ***")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.lp = loginpage(self.driver)
        self.lp.setusername(self.username)
        self.lp.setpassword(self.password)
        self.lp.click_login()
        
        self.logger.info("*** Succesfully logged ***")
        self.logger.info("*** Started Assign Membership Test ***")
        self.editcategory = MyInfo(self.driver)
        self.editcategory.ClickOnMyInfo()
        self.editcategory.ClickOnMembership()
        
        # Memberships
        self.logger.info("*** Assigning Membership ***")
        self.memberships = Memberships(self.driver)
        self.memberships.ClickOnAddMembership()
        self.memberships.SetMembershipType("4")
        self.memberships.SetSubscriptionPaidBy("Individual")
        self.memberships.SetSubscriptionAmount("20")
        self.memberships.SetCurrencyType("EUR")
        self.memberships.SetSubscriptionStartDate("2020-02-02")
        self.memberships.SetSubscriptionEndDate("2021-02-02")
        self.memberships.ClickOnSaveMembership()
        
        self.logger.info("*** Saving Membership ***")
        self.saveMembership = self.driver.find_element_by_css_selector("#listMembershipDetails > div.inner > div").text
        self.logger.info("*** Deleting Memberships ***")
        self.memberships.SelectAllMemberships()
        self.memberships.ClickOnDeleteMemberships()
        self.deleteMemberships = self.driver.find_element_by_css_selector("#listMembershipDetails > div.inner > div").text
        
        self.logger.info("*** Memberships Test Validation Started ***")
        if self.saveMembership == "Successfully Saved" and self.deleteMemberships == "Successfully Deleted":
            self.logger.info("*** Memberships Test Passed ***")
            assert True
        elif self.saveMembership == "Successfully Saved" and self.deleteMemberships != "Successfully Deleted":
            self.logger.error("*** Memberships Test Failed ***")
            self.logger.error("*** Adding Membership Worked but deleting of the Memberships Failed ***")
            self.driver.save_screenshot("..\\Screenshots\\" + "test_memberships.png")
            assert False
        else:
            self.logger.error("*** Memberships Test Failed ***")
            self.logger.error("*** Adding Membership Failed ***")
            self.driver.save_screenshot("..\\Screenshots\\" + "test_memberships.png")
            assert False
        
        self.driver.close()
        self.logger.info("*** Ending Memberships test ***")