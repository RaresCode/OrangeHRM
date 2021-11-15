from PageObjects.LoginPage import loginpage
from utilities.customlogger import logGen
from utilities.ReadProperties import ReadConfig
from PageObjects.MyInfo import MyInfo
from PageObjects.EmergencyContacts import EmergencyContacts
import pytest

class Test_005_Emergency_Contacts():
    baseurl = ReadConfig.GetAplicationUrl()
    username = ReadConfig.getusername()
    password = ReadConfig.getpassword()
    logger = logGen.logger()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_emergency_contacts(self, setup):
        self.logger.info("*** Test_005_Emergency_contacts ***")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.lp = loginpage(self.driver)
        self.lp.setusername(self.username)
        self.lp.setpassword(self.password)
        self.lp.click_login()
        
        self.logger.info("*** Succesfully logged ***")
        self.logger.info("*** Started Emergency Contacts Test ***")
        self.opencategory = MyInfo(self.driver)
        self.opencategory.ClickOnMyInfo()
        self.opencategory.ClickOnEmergencyContacts()
        self.editemergencycontact = EmergencyContacts(self.driver)
        
        # Adding Emergency Contact
        self.logger.info("*** Adding Emergency Contact ***")
        self.editemergencycontact.ClickOnAddEmergencyContact()
        self.editemergencycontact.SetName("Andrei")
        self.editemergencycontact.SetRelationship("Single")
        self.editemergencycontact.SetHomeTelephone("4234324234")
        self.editemergencycontact.SetMobile("0711111111")
        self.editemergencycontact.SetWorkTelephone("0744444444")
        self.editemergencycontact.ClickOnSaveEmergencyContact()
        self.msg1 = self.driver.find_element_by_css_selector("#listEmegrencyContact > div.inner > div").text
        self.logger.info("*** Saving info ***")
        self.logger.info("*** Deleting info ***")
        
        self.editemergencycontact.SelectAllEmergencyContacts()
        self.editemergencycontact.ClickOnDeleteEmergencyContact()
        self.msg2 = self.driver.find_element_by_css_selector("#listEmegrencyContact > div.inner > div").text
        self.logger.info("*** Emergency Contact Validation Started ***")

        if self.msg1 == "Successfully Saved" and self.msg2 == "Successfully Deleted":
            self.logger.info("*** Emergency Contact Test Passed ***")
            assert True
        elif self.msg1 == "Successfully Saved" and self.msg2 != "Successfully Deleted":
            self.logger.error("*** Emergency Contact Test Failed ***")
            self.logger.error("*** Add Emergency Contact Passed but deleting of Emergency Contacts Failed ***")
            self.driver.save_screenshot("..\\Screenshots\\" + "test_emergency_contacts.png")
            assert False
        else:
            self.logger.error("*** Emergency Contact Test Failed ***")
            self.logger.error("*** Add Emergency Contact Failed ***")
            self.driver.save_screenshot("..\\Screenshots\\" + "test_emergency_contacts.png")
            assert False
        
        self.driver.close()
        self.logger.info("*** Ending Emergency Contact test ***")
        
        
        
        
        
        