from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class Photograph():
    btnFilePath_id = "photofile"
    btnUploadFile_id = "btnSave"
    btnDeleteFile_id = "btnDelete"
    btnConfirmFileDeletion_id = "btnYes"
    btnCancelFileDeletion_id = "btnNo"

    def __init__(self, driver):
        self.driver = driver
        self.WebDriverWait = WebDriverWait(self.driver, 10)
        
    def SetFilePath(self, path):
        self.WebDriverWait.until(EC.presence_of_element_located((By.ID , self.btnFilePath_id))).send_keys(path)
    
    def ClickOnUpload(self):
        self.driver.find_element_by_id(self.btnUploadFile_id).click()
    
    def ClickOnDelete(self):
        self.driver.find_element_by_id(self.btnDeleteFile_id).click()
    
    def ClickOnConfirmDeletion(self):
        self.driver.find_element_by_id(self.btnConfirmFileDeletion_id).click()
    
    def ClickOnCancelDeletion(self):
        self.driver.find_element_by_id(self.btnCancelFileDeletion_id).click()
    
    