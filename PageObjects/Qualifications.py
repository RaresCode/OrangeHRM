from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class Qualifications():
    # Work Experience
    btnAddExp_id = "addWorkExperience"
    txtExpCompany_id = "experience_employer"
    txtExpJobTitle_id = "experience_jobtitle"
    txtExpFromDate_id = "experience_from_date"
    txtExpToDate_id = "experience_to_date"
    txtExpComment_id = "experience_comments"
    btnSaveExp_id = "btnWorkExpSave"
    btnCancelExp_id = "btnWorkExpCancel"
    cbSelectAllExp_id = "workCheckAll"
    btnDeleteExp_id = "delWorkExperience"
    
    # Education
    btnAddEducation_id = "addEducation"
    drpEducationLevel_id = "education_code"
    txtEducationInstitute_id = "education_institute"
    txtEducationMajor_id = "education_major"
    txtEducationYear_id = "education_year"
    txtEducationGPA_id = "education_gpa"
    txtEducationStartDate_id = "education_start_date"
    txtEducationEndDate_id = "education_end_date"
    btnSaveEducation_id = "btnEducationSave"
    btnCancelEducation_id = "btnEducationCancel"
    btnDeleteEducation_id = "delEducation"
    cbSelectAllEducation_id = "educationCheckAll"
    
    # Skills
    btnAddSkills_id = "addSkill"
    drpSelectSkill_id = "skill_code"
    txtSkillYearsOfExp_id = "skill_years_of_exp"
    txtSkillComment_id = "skill_comments"
    btnSaveSkill_id = "btnSkillSave"
    btnCancelSkill_id = "btnSkillCancel"
    btnDeleteSkills_id = "delSkill"
    cbSelectAllSkills_id = "skillCheckAll"
    
    # Languages
    btnAddLanguages_id = "addLanguage"
    drpSelectLanguage_id = "language_code"
    drpSelectLanguageFluency_id = "language_lang_type"
    drpSelectLanguageCompetency_id = "language_competency"
    txtLanguageComment_id = "language_comments"
    btnSaveLanguage_id = "btnLanguageSave"
    btnCancelLanguage_id = "btnLanguageCancel"
    cbSelectAllLanguages_id = "languageCheckAll"
    btnDeleteLanguages_id = "delLanguage"
    
    # License
    btnAddLicense_id = "addLicense"
    drpLicenseType_id = "license_code"
    txtLicenseNumber_id = "license_license_no"
    txtLicenseIssuedDate_id = "license_date"
    txtLicenseExpireDate_id = "license_renewal_date"
    btnSaveLicense_id = "btnLicenseSave"
    btnCancelLicense_id = "btnLicenseCancel"
    cbSelectAllLicences_id = "licenseCheckAll"
    btnDeleteLicences_id = "delLicense"
    
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
    
    # Work Experience
        
    def ClickOnAddExperience(self):
        self.WebDriverWait.until(EC.presence_of_element_located((By.ID , self.btnAddExp_id))).click()
        
    def SetExpCompany(self, Experience):
        self.WebDriverWait.until(EC.presence_of_element_located((By.ID , self.txtExpCompany_id))).send_keys(Experience)
    
    def SetJobTitle(self, JobTitle):
        self.driver.find_element_by_id(self.txtExpJobTitle_id).send_keys(JobTitle)
    
    def SetExpFromDate(self, Date):
        self.driver.find_element_by_id(self.txtExpFromDate_id).clear()
        self.driver.find_element_by_id(self.txtExpFromDate_id).send_keys(Date)
    
    def SetExpToDate(self, Date):
        self.driver.find_element_by_id(self.txtExpToDate_id).clear()
        self.driver.find_element_by_id(self.txtExpToDate_id).send_keys(Date)
    
    def SetExpComment(self, Comment):
        self.driver.find_element_by_id(self.txtExpComment_id).send_keys(Comment)
    
    def ClickOnSaveExp(self):
        self.driver.find_element_by_id(self.btnSaveExp_id).click()
    
    def ClickOnCancelExp(self):
        self.driver.find_element_by_id(self.btnCancelExp_id).click()
    
    def SelectAllExp(self):
        self.WebDriverWait.until(EC.presence_of_element_located((By.ID , self.cbSelectAllExp_id))).click()
    
    def ClickOnDeleteExp(self):
        self.driver.find_element_by_id(self.btnDeleteExp_id).click()
    
    # Education
    
    def ClickOnAddEducation(self):
        self.WebDriverWait.until(EC.presence_of_element_located((By.ID , self.btnAddEducation_id))).click()
    
    def SetEducationLevel(self, EducationLevel):
        self.WebDriverWait.until(EC.presence_of_element_located((By.ID , self.drpEducationLevel_id)))
        self.drp = Select(self.driver.find_element_by_id(self.drpEducationLevel_id))
        self.drp.select_by_value(EducationLevel)
    
    def SetEducationInstitute(self, Institute):
        self.driver.find_element_by_id(self.txtEducationInstitute_id).send_keys(Institute)
    
    def SetEducationMajor(self, Major):
        self.driver.find_element_by_id(self.txtEducationMajor_id).send_keys(Major)
    
    def SetEducationYear(self, Year):
        self.driver.find_element_by_id(self.txtEducationYear_id).send_keys(Year)
    
    def SetEducationGPA(self, Score):
        self.driver.find_element_by_id(self.txtEducationGPA_id).send_keys(Score)
    
    def SetEducationStartDate(self, Date):
        self.driver.find_element_by_id(self.txtEducationStartDate_id).clear()
        self.driver.find_element_by_id(self.txtEducationStartDate_id).send_keys(Date)
    
    def SetEducationEndDate(self, Date):
        self.driver.find_element_by_id(self.txtEducationEndDate_id).clear()
        self.driver.find_element_by_id(self.txtEducationEndDate_id).send_keys(Date)
    
    def ClickOnSaveEducation(self):
        self.driver.find_element_by_id(self.btnSaveEducation_id).click()
    
    def ClickOnCancelEducation(self):
        self.driver.find_element_by_id(self.btnCancelEducation_id).click()
    
    def SelectAllEducation(self):
        self.WebDriverWait.until(EC.presence_of_element_located((By.ID , self.cbSelectAllEducation_id))).click()
    
    def ClickOnDeleteEducation(self):
        self.driver.find_element_by_id(self.btnDeleteEducation_id).click()
        
    # Skills
    
    def ClickOnAddSkills(self):
        self.WebDriverWait.until(EC.presence_of_element_located((By.ID , self.btnAddSkills_id))).click()
    
    def SetSkill(self, Skill):
        self.WebDriverWait.until(EC.presence_of_element_located((By.ID , self.drpSelectSkill_id)))
        self.drp = Select(self.driver.find_element_by_id(self.drpSelectSkill_id))
        self.drp.select_by_value(Skill)

    def SetSkillYearOfExp(self, YearOfExp):
        self.driver.find_element_by_id(self.txtSkillYearsOfExp_id).send_keys(YearOfExp)
    
    def SetSkillComment(self, Comment):
        self.driver.find_element_by_id(self.txtSkillComment_id).send_keys(Comment)
    
    def ClickOnSaveSkill(self):
        self.driver.find_element_by_id(self.btnSaveSkill_id).click()
    
    def ClickOnCancelSkill(self):
        self.driver.find_element_by_id(self.btnCancelSkill_id).click()
    
    def SelectAllSkills(self):
        self.WebDriverWait.until(EC.presence_of_element_located((By.ID , self.cbSelectAllSkills_id))).click()
    
    def ClickOnDeleteSkills(self):
        self.driver.find_element_by_id(self.btnDeleteSkills_id).click()
    
    # Languages
    
    def ClickOnAddLanguages(self):
        self.WebDriverWait.until(EC.presence_of_element_located((By.ID , self.btnAddLanguages_id))).click()
    
    def SetLanguage(self, Language):
        self.WebDriverWait.until(EC.presence_of_element_located((By.ID , self.drpSelectLanguage_id)))
        self.drp = Select(self.driver.find_element_by_id(self.drpSelectLanguage_id))
        self.drp.select_by_value(Language)
    
    def SetLanguageFluency(self, Fluency):
        self.drp = Select(self.driver.find_element_by_id(self.drpSelectLanguageFluency_id))
        self.drp.select_by_value(Fluency)
    
    def SetLanguageCompetency(self, Competency):
        self.drp = Select(self.driver.find_element_by_id(self.drpSelectLanguageCompetency_id))
        self.drp.select_by_value(Competency)
    
    def SetLanguageComment(self, Comment):
        self.driver.find_element_by_id(self.txtLanguageComment_id).send_keys(Comment)
    
    def ClickOnSaveLanguage(self):
        self.driver.find_element_by_id(self.btnSaveLanguage_id).click()
    
    def ClickOnCancelLanguage(self):
        self.driver.find_element_by_id(self.btnCancelLanguage_id).click()
    
    def SelectAllLanguages(self):
        self.WebDriverWait.until(EC.presence_of_element_located((By.ID , self.cbSelectAllLanguages_id))).click()
    
    def ClickOnDeleteLanguages(self):
        self.driver.find_element_by_id(self.btnDeleteLanguages_id).click()
    
    # License
    
    def ClickOnAddLicense(self):
        self.WebDriverWait.until(EC.presence_of_element_located((By.ID , self.btnAddLicense_id))).click()
    
    def SetLicenseType(self, LicenseType):
        self.WebDriverWait.until(EC.presence_of_element_located((By.ID , self.drpLicenseType_id)))
        self.drp = Select(self.driver.find_element_by_id(self.drpLicenseType_id))
        self.drp.select_by_value(LicenseType)
    
    def SetLicenseNumber(self, Number):
        self.driver.find_element_by_id(self.txtLicenseNumber_id).send_keys(Number)
    
    def SetLicenseIssuedDate(self, Date):
        self.driver.find_element_by_id(self.txtLicenseIssuedDate_id).clear()
        self.driver.find_element_by_id(self.txtLicenseIssuedDate_id).send_keys(Date)
    
    def SetLicenseExpireDate(self, Date):
        self.driver.find_element_by_id(self.txtLicenseExpireDate_id).clear()
        self.driver.find_element_by_id(self.txtLicenseExpireDate_id).send_keys(Date)
    
    def ClickOnSaveLicense(self):
        self.driver.find_element_by_id(self.btnSaveLicense_id).click()
    
    def ClickOnCancelLicense(self):
        self.driver.find_element_by_id(self.btnCancelLicense_id).click()
    
    def SelectAllLicenses(self):
        self.WebDriverWait.until(EC.presence_of_element_located((By.ID , self.cbSelectAllLicences_id))).click()
    
    def ClickOnDeleteLicenses(self):
        self.driver.find_element_by_id(self.btnDeleteLicences_id).click()
    
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
    
    