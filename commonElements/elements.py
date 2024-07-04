from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

class elements:
    def __init__(self, driver):
        self.driver = driver

    def getElement(self, locator):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(locator)
        )

    def getElementText(self, locator):
        return self.getElement(locator).text
    
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
        assert targetElement == expectedText, f"Expected text to be '{expectedText}' but got '{targetElement}'"