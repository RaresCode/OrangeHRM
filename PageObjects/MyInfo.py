from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class MyInfo():
    linkMyInfo_id = "menu_pim_viewMyDetails"
    linkPhotoChange_id = "empPic"
    linkContactDetails_link = "Contact Details"
    linkEmergencyContacts_link = "Emergency Contacts"
    linkDependents_link = "Dependents"
    linkImmigration_link = "Immigration"
    linkJob_link = "Job"
    linkSalary_link = "Salary"
    linkTaxExemptions_link = "Tax Exemptions"
    linkReportto_link = "Report-to"
    linkQualitifactions_link = "Qualifications"
    linkMemberships_link = "Memberships"
    
    def __init__(self, driver):
        self.driver = driver
        self.WebDriverWait = WebDriverWait(self.driver, 10)
    
    def ClickOnMyInfo(self):
        self.WebDriverWait.until(EC.presence_of_element_located((By.ID , self.linkMyInfo_id))).click()
    
    def ClickOnPhotoChange(self):
        self.WebDriverWait.until(EC.presence_of_element_located((By.ID , self.linkPhotoChange_id))).click()
    
    def ClickOnContactDetails(self):
        self.WebDriverWait.until(EC.presence_of_element_located((By.LINK_TEXT , self.linkContactDetails_link))).click()
        
    def ClickOnEmergencyContacts(self):
        self.WebDriverWait.until(EC.presence_of_element_located((By.LINK_TEXT , self.linkEmergencyContacts_link))).click()
    
    def ClickOnDependents(self):
        self.WebDriverWait.until(EC.presence_of_element_located((By.LINK_TEXT , self.linkDependents_link))).click()
        
    def ClickOnImmigration(self):
        self.WebDriverWait.until(EC.presence_of_element_located((By.LINK_TEXT , self.linkImmigration_link))).click()
    
    def ClickOnJob(self):
        self.WebDriverWait.until(EC.presence_of_element_located((By.LINK_TEXT , self.linkJob_link))).click()

    def ClickOnSalary(self):
        self.WebDriverWait.until(EC.presence_of_element_located((By.LINK_TEXT , self.linkSalary_link))).click()
    
    def ClickOnTaxExemptions(self):
        self.WebDriverWait.until(EC.presence_of_element_located((By.LINK_TEXT , self.linkTaxExemptions_link))).click()
        
    def ClickOnReportTo(self):
        self.WebDriverWait.until(EC.presence_of_element_located((By.LINK_TEXT , self.linkReportto_link))).click()
    
    def ClickOnQualifications(self):
        self.WebDriverWait.until(EC.presence_of_element_located((By.LINK_TEXT , self.linkQualitifactions_link))).click()
    
    def ClickOnMembership(self):
        self.WebDriverWait.until(EC.presence_of_element_located((By.LINK_TEXT , self.linkMemberships_link))).click()