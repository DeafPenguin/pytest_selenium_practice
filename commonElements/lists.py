from commonElements.elements import elements

class lists(elements):
    def __init__(self, driver):
        self.driver = driver

    def getListElementByPosition(self, listLocator, repeatableElement, position):
        # Store list element
        listElement = self.getElement(listLocator)

        # Find child elements via repeatable element
        childElements = listElement.find_elements(*repeatableElement)

        # Return target child element
        return childElements[position - 1]
    
    def getListElementByValue(self, listLocator, repeatableElement, targetValue):
        # Store list element
        listElement = self.getElement(listLocator)

        # Find child elements via repeatable element
        childElements = listElement.find_elements(*repeatableElement)

        # Return target child element
        for element in childElements:
            if targetValue in element.text:
                return element
            
    def clickOnListElementByPosition(self, listLocator, repeatableElement, position):
        # Store the element from the given list element
        listElement = self.getListElementByPosition(listLocator, repeatableElement, position)

        listElement.click()
    
    def clickOnListElementByValue(self, listLocator, repeatableElement, targetValue):
        # Store the element from the given list element
        listElement = self.getListElementByValue(listLocator, repeatableElement, targetValue)

        listElement.click()

