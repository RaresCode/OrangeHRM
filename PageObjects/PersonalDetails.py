from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class PersonalDetails():
    # Personal Details
    btnEditDetails_id = "btnSave"
    txtFirstName_id = "personal_txtEmpFirstName"
    txtMiddleName_id = "personal_txtEmpMiddleName"
    txtLastName_id = "personal_txtEmpLastName"
    txtEmployeeid_id = "personal_txtEmployeeId"
    txtDriverLicenceNumber_id = "personal_txtLicenNo"
    txtSSNNumber_id = "personal_txtNICNo"
    txtOtherid_id = "personal_txtOtherID"
    txtLicenceExpireDate_name = "personal[txtLicExpDate]"
    txtSINNumber_id = "personal_txtSINNo"
    rdMaleGender_id = "personal_optGender_1"
    rdFemale_id = "personal_optGender_2"
    drpNationality_id = "personal_cmbNation"
    drpMaritalStatus_id = "personal_cmbMarital"
    txtDob_name = "personal[DOB]"
    txtNickName_id = "personal_txtEmpNickName"
    txtMilitaryService_id = "personal_txtMilitarySer"
    cbSmoker_id = "personal_chkSmokeFlag"
    
    # Custom Fields
    btnCustomFields_id = "btnEditCustom"
    drpBloodType_name = "custom1"
    
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
    
    # Personal Details
    def ClickOnEdit(self):
        self.WebDriverWait.until(EC.presence_of_element_located((By.ID , self.btnEditDetails_id))).click()
    
    def SetFirstName(self, fname):
        self.driver.find_element_by_id(self.txtFirstName_id).clear()
        self.driver.find_element_by_id(self.txtFirstName_id).send_keys(fname)
    
    def SetMiddleName(self, mdname):
        self.driver.find_element_by_id(self.txtMiddleName_id).clear()
        self.driver.find_element_by_id(self.txtMiddleName_id).send_keys(mdname)
    
    def SetLastName(self, lname):
        self.driver.find_element_by_id(self.txtLastName_id).clear()
        self.driver.find_element_by_id(self.txtLastName_id).send_keys(lname)
        
    def SetEmployeeID(self, ID):
        self.driver.find_element_by_id(self.txtEmployeeid_id).clear()
        self.driver.find_element_by_id(self.txtEmployeeid_id).send_keys(ID)
    
    def SetDriverLicenceNr(self, Number):
        self.driver.find_element_by_id(self.txtDriverLicenceNumber_id).clear()
        self.driver.find_element_by_id(self.txtDriverLicenceNumber_id).send_keys(Number)
    
    def SetSSN(self, Number):
        self.driver.find_element_by_id(self.txtSSNNumber_id).clear()
        self.driver.find_element_by_id(self.txtSSNNumber_id).send_keys(Number)
    
    def SetOtherID(self, ID):
        self.driver.find_element_by_id(self.txtOtherid_id).clear()
        self.driver.find_element_by_id(self.txtOtherid_id).send_keys(ID)
    
    def SetLicenceExpireDate(self, Date):
        self.driver.find_element_by_name(self.txtLicenceExpireDate_name).clear()
        self.driver.find_element_by_name(self.txtLicenceExpireDate_name).send_keys(Date)
    
    def SetSIN(self, Number):
        self.driver.find_element_by_id(self.txtSINNumber_id).clear()
        self.driver.find_element_by_id(self.txtSINNumber_id).send_keys(Number)
    
    def SetGender(self, gender):
        if gender.lower() == "male":
            self.driver.find_element_by_id(self.rdMaleGender_id).click()
        elif gender.lower() == "female":
            self.driver.find_element_by_id(self.rdFemale_id).click()
        else:
            self.driver.find_element_by_id(self.rdMaleGender_id).click()
    
    def SetNationality(self):
        drp = Select(self.driver.find_element_by_id(self.drpNationality_id))
        drp.select_by_value("145")
    
    def SetMaritalStatus(self, Status):
        drp = Select(self.driver.find_element_by_id(self.drpMaritalStatus_id))
        drp.select_by_value(Status)
    
    def SetDob(self, Date):
        self.driver.find_element_by_name(self.txtDob_name).clear()
        self.driver.find_element_by_name(self.txtDob_name).send_keys(Date)
    
    def SetNickName(self, NickName):
        self.driver.find_element_by_id(self.txtNickName_id).clear()
        self.driver.find_element_by_id(self.txtNickName_id).send_keys(NickName)
    
    def SetMilitaryService(self, Number):
        self.driver.find_element_by_id(self.txtMilitaryService_id).clear()
        self.driver.find_element_by_id(self.txtMilitaryService_id).send_keys(Number)
        
    def SetSmoker(self, answer):
        if answer.lower() == "yes":
            self.driver.find_element_by_id(self.cbSmoker_id).click()
    
    # Custom Fields
    def EditBloodbtn(self):
        self.WebDriverWait.until(EC.presence_of_element_located((By.ID , self.btnCustomFields_id))).click()
    
    def SetBloodType(self, Type):
        self.drp = Select(self.driver.find_element_by_name(self.drpBloodType_name))
        self.drp.select_by_value(Type)
    
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
    
    