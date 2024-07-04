from selenium.webdriver.common.by import By
from commonElements.commonElements import commonElements

class TestAutomationPracticePage(commonElements):
    def __init__(self, driver):
        super().__init__(driver)

        # PageUrl
        self.pageUrl = "https://testautomationpractice.blogspot.com/"

        # Locators
        self.headerInner = (By.ID, "header-inner")
        self.divClass = (By.CSS_SELECTOR, "div")
        self.daysList = (By.CSS_SELECTOR, ".post-body > div:nth-child(9)")

        # Form locators
        self.nameInput = (By.ID, "name")
        self.emailInput = (By.ID, "email")
        self.phoneInput = (By.ID, "phone")
        self.addressInput = (By.ID, "textarea")
        self.maleGenderRadioButton = (By.ID, "male")
        self.femaleGenderRadioButton = (By.ID, "female")
        self.countryDropdown = (By.ID, "country")
        self.colors = (By.ID, "colors")

        # Table locators
        self.webTable = (By.CSS_SELECTOR, '[name="BookTable"]')
        self.paginationTable = (By.ID, "productTable")

    def load(self):
        self.driver.get(self.pageUrl)

    def selectDayOfList(self, position):
        element = commonElements.getListElement(self, self.daysList, self.divClass, position)
        element.click()
    
    def selectProductOnPaginationTableByRowNumber(self, row):
        element = self.getCellByColumnName(self.paginationTable, "Select", row)
        targetElement = element.find_element(By.CSS_SELECTOR, "input[type=checkbox]")
        targetElement.click()