
class Photograph():
    btnFilePath_id = "photofile"
    btnUploadFile_id = "btnSave"
    btnDeleteFile_id = "btnDelete"
    btnConfirmFileDeletion_id = "btnYes"
    btnCancelFileDeletion_id = "btnNo"

    def __init__(self, driver):
        self.driver = driver
        
    def SetFilePath(self, path):
        self.driver.find_element_by_id(self.btnFilePath_id).send_keys(path)
    
    def ClickOnUpload(self):
        self.driver.find_element_by_id(self.btnUploadFile_id).click()
    
    def ClickOnDelete(self):
        self.driver.find_element_by_id(self.btnDeleteFile_id).click()
    
    def ClickOnConfirmDeletion(self):
        self.driver.find_element_by_id(self.btnConfirmFileDeletion_id).click()
    
    def ClickOnCancelDeletion(self):
        self.driver.find_element_by_id(self.btnCancelFileDeletion_id).click()
    
    