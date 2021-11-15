from PageObjects.LoginPage import loginpage
from utilities.customlogger import logGen
from utilities.ReadProperties import ReadConfig
from PageObjects.MyInfo import MyInfo
from PageObjects.Photograph import Photograph
import pytest
import os

class Test_014_Profile_Picture():
    baseurl = ReadConfig.GetAplicationUrl()
    username = ReadConfig.getusername()
    password  = ReadConfig.getpassword()
    logger = logGen.logger()
    
    @pytest.mark.regression
    @pytest.mark.sanity
    def test_ProfilePicture(self, setup):
        self.logger.info("*** Test_014_Profile_Picture ***")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.lp = loginpage(self.driver)
        self.lp.setusername(self.username)
        self.lp.setpassword(self.password)
        self.lp.click_login()
        
        self.logger.info("*** Succesfully logged ***")
        self.logger.info("*** Started Profile Picture Test ***")
        self.editcategory = MyInfo(self.driver)
        self.editcategory.ClickOnMyInfo()
        self.editcategory.ClickOnPhotoChange()
        
        # Profile Picture
        self.logger.info("*** Saving Photograph ***")
        self.photograph = Photograph(self.driver)
        
        # Finding Absolute path for the photo
        self.abspath = os.path.abspath("..\\TestData\\dog.jpg")
        self.photograph.SetFilePath(self.abspath)
        
        # Uploading the photo
        self.photograph.ClickOnUpload()
        self.photosaved = self.driver.find_element_by_css_selector("#content > div.box.pimPane > div.inner > div").text
        self.logger.info("*** Deleting Photograph ***")
        self.photograph.ClickOnDelete()
        self.photograph.ClickOnConfirmDeletion()
        self.photodeleted = self.driver.find_element_by_css_selector("#content > div.box.pimPane > div.inner > div").text
        
        self.logger.info("*** Photo Validation Test Started ***")
        if self.photosaved == "Successfully Uploaded" and self.photodeleted == "Successfully Deleted":
            self.logger.info("*** Profile Picture Test Passed ***")
            assert True
        elif self.photosaved == "Successfully Uploaded" and self.photodeleted != "Successfully Deleted":
            self.logger.error("*** Profile Picture Test Failed ***")
            self.logger.error("*** Adding Photograph Worked but deleting of the Picture Failed ***")
            self.driver.save_screenshot("..\\Screenshots\\" + "test_profilepicture.png")
            assert False
        else:
            self.logger.error("*** Profile Picture Test Failed ***")
            self.logger.error("*** Adding Photograph Failed ***")
            self.driver.save_screenshot("..\\Screenshots\\" + "test_profilepicture.png")
            assert False
        
        self.driver.close()
        self.logger.info("*** Ending Profile Picture test ***")
        
        
        
        
        
        