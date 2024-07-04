from commonElements.elements import elements
from commonElements.lists import lists
from commonElements.tables import tables

class commonElements(elements, lists, tables):
    def __init__(self, driver):
        elements.__init__(self, driver)
        lists.__init__(self, driver)
        tables.__init__(self, driver)