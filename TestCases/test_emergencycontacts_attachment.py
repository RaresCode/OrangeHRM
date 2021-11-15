from PageObjects.LoginPage import loginpage
from PageObjects.MyInfo import MyInfo
from PageObjects.EmergencyContacts import EmergencyContacts
from utilities.customlogger import logGen
from utilities.ReadProperties import ReadConfig
import pytest
import os

class Test_017_EmergencyContacts_Attachment():
    baseurl = ReadConfig.GetAplicationUrl()
    username = ReadConfig.getusername()
    password = ReadConfig.getpassword()
    logger = logGen.logger()
    
    @pytest.mark.sanity
    @pytest.mark.regression
    def test_emergencycontacts_attachment(self, setup):
        self.logger.info("*** Test_017_EmergencyContacts_Attachment ***")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.lp = loginpage(self.driver)
        self.lp.setusername(self.username)
        self.lp.setpassword(self.password)
        self.lp.click_login()

        self.logger.info("*** Succesfully logged ***")
        self.logger.info("*** Started Attachment Test ***")
        self.opencategory = MyInfo(self.driver)
        self.opencategory.ClickOnMyInfo()
        self.opencategory.ClickOnEmergencyContacts()
        self.emergencyattachment = EmergencyContacts(self.driver)
        
        # Adding Emergency Contact Attachment
        self.logger.info("*** Adding Attachment ***")
        self.emergencyattachment.ClickOnAddAttachment()
        
        # Finding Absolute path for the photo
        self.abspath = os.path.abspath("..\\TestData\\dog.jpg")
        self.emergencyattachment.SetFilePath(self.abspath)
        
        # Emergency Contact Attachment Uploading and Deletion
        self.emergencyattachment.SetAttachmentComment("This is a comment in english!")
        self.emergencyattachment.ClickOnUpload()
        self.saveattachment = self.driver.find_element_by_css_selector("#attachmentList > div.inner > div").text
        self.logger.info("*** Deleting Attachment ***")
        self.emergencyattachment.SelectAllAttachments()
        self.emergencyattachment.ClickOnDeleteAttachments()
        self.deleteattachment = self.driver.find_element_by_css_selector("#attachmentList > div.inner > div").text
        
        self.logger.info("*** Attachment Validation Test Started ***")
        if self.saveattachment == "Successfully Saved" and self.deleteattachment == "Successfully Deleted":
            self.logger.info("*** Attachment Test Passed ***")
            assert True
        elif self.saveattachment == "Successfully Saved" and self.deleteattachment != "Successfully Deleted":
            self.logger.error("*** Attachment Test Failed ***")
            self.logger.error("*** Adding Attachment Worked but deleting of the Attachment Failed ***")
            self.driver.save_screenshot("..\\Screenshots\\" + "test_EmergencyContactAttachment.png")
            assert False
        else:
            self.logger.error("*** Attachment Test Failed ***")
            self.logger.error("*** Adding Attachment Failed ***")
            self.driver.save_screenshot("..\\Screenshots\\" + "test_EmergencyContactAttachment.png")
            assert False
        
        self.driver.close()
        self.logger.info("*** Ending Attachment test ***")