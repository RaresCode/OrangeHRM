from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class ContactDetails():
    # Contact Details
    btnEditDetails_id = "btnSave"
    txtAddressStreet1_id = "contact_street1"
    txtAddressStreet2_id = "contact_street2"
    txtCity_id = "contact_city"
    txtProvince_id = "contact_province"
    txtZIP_id = "contact_emp_zipcode"
    drpCountry_id = "contact_country"
    txtHomeTelephone_id = "contact_emp_hm_telephone"
    txtMobile_id = "contact_emp_mobile"
    txtWorkPhone_id = "contact_emp_work_telephone"
    txtWorkMail_id = "contact_emp_work_email"
    txtOtherMail_id = "contact_emp_oth_email"
    
    # Attachment
    btnAddAttachments_id = "btnAddAttachment"
    btnDeleteAttachments_id = "btnDeleteAttachment"
    cbSelectAllAttachments_id = "attachmentsCheckAll"
    btnFilePath_id = "ufile"
    txtAttachmentComment_id = "txtAttDesc"
    btnUploadFile_id = "btnSaveAttachment"
    btnCancelUpload_id = "cancelButton"
    
    
    def __init__(self, driver):
        self.driver = driver
        self.WebDriverWait = WebDriverWait(self.driver, 10)
    
    # Contact Details
    def ClickOnEdit(self):
        self.WebDriverWait.until(EC.presence_of_element_located((By.ID , self.btnEditDetails_id))).click()
        
    def SetAddressStreet1(self, Address):
        self.driver.find_element_by_id(self.txtAddressStreet1_id).clear()
        self.driver.find_element_by_id(self.txtAddressStreet1_id).send_keys(Address)
    
    def SetAddressStreet2(self, Address):
        self.driver.find_element_by_id(self.txtAddressStreet2_id).clear()
        self.driver.find_element_by_id(self.txtAddressStreet2_id).send_keys(Address)
        
    def SetCity(self, City):
        self.driver.find_element_by_id(self.txtCity_id).clear()
        self.driver.find_element_by_id(self.txtCity_id).send_keys(City)
    
    def SetProvince(self, Province):
        self.driver.find_element_by_id(self.txtProvince_id).clear()
        self.driver.find_element_by_id(self.txtProvince_id).send_keys(Province)
    
    def SetZIP(self, ZIP):
        self.driver.find_element_by_id(self.txtZIP_id).clear()
        self.driver.find_element_by_id(self.txtZIP_id).send_keys(ZIP)
        
    def SetCountry(self, Country):
        drp = Select(self.driver.find_element_by_id(self.drpCountry_id))    
        drp.select_by_value(Country)
        
    def SetHomeTelephone(self, HomeNr):
        self.driver.find_element_by_id(self.txtHomeTelephone_id).clear()
        self.driver.find_element_by_id(self.txtHomeTelephone_id).send_keys(HomeNr)
    
    def SetMobileNr(self, MobileNr):
        self.driver.find_element_by_id(self.txtMobile_id).clear()
        self.driver.find_element_by_id(self.txtMobile_id).send_keys(MobileNr)
    
    def SetWorkPhone(self, WorkNr):
        self.driver.find_element_by_id(self.txtWorkPhone_id).clear()
        self.driver.find_element_by_id(self.txtWorkPhone_id).send_keys(WorkNr)
    
    def SetWorkMail(self, WorkMail):
        self.driver.find_element_by_id(self.txtWorkMail_id).clear()
        self.driver.find_element_by_id(self.txtWorkMail_id).send_keys(WorkMail)
    
    def SetOtherMail(self, OtherMail):
        self.driver.find_element_by_id(self.txtOtherMail_id).clear()
        self.driver.find_element_by_id(self.txtOtherMail_id).send_keys(OtherMail)
    
    # Attachment
    def ClickOnAddAttachment(self):
        self.WebDriverWait.until(EC.presence_of_element_located((By.ID , self.btnAddAttachments_id))).click()
    
    def ClickOnDeleteAttachments(self):
        self.driver.find_element_by_id(self.btnDeleteAttachments_id).click()
    
    def SelectAllAttachments(self):
        self.WebDriverWait.until(EC.presence_of_element_located((By.ID , self.cbSelectAllAttachments_id))).click()
    
    def ClickOnCancelUpload(self):
        self.driver.find_element_by_id(self.btnCancelUpload_id).click()
    
    def SetFilePath(self, Path):
        self.WebDriverWait.until(EC.presence_of_element_located((By.ID , self.btnFilePath_id))).send_keys(Path)
    
    def ClickOnUpload(self):
        self.driver.find_element_by_id(self.btnUploadFile_id).click()
        
    def SetAttachmentComment(self, Comment):
        self.driver.find_element_by_id(self.txtAttachmentComment_id).send_keys(Comment)