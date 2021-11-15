from PageObjects.LoginPage import loginpage
from utilities.customlogger import logGen
from utilities.ReadProperties import ReadConfig
import pytest
import openpyxl

class Test_002_DDT_Login():
    baseurl = ReadConfig.GetAplicationUrl()
    logger = logGen.logger()
    userandpass = "..\\TestData\\username&password.xlsx"
    expected_url = "https://opensource-demo.orangehrmlive.com/index.php/dashboard"
    
    @pytest.mark.regression
    def test_login_ddt(self, setup):
        self.logger.info("*** Started Test_002_DDT_Login ***")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.lp = loginpage(self.driver)
        self.lst_status = []
        self.accounts_tested = 1
        self.workbook = openpyxl.load_workbook(self.userandpass)
        self.sheet = self.workbook.active
        self.maxrow = self.sheet.iter_rows(min_row=2, min_col=1, max_col=3)
        for a,b,c in self.maxrow:
            self.accounts_tested += 1
            self.excel_username = a.value
            self.excel_password = b.value
            self.login_outcome = c.value
            self.lp.setusername(self.excel_username)
            self.lp.setpassword(self.excel_password)
            self.lp.click_login()
            if self.driver.current_url == self.expected_url:
                if self.login_outcome == "Login Passed":
                    self.sheet["D" + str(self.accounts_tested)]= "As Expected"
                    self.logger.info("*** Login Passed ***")
                    self.lst_status.append("Passed")
                    self.driver.get(self.lp.link_logout)
                elif self.login_outcome == "Login Failed":
                    self.sheet["D" + str(self.accounts_tested)]= "Login Passed"
                    self.logger.info("*** Login Failed ***")
                    self.lst_status.append("Failed")
                    self.driver.get(self.lp.link_logout)
            elif self.driver.current_url != self.expected_url:
                if self.login_outcome == "Login Passed":
                    self.sheet["D" + str(self.accounts_tested)]= "Login Failed"
                    self.logger.info("*** Login Failed ***")
                    self.lst_status.append("Failed")
                    self.driver.get(self.lp.link_logout)
                elif self.login_outcome == "Login Failed":
                    self.sheet["D" + str(self.accounts_tested)]= "As Expected"
                    self.logger.info("*** Login Passed ***")
                    self.lst_status.append("Passed")
                    self.driver.get(self.lp.link_logout)
                    
        self.workbook.save(self.userandpass)
        self.workbook.close()
        self.driver.close()
        
        print(self.lst_status)
        if "Failed" not in self.lst_status:
            self.logger.info("DDT Test Passed")
            assert True
        else:
            self.logger.info("DDT Test Failed")
            assert False
        
        self.logger.info("*** End of DDT Testing ***")
        self.logger.info("*** Completed Test_002_DDT_Login ***")
