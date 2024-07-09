from commonElements.elements import elements
from selenium.webdriver.common.by import By

class datepickers(elements):
    def __init__(self, driver):
        self.driver = driver

        # DatePicker Locators
        self.dateFieldLocator = (By.ID, 'datepicker')
        self.datePickerLocator = (By.CLASS_NAME, 'ui-datepicker-calendar')
        self.datePickerTitle = (By.CLASS_NAME, 'ui-datepicker-title')
        self.datePickerMonthText = (By.CLASS_NAME, 'ui-datepicker-month')
        self.datePickerYearText = (By.CLASS_NAME, 'ui-datepicker-year')
        self.previousMonthButton = (By.CLASS_NAME, 'ui-datepicker-prev')
        self.nextMonthButton = (By.CLASS_NAME, 'ui-datepicker-next')
    
    monthsMap = {
        "01": "January",
        "02": "February",
        "03": "March",
        "04": "April",
        "05": "May",
        "06": "June",
        "07": "July",
        "08": "August",
        "09": "September",
        "10": "October",
        "11": "November",
        "12": "December",
    }

    def openDatepicker(self, dateFieldLocator):
        self.getElement(dateFieldLocator).click()

    def clickNextMonthButton(self):
        self.getElement(self.nextMonthButton).click()

    def clickPreviousMonthButton(self):
        self.getElement(self.previousMonthButton).click()

    def selectDay(self, day):
        # Select given day
        dayLocator = (By.XPATH, f"//a[text()='{int(day)}']")

        # Get day element
        dayElement = self.getElement(dayLocator)

        # Click in day element
        dayElement.click()
    
    def navigateToMonthYear(self, month, year):
        targetMonth = self.monthsMap[month]
        targetYear = year

        while True:
            currentMonth = self.getElement(self.datePickerMonthText).text
            currentYear = self.getElement(self.datePickerYearText).text
            
            # Navigates to current month and year
            if currentMonth == targetMonth and currentYear == targetYear:
                break
            elif int(currentYear) > int(targetYear) or (int(currentYear) == int(targetYear) and list(self.monthsMap.values()).index(currentMonth) > list(self.monthsMap.values()).index(targetMonth)):
                self.clickPreviousMonthButton()
            else:
                self.clickNextMonthButton()

    def selectDate(self, dateFieldLocator, date):
        month, day, year = date.split('/')

        # Click on datefield to open datepicker
        self.openDatepicker(dateFieldLocator)

        # Navigate to target month
        self.navigateToMonthYear(month, year)

        # Select target day
        self.selectDay(day)
