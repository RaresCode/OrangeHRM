from PageObjects.LoginPage import loginpage
from utilities.customlogger import logGen
from utilities.ReadProperties import ReadConfig
import pytest

class Test_001_Login():
    baseurl = ReadConfig.GetAplicationUrl()
    username = ReadConfig.getusername()
    password = ReadConfig.getpassword()
    logger = logGen.logger()
    expected_url = "https://opensource-demo.orangehrmlive.com/index.php/dashboard"

    @pytest.mark.regression
    def test_pagetitle(self, setup):
        self.logger.info("*** Started Page Title Test ***")
        self.driver = setup
        self.logger.info("*** Opening the url ***")
        self.driver.get(self.baseurl)

        if self.driver.title == "OrangeHRM":
            self.logger.info("*** Page Title Test Passed ***")
            self.driver.close()
            assert True
        else:
            self.logger.error("*** Page Title Test Failed")
            self.driver.close()
            assert False

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_login(self, setup):
        self.logger.info("*** Started Login Test ***")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.lp = loginpage(self.driver)
        self.lp.setusername(self.username)
        self.lp.setpassword(self.password)
        self.lp.click_login()
        if self.driver.current_url == self.expected_url:
            self.logger.info("*** Login Test Passed ***")
            self.driver.close()
            assert True
        else:
            self.logger.error("*** Login Test Failed ***")
            self.driver.save_screenshot("..\\Screenshots\\" + "test_Login.png")
            self.driver.close()
            assert False