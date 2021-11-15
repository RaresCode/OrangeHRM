from PageObjects.LoginPage import loginpage
from PageObjects.PersonalDetails import PersonalDetails
from PageObjects.MyInfo import MyInfo
from utilities.customlogger import logGen
from utilities.ReadProperties import ReadConfig
import pytest
import os

class Test_015_PersonalDetails_Attachment():
    baseurl = ReadConfig.GetAplicationUrl()
    username = ReadConfig.getusername()
    password = ReadConfig.getpassword()
    logger = logGen.logger()
    
    @pytest.mark.sanity
    @pytest.mark.regression
    def test_personaldetails_attachment(self, setup):
        self.logger.info("*** Test_015_PersonalDetails_Attachment ***")
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
        self.persdetails_attachment = PersonalDetails(self.driver)
        
        # Adding Attachment
        self.logger.info("*** Adding Attachment ***")
        self.persdetails_attachment.ClickOnAddAttachment()
        
        # Finding Absolute path for the photo
        self.abspath = os.path.abspath("..\\TestData\\dog.jpg")
        self.persdetails_attachment.SetFilePath(self.abspath)
        
        # Personal Details Attachments uploading and deletion
        self.persdetails_attachment.SetAttachmentComment("Aici este un comment in romana :P")
        self.persdetails_attachment.ClickOnUpload()
        self.saveattachment = self.driver.find_element_by_css_selector("#attachmentList > div.inner > div").text
        self.logger.info("*** Deleting Attachment ***")
        self.persdetails_attachment.SelectAllAttachments()
        self.persdetails_attachment.ClickOnDeleteAttachments()
        self.deleteattachment = self.driver.find_element_by_css_selector("#attachmentList > div.inner > div").text
        
        self.logger.info("*** Attachment Validation Test Started ***")
        if self.saveattachment == "Successfully Saved" and self.deleteattachment == "Successfully Deleted":
            self.logger.info("*** Attachment Test Passed ***")
            assert True
        elif self.saveattachment == "Successfully Saved" and self.deleteattachment != "Successfully Deleted":
            self.logger.error("*** Attachment Test Failed ***")
            self.logger.error("*** Adding Attachment Worked but deleting of the Attachment Failed ***")
            self.driver.save_screenshot("..\\Screenshots\\" + "test_PersDetailsAttachment.png")
            assert False
        else:
            self.logger.error("*** Attachment Test Failed ***")
            self.logger.error("*** Adding Attachment Failed ***")
            self.driver.save_screenshot("..\\Screenshots\\" + "test_PersDetailsAttachment.png")
            assert False
        
        self.driver.close()
        self.logger.info("*** Ending Attachment test ***")
        