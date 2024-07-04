from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class lists:
    def __init__(self, driver):
        self.driver = driver

    def getListElement(self, listLocator, repeatableElement, position):
        # Store list element
        listElement = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(listLocator)
        )

        # Find child elements via repeatable element
        childElements = listElement.find_elements(*repeatableElement)

        # Return target child element
        return childElements[position - 1]

