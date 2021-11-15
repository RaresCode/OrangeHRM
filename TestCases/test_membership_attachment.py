from PageObjects.LoginPage import loginpage
from PageObjects.MyInfo import MyInfo
from PageObjects.Memberships import Memberships
from utilities.customlogger import logGen
from utilities.ReadProperties import ReadConfig
import pytest
import os

class Test_021_Membership_Attachment():
    baseurl = ReadConfig.GetAplicationUrl()
    username = ReadConfig.getusername()
    password = ReadConfig.getpassword()
    logger = logGen.logger()
    
    @pytest.mark.sanity
    @pytest.mark.regression
    def test_membership_attachment(self, setup):
        self.logger.info("*** Test_021_Membership_Attachment ***")
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
        self.opencategory.ClickOnMembership()
        self.membershipattachment = Memberships(self.driver)
        
        # Adding Attachment
        self.logger.info("*** Adding Attachment ***")
        self.membershipattachment.ClickOnAddAttachment()
        
        # Finding Absolute path for the file
        self.abspath = os.path.abspath("..\\TestData\\dog.jpg")
        self.membershipattachment.SetFilePath(self.abspath)
        
        # Uploading and deletion of the attachment
        self.membershipattachment.SetAttachmentComment("This is a comment in english!")
        self.membershipattachment.ClickOnUpload()
        self.saveattachment = self.driver.find_element_by_css_selector("#attachmentList > div.inner > div").text
        self.logger.info("*** Deleting Attachment ***")
        self.membershipattachment.SelectAllAttachments()
        self.membershipattachment.ClickOnDeleteAttachments()
        self.deleteattachment = self.driver.find_element_by_css_selector("#attachmentList > div.inner > div").text
        
        self.logger.info("*** Attachment Validation Test Started ***")
        if self.saveattachment == "Successfully Saved" and self.deleteattachment == "Successfully Deleted":
            self.logger.info("*** Attachment Test Passed ***")
            assert True
        elif self.saveattachment == "Successfully Saved" and self.deleteattachment != "Successfully Deleted":
            self.logger.error("*** Attachment Test Failed ***")
            self.logger.error("*** Adding Attachment Worked but deleting of the Attachment Failed ***")
            self.driver.save_screenshot("..\\Screenshots\\" + "test_MembershipAttachments.png")
            assert False
        else:
            self.logger.error("*** Attachment Test Failed ***")
            self.logger.error("*** Adding Attachment Failed ***")
            self.driver.save_screenshot("..\\Screenshots\\" + "test_MembershipAttachments.png")
            assert False
        
        self.driver.close()
        self.logger.info("*** Ending Attachment test ***")