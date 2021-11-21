from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class Memberships():
    # Memberships
    btnAddMembership_id = "btnAddMembershipDetail"
    drpMembershipType_id = "membership_membership"
    drpSubscriptionPaidBy_id = "membership_subscriptionPaidBy"
    txtSubscriptionAmount_id = "membership_subscriptionAmount"
    drpCurrencyType_id = "membership_currency"
    txtSubscriptionStartDate_id = "membership_subscriptionCommenceDate"
    txtSubscriptionEndDate_id = "membership_subscriptionRenewalDate"
    btnSaveMembership_id = "btnSaveMembership"
    btnCancelMembership_id = "btnCancel"
    cbSelectAllMemberships_id = "checkAllMem"
    btnDeleteMembership_id = "delMemsBtn"
    
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
    
    # Memberships
    def ClickOnAddMembership(self):
        self.WebDriverWait.until(EC.presence_of_element_located((By.ID , self.btnAddMembership_id))).click()
    
    def SetMembershipType(self, Type):
        self.WebDriverWait.until(EC.presence_of_element_located((By.ID , self.drpMembershipType_id)))
        self.drp = Select(self.driver.find_element_by_id(self.drpMembershipType_id))
        self.drp.select_by_value(Type)
    
    def SetSubscriptionPaidBy(self, PaidBy):
        self.drp = Select(self.driver.find_element_by_id(self.drpSubscriptionPaidBy_id))
        self.drp.select_by_value(PaidBy)
    
    def SetSubscriptionAmount(self, Amount):
        self.driver.find_element_by_id(self.txtSubscriptionAmount_id).send_keys(Amount)
    
    def SetCurrencyType(self, Currency):
        self.drp = Select(self.driver.find_element_by_id(self.drpCurrencyType_id))
        self.drp.select_by_value(Currency)
    
    def SetSubscriptionStartDate(self, Date):
        self.driver.find_element_by_id(self.txtSubscriptionStartDate_id).clear()
        self.driver.find_element_by_id(self.txtSubscriptionStartDate_id).send_keys(Date)
        
    def SetSubscriptionEndDate(self, Date):
        self.driver.find_element_by_id(self.txtSubscriptionEndDate_id).clear()
        self.driver.find_element_by_id(self.txtSubscriptionEndDate_id).send_keys(Date)
    
    def ClickOnSaveMembership(self):
        self.driver.find_element_by_id(self.btnSaveMembership_id).click()
    
    def ClickOnCancelMembership(self):
        self.driver.find_element_by_id(self.btnCancelMembership_id).click()
    
    def SelectAllMemberships(self):
        self.WebDriverWait.until(EC.presence_of_element_located((By.ID , self.cbSelectAllMemberships_id))).click()
    
    def ClickOnDeleteMemberships(self):
        self.driver.find_element_by_id(self.btnDeleteMembership_id).click()
    
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
    
    
    
    
    
    

    