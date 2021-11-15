from selenium.webdriver.support.ui import Select

class Dependents():
    # Dependents
    btnAddDependent_id = "btnAddDependent"
    txtName_id = "dependent_name"
    drpRelationship_id = "dependent_relationshipType"
    txtDob_id = "dependent_dateOfBirth"
    btnSaveDependent_id = "btnSaveDependent"
    btnCancelDependent_id = "btnCancel"
    cbSelectAllDependents_id = "checkAll"
    btnDeleteSelectedDependents_id = "delDependentBtn"
    
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
    
    # Dependents
    def ClickOnAddDependent(self):
        self.driver.find_element_by_id(self.btnAddDependent_id).click()
        
    def SetName(self, Name):
        self.driver.find_element_by_id(self.txtName_id).send_keys(Name)
    
    def SetRelationship(self, Relationship):
        self.drp = Select(self.driver.find_element_by_id(self.drpRelationship_id))
        self.drp.select_by_value(Relationship)
    
    def SetDob(self, Dob):
        self.driver.find_element_by_id(self.txtDob_id).clear()
        self.driver.find_element_by_id(self.txtDob_id).send_keys(Dob)
    
    def ClickOnSaveDependent(self):
        self.driver.find_element_by_id(self.btnSaveDependent_id).click()
        
    def ClickOnCancelDependent(self):
        self.driver.find_element_by_id(self.btnCancelDependent_id).click()
    
    def SelectAllDependents(self):
        self.driver.find_element_by_id(self.cbSelectAllDependents_id).click()
    
    def ClickOnDeleteDependents(self):
        self.driver.find_element_by_id(self.btnDeleteSelectedDependents_id).click()
        
    # Attachment
    def ClickOnAddAttachment(self):
        self.driver.find_element_by_id(self.btnAddAttachments_id).click()
    
    def ClickOnDeleteAttachments(self):
        self.driver.find_element_by_id(self.btnDeleteAttachments_id).click()
    
    def SelectAllAttachments(self):
        self.driver.find_element_by_id(self.cbSelectAllAttachments_id).click()
    
    def ClickOnCancelUpload(self):
        self.driver.find_element_by_id(self.btnCancelUpload_id).click()
    
    def SetFilePath(self, Path):
        self.driver.find_element_by_id(self.btnFilePath_id).send_keys(Path)
    
    def ClickOnUpload(self):
        self.driver.find_element_by_id(self.btnUploadFile_id).click()
        
    def SetAttachmentComment(self, Comment):
        self.driver.find_element_by_id(self.txtAttachmentComment_id).send_keys(Comment)
    