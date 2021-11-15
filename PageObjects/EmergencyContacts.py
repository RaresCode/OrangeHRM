
class EmergencyContacts():
    # Emergency Contacts
    btnAddEmergencyContact_id = "btnAddContact"
    txtName_id = "emgcontacts_name"
    txtRelationship_id = "emgcontacts_relationship"
    txtHomeTelephone_id = "emgcontacts_homePhone"
    txtMobile_id = "emgcontacts_mobilePhone"
    txtWorkTelephone_id = "emgcontacts_workPhone"
    btnSaveEmergencyContact_id = "btnSaveEContact"
    btnCancelEmergencyContact_id = "btnCancel"
    cbSelectAllEmergencyContacts_id = "checkAll"
    btnDeleteEmergencyContact_class = "delete"
    
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
        
    # Emergency Contacts
    def ClickOnAddEmergencyContact(self):
        self.driver.find_element_by_id(self.btnAddEmergencyContact_id).click()
        
    def SetName(self, Name):
        self.driver.find_element_by_id(self.txtName_id).send_keys(Name)
    
    def SetRelationship(self, Relationship):
        self.driver.find_element_by_id(self.txtRelationship_id).send_keys(Relationship)
    
    def SetHomeTelephone(self, HomeTelephoneNr):
        self.driver.find_element_by_id(self.txtHomeTelephone_id).send_keys(HomeTelephoneNr)
    
    def SetMobile(self, MobileNr):
        self.driver.find_element_by_id(self.txtMobile_id).send_keys(MobileNr)
    
    def SetWorkTelephone(self, WorkTelephoneNr):
        self.driver.find_element_by_id(self.txtWorkTelephone_id).send_keys(WorkTelephoneNr)
    
    def ClickOnSaveEmergencyContact(self):
        self.driver.find_element_by_id(self.btnSaveEmergencyContact_id).click()
        
    def ClickOnCancelEmergencyContact(self):
        self.driver.find_element_by_id(self.btnCancelEmergencyContact_id).click()
    
    def SelectAllEmergencyContacts(self):
        self.driver.find_element_by_id(self.cbSelectAllEmergencyContacts_id).click()
    
    def ClickOnDeleteEmergencyContact(self):
        self.driver.find_element_by_class_name(self.btnDeleteEmergencyContact_class).click()
    
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
    

