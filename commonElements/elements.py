from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

class elements:
    def __init__(self, driver):
        self.driver = driver

    def wait(self, waitTime = 1):
        return WebDriverWait(self.driver, waitTime)

    def getElement(self, locator):
        return self.wait().until(
            EC.presence_of_element_located(locator)
        )

    def getElementText(self, locator):
        return self.getElement(locator).text
    
    def getElementHref(self, locator):
        return self.getElement(locator).get_attribute('href')

    def clickElement(self, locator):
        self.getElement(locator).click()
    
    def type(self, locator, value):
        targetElement = self.getElement(locator)
        targetElement.clear()
        targetElement.send_keys(value)
    
    def select(self, locator, value):
        targetElement = self.getElement(locator)
        select = Select(targetElement)
        select.select_by_visible_text(value)
    
    def selectByValue(self, locator, value):
        targetElement = self.getElement(locator)
        select = Select(targetElement)
        select.select_by_value(value)

    def validateElementText(self, locator, expectedText):
        targetElement = self.getElementText(locator)
        assert targetElement == expectedText, f"\nExpected text to be '{expectedText}' but got '{targetElement}'"
        print("\nSucessful validated, text match!")

    def validateElementIsChecked(self, element):
        assert element.is_selected(), "\nValidation failed, element isn't checked!"
        print("\nSucessful validated, element is checked!")
    
    def validateElementIsNotChecked(self, element):
        assert not element.is_selected(), "\nValidation failed, element is checked!"
        print("\nSucessful validated, element isn't checked!")
    
    def validateElementHref(self, locator, expectedHref):
        targetElement = self.getElementHref(locator)
        assert targetElement == expectedHref, f"\nExpected text to be '{expectedHref}' but got '{targetElement}'"
        print("\nSucessful validated, Href match!")
