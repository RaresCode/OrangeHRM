from PageObjects.LoginPage import loginpage
from utilities.customlogger import logGen
from utilities.ReadProperties import ReadConfig
from PageObjects.ContactDetails import ContactDetails
from PageObjects.MyInfo import MyInfo
import pytest

class Test_004_Edit_Contact_Details():
    baseurl = ReadConfig.GetAplicationUrl()
    username = ReadConfig.getusername()
    password = ReadConfig.getpassword()
    logger = logGen.logger()
    
    @pytest.mark.sanity
    @pytest.mark.regression
    def test_contact_details(self, setup):
        self.logger.info("*** Test_004_Edit_Contact_Details ***")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.lp = loginpage(self.driver)
        self.lp.setusername(self.username)
        self.lp.setpassword(self.password)
        self.lp.click_login()
        
        self.logger.info("*** Succesfully logged ***")
        self.logger.info("*** Started Edit Contact Details Test ***")
        self.opencategory = MyInfo(self.driver)
        self.opencategory.ClickOnMyInfo()
        self.opencategory.ClickOnContactDetails()
        self.editcontact = ContactDetails(self.driver)
        
        # Contact Details
        self.logger.info("*** Modifying Contact Details ***")
        self.editcontact.ClickOnEdit()
        self.editcontact.SetAddressStreet1("Piata Unirii 15, Nasaud")
        self.editcontact.SetAddressStreet2("Strada Unirii 20, Zalau")
        self.editcontact.SetCity("Oradea")
        self.editcontact.SetProvince("Bihor")
        self.editcontact.SetCountry("RO")
        self.editcontact.SetHomeTelephone("257 356 226")
        self.editcontact.SetMobileNr("0755555555")
        self.editcontact.SetWorkPhone("0744444444")
        self.editcontact.SetWorkMail("thisismyworkemail@orangehrm.com")
        self.editcontact.SetOtherMail("thisismyotheremail@gmail.com")
        self.editcontact.ClickOnEdit()
        self.msg1 = self.driver.find_element_by_css_selector("#contact-details > div:nth-child(2) > div.inner > div").text
        
        self.logger.info("*** Saving info ***")
        self.logger.info("*** Contact Details Validation Started ***")
        
        if self.msg1 == "Successfully Saved":
            self.logger.info("*** Edit Contact Details Test Passed ***")
            assert True
        else:
            self.driver.save_screenshot("..\\Screenshots\\" + "test_contact_details.png")
            self.logger.error("*** Edit Contact Details Test Failed ***")
            assert False
            
        self.driver.close()
        self.logger.info("*** Ending Contact Details test ***")
        
        
        