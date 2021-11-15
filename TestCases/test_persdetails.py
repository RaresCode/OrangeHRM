from PageObjects.LoginPage import loginpage
from PageObjects.PersonalDetails import PersonalDetails
from PageObjects.MyInfo import MyInfo
from utilities.customlogger import logGen
from utilities.ReadProperties import ReadConfig
import pytest

class Test_003_Edit_Personal_Details():
    baseurl = ReadConfig.GetAplicationUrl()
    username = ReadConfig.getusername()
    password = ReadConfig.getpassword()
    logger = logGen.logger()
    
    @pytest.mark.sanity
    @pytest.mark.regression
    def test_Personal_Details(self, setup):
        self.logger.info("*** Test_003_Edit_Personal_Details ***")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.lp = loginpage(self.driver)
        self.lp.setusername(self.username)
        self.lp.setpassword(self.password)
        self.lp.click_login()

        self.logger.info("*** Succesfully logged ***")
        self.logger.info("*** Started Edit Personal Details Test ***")
        self.opencategory = MyInfo(self.driver)
        self.opencategory.ClickOnMyInfo()
        self.editpersdetails = PersonalDetails(self.driver)
        self.editpersdetails.ClickOnEdit()
        self.logger.info("*** Modifying Personal Details ***")

        # Personal Details
        self.editpersdetails.SetFirstName("Andrei")
        self.editpersdetails.SetMiddleName("Ionut")
        self.editpersdetails.SetLastName("Popescu")
        self.editpersdetails.SetEmployeeID("5467")
        self.editpersdetails.SetDriverLicenceNr("123523")
        self.editpersdetails.SetLicenceExpireDate("2027-02-27")
        self.editpersdetails.SetDob("2001-01-29")
        self.editpersdetails.SetSSN("405")
        self.editpersdetails.SetOtherID("31321")
        self.editpersdetails.SetSIN("332")
        self.editpersdetails.SetGender("Male")
        self.editpersdetails.SetNationality()
        self.editpersdetails.SetMaritalStatus("Single")
        self.editpersdetails.SetNickName("Andrew")
        self.editpersdetails.SetMilitaryService("Active Guard")
        self.editpersdetails.SetSmoker("Yes")
        self.editpersdetails.ClickOnEdit()
        self.msg1 = self.driver.find_element_by_css_selector("#pdMainContainer > div.inner > div").text

        # Custom Fields
        self.editpersdetails.EditBloodbtn()
        self.editpersdetails.SetBloodType("A+")
        self.editpersdetails.EditBloodbtn()

        self.logger.info("*** Saving info ***")
        self.logger.info("*** Personal Details Validation Started ***")

        # Verifying if the details have been modified
        self.msg2 = self.driver.find_element_by_css_selector("#employee-details > div.single > div.inner > div").text

        if self.msg1 == "Successfully Saved" and self.msg2 == "Successfully Updated":
            self.logger.info("*** Edit Personal Details Test Passed ***")
            assert True
        elif self.msg1 != "Successfully Saved" and self.msg2 == "Successfully Updated":
            self.logger.error("*** Edit Personal Details Test Failed ***")
            self.logger.error("*** Personal Details Category Failed but Custom Fields Passed ***")
            self.driver.save_screenshot("..\\Screenshots\\" + "test_personal_details.png")
            assert False
        elif self.msg1 == "Successfully Saved" and self.msg2 != "Successfully Updated":
            self.logger.error("*** Edit Personal Details Test Failed ***")
            self.logger.error("*** Personal Details Category Passed but Custom Fields Failed ***")
            self.driver.save_screenshot("..\\Screenshots\\" + "test_personal_details.png")
            assert False
        else:
            self.driver.save_screenshot("..\\Screenshots\\" + "test_personal_details.png")
            self.logger.error("*** Edit Personal Details Test Failed ***")
            assert False

        self.driver.close()
        self.logger.info("*** Ending Personal Details test ***")

