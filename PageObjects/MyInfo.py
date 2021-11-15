
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
    
    def ClickOnMyInfo(self):
        self.driver.find_element_by_id(self.linkMyInfo_id).click()
    
    def ClickOnPhotoChange(self):
        self.driver.find_element_by_id(self.linkPhotoChange_id).click()
    
    def ClickOnContactDetails(self):
        self.driver.find_element_by_link_text(self.linkContactDetails_link).click()
        
    def ClickOnEmergencyContacts(self):
        self.driver.find_element_by_link_text(self.linkEmergencyContacts_link).click()
    
    def ClickOnDependents(self):
        self.driver.find_element_by_link_text(self.linkDependents_link).click()
        
    def ClickOnImmigration(self):
        self.driver.find_element_by_link_text(self.linkImmigration_link).click()
    
    def ClickOnJob(self):
        self.driver.find_element_by_link_text(self.linkJob_link).click()

    def ClickOnSalary(self):
        self.driver.find_element_by_link_text(self.linkSalary_link).click()
    
    def ClickOnTaxExemptions(self):
        self.driver.find_element_by_link_text(self.linkTaxExemptions_link).click()
        
    def ClickOnReportTo(self):
        self.driver.find_element_by_link_text(self.linkReportto_link).click()
    
    def ClickOnQualifications(self):
        self.driver.find_element_by_link_text(self.linkQualitifactions_link).click()
    
    def ClickOnMembership(self):
        self.driver.find_element_by_link_text(self.linkMemberships_link).click()