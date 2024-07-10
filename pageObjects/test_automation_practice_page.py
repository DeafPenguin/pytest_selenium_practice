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
        self.openCartLink = (By.CSS_SELECTOR, ".post-body > a:nth-child(21)")
        self.orangeHRMLink = (By.CSS_SELECTOR, ".post-body > a:nth-child(22)")
        self.submitButton = (By.ID, "FSsubmit")

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

        # Datepicker locators
        self.calendar = (By.ID, "datepicker")

        # Iframe locators
        self.iframeTapLocator = (By.CSS_SELECTOR, "iframe[id*=frame]")
        self.iframeHeaderError = (By.CSS_SELECTOR, "body > div > div:nth-child(1)")
        self.iframeErrorDescribe = (By.CSS_SELECTOR, "body > div > div:nth-child(3)")

    def load(self):
        self.driver.get(self.pageUrl)

    def fillUserForm(self, userName, userEmail, userPhone, userAddress):
        self.type(self.nameInput, userName)
        self.type(self.emailInput, userEmail)
        self.type(self.phoneInput, userPhone)
        self.type(self.addressInput, userAddress)

    def selectFemaleGenderOnForm(self):
        self.clickElement(self.femaleGenderRadioButton)
    
    def selectMaleGenderOnForm(self):
        self.clickElement(self.maleGenderRadioButton)

    def selectCountry(self, userCountry):
        self.select(self.countryDropdown, userCountry)

    def setColor(self, color):
        self.select(self.colors, color)

    def selectDayOfListByPosition(self, position):
        commonElements.clickOnListElementByPosition(self, self.daysList, self.divClass, position)
    
    def selectDayOfListByValue(self, value):
        commonElements.clickOnListElementByValue(self, self.daysList, self.divClass, value)
    
    def selectProductOnPaginationTableByRowNumber(self, row):
        element = self.getCellByColumnName(self.paginationTable, "Select", row)
        targetElement = element.find_element(By.CSS_SELECTOR, "input[type=checkbox]")
        targetElement.click()
    
    def selectProductByName(self, productName):
        # Get target rows
        rows = self.getRowsByColumnValue(self.paginationTable, "Name", productName)

        # Get target cells from rows
        cells = self.getCellsFromRowsByPosition(rows, 3)

        # Click on the select cells
        self.clickMultipleCellsWithinElement(cells, "input")

    def selectDateOnForm(self, targetDate):
        self.selectDate(self.calendar, targetDate)

    def validateHeader(self):
        self.validateElementText(self.headerInner, "Automation Testing Practice")

    def validateFormLinks(self):
        self.validateElementLink(self.openCartLink, 'https://demo.opencart.com/')
        self.validateElementLink(self.orangeHRMLink, 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')

    def validateWeekdayIsChecked(self, value):
        targetElement = commonElements.getListElementByValue(self, self.daysList, self.divClass, value)

        targetCheckbox = targetElement.find_element(By.CSS_SELECTOR, 'input')

        self.validateElementIsChecked(targetCheckbox)
    
    def validateWeekdayIsNotChecked(self, value):
        targetElement = commonElements.getListElementByValue(self, self.daysList, self.divClass, value)

        targetCheckbox = targetElement.find_element(By.CSS_SELECTOR, 'input')

        self.validateElementIsNotChecked(targetCheckbox)
    
    def validateBookAuthor(self, bookName, author):
        # Get target rows
        rows = self.getRowsByColumnValue(self.webTable, "BookName", bookName)

        # Get target cells from rows
        cells = self.getCellsFromRowsByPosition(rows, 1)

        for cell in cells:
            assert cell.text == author, f"Expected text to be '{author}' but got '{cell.text}'"
            print("\nSucessful validated, Book and Author match!")

    def validateBookSubject(self, bookName, subject):
        # Get target rows
        rows = self.getRowsByColumnValue(self.webTable, "BookName", bookName)

        # Get target cells from rows
        cells = self.getCellsFromRowsByPosition(rows, 2)

        for cell in cells:
            assert cell.text == subject, f"Expected text to be '{subject}' but got '{cell.text}'"
            print("\nSucessful validated, Book and Subject match!")
    
    def validateBookPrice(self, bookName, price):
        # Get target rows
        rows = self.getRowsByColumnValue(self.webTable, "BookName", bookName)

        # Get target cells from rows
        cells = self.getCellsFromRowsByPosition(rows, 3)

        for cell in cells:
            assert cell.text == price, f"Expected text to be '{price}' but got '{cell.text}'"
            print("\nSucessful validated, Book and Price match!")
    
    def validateProductPrice(self, product, price):
        # Get target rows
        rows = self.getRowsByColumnValue(self.paginationTable, "Name", product)

        # Get target cells from rows
        cells = self.getCellsFromRowsByPosition(rows, 2)

        for cell in cells:
            assert cell.text == price, f"Expected text to be '{price}' but got '{cell.text}'"
            print("\nSucessful validated, Product and Price match!")
    
    def submitFormAndValidate(self):
        expectedContentLabel = "An error has occurred"
        expectedContentDescription = "The result storage capacity has been reached for this form. Your result was not created. Please contact the form owner."

        # Switch to Iframe
        self.switchToIframe(self.iframeTapLocator)

        # Submit form
        self.clickElement(self.submitButton)

        # Validate error label
        contentLabel = self.getElement(self.iframeHeaderError).text
        assert contentLabel == expectedContentLabel, f"\nIframe content should be {expectedContentLabel}, but instead is {contentLabel}."
        print(f"\nIframe content validated successfully: '{expectedContentLabel}'")

        # Validate error description
        contentDescription = self.getElement(self.iframeErrorDescribe).text
        assert contentDescription == expectedContentDescription, f"\nIframe content should be {expectedContentDescription}, but instead is {contentDescription}."
        print(f"\nIframe content validated successfully: '{expectedContentDescription}'")

        # Switch back to default
        self.switchToDefaultContent()