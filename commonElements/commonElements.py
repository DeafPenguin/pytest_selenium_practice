from commonElements.lists import lists
from commonElements.tables import tables
from commonElements.datepickers import datepickers
from commonElements.iframes import iframes

class commonElements(lists, tables, datepickers, iframes):
    def __init__(self, driver):
        lists.__init__(self, driver)
        tables.__init__(self, driver)
        datepickers.__init__(self, driver)
        iframes.__init__(self, driver)