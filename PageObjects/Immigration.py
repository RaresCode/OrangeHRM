from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class Immigration():
    # Immigration
    btnAddImmigrationRecord_id = "btnAdd"
    rdPassportDocumentType_id = "immigration_type_flag_1"
    rdVisaDocumentType_id = "immigration_type_flag_2"
    txtNumber_id = "immigration_number"
    txtIssuedDate_id = "immigration_passport_issue_date"
    txtExpiryDate_id = "immigration_passport_expire_date"
    txtEligibleStatus_id = "immigration_i9_status"
    drpIssuedBy_id = "immigration_country"
    txtEligibleReviewDate_id = "immigration_i9_review_date"
    txtComments_id = "immigration_comments"
    btnSaveImmigrationRecord_id = "btnSave"
    btnCancelImmigrationRecord_id = "btnCancel"
    cbSelectAllImmigrations_id = "immigrationCheckAll"
    btnDeleteSelectedImmigrations_id = "btnDelete"
    
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
    
    # Immigration
    def ClickOnAddImmigrationRecord(self):
        self.WebDriverWait.until(EC.presence_of_element_located((By.ID , self.btnAddImmigrationRecord_id))).click()
        
    def SetDocumentType(self, DocumentType):
        self.WebDriverWait.until(EC.presence_of_element_located((By.ID , self.rdPassportDocumentType_id)))
        if DocumentType.lower() == "passport":
            self.driver.find_element_by_id(self.rdPassportDocumentType_id).click()
        elif DocumentType.lower() == "visa":
            self.driver.find_element_by_id(self.rdVisaDocumentType_id).click()
        else:
            self.driver.find_element_by_id(self.rdPassportDocumentType_id).click()
        
    def SetNumber(self, Number):
        self.driver.find_element_by_id(self.txtNumber_id).send_keys(Number)
    
    def SetIssuedDate(self, Date):
        self.driver.find_element_by_id(self.txtIssuedDate_id).clear()
        self.driver.find_element_by_id(self.txtIssuedDate_id).send_keys(Date)
    
    def SetExpireDate(self, Date):
        self.driver.find_element_by_id(self.txtExpiryDate_id).clear()
        self.driver.find_element_by_id(self.txtExpiryDate_id).send_keys(Date)
    
    def SetEligibleStatus(self, Status):
        self.driver.find_element_by_id(self.txtEligibleStatus_id).send_keys(Status)
    
    def SetIssuedBy(self, IssuedBy):
        self.drp = Select(self.driver.find_element_by_id(self.drpIssuedBy_id))
        self.drp.select_by_value(IssuedBy)
    
    def SetEligibleReviewDate(self, Date):
        self.driver.find_element_by_id(self.txtEligibleReviewDate_id).clear()
        self.driver.find_element_by_id(self.txtEligibleReviewDate_id).send_keys(Date)
    
    def SetComment(self, Comment):
        self.driver.find_element_by_id(self.txtComments_id).send_keys(Comment)
    
    def ClickOnSaveImmigrationRecord(self):
        self.driver.find_element_by_id(self.btnSaveImmigrationRecord_id).click()
    
    def ClickOnCancelImmigrationRecord(self):
        self.driver.find_element_by_id(self.btnCancelImmigrationRecord_id).click()
    
    def SelectAllImmigrationRecords(self):
        self.WebDriverWait.until(EC.presence_of_element_located((By.ID , self.cbSelectAllImmigrations_id))).click()
    
    def ClickOnDeleteAllImmigrations(self):
        self.driver.find_element_by_id(self.btnDeleteSelectedImmigrations_id).click()
    
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
    
    