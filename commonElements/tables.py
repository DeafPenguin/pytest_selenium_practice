from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pprint

class tables:
    def __init__(self, driver):
        self.driver = driver

    def getTableElement(self, tableLocator: tuple):
        # Return table element
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(tableLocator)
        )
    
    def getHeadersFromTable(self, tableElement):
        # Return table headers element
        return tableElement.find_elements(By.TAG_NAME, "th")

    def getCellByPosition(self, tableLocator: tuple, column: int, row: int):
        # Store table element
        tableElement = self.getTableElement(tableLocator)

        # Verify if <thead> exists on table, then find the specific cell
        try:
            tableElement.find_element(By.TAG_NAME, "thead")
            cellElement = tableElement.find_element(
                By.XPATH, f".//tr[{row}]/td[{column}]"
            )
        except:
            cellElement = tableElement.find_element(
                By.XPATH, f".//tr[{row + 1}]/td[{column}]"
            )

        return cellElement
    
    def getCellByColumnName(self, tableLocator: tuple, columnName, row: int):
        # Store table element
        tableElement = self.getTableElement(tableLocator)
        # Store header element from table element 
        headerElement = self.getHeadersFromTable(tableElement)

        # Create a collection enumerating them
        columns = {header.text: index for index, header in enumerate(headerElement)}

        # Get index of given column name
        columnIndex = columns[columnName]

        # Verify if <thead> exists on table, then find the specific cell using index
        try:
            tableElement.find_element(By.TAG_NAME, "thead")
            cellElement = tableElement.find_element(By.XPATH, f".//tr[{row}]/td[{columnIndex + 1}]")
        except:
            cellElement = tableElement.find_element(By.XPATH, f".//tr[{row + 1}]/td[{columnIndex + 1}]")

        # Return found cell element
        return cellElement

    def getCellTextByColumnName(self, tableLocator: tuple, columnName, row: int):
        element = self.getCellByColumnName(tableLocator, columnName, row)
        return element.text
    
    def clickCellByColumnName(self, tableLocator: tuple, columnName, row: int):
        element = self.getCellByColumnName(tableLocator, columnName, row)
        element.click()

    def getCellTextByPosition(self, tableLocator: tuple, column: int, row: int):
        element = self.getCellByPosition(tableLocator, column, row)
        return element.text
    
    def clickCellByPosition(self, tableLocator: tuple, column: int, row: int):
        element = self.getCellByPosition(tableLocator, column, row)
        element.click()

    def validateCellContentByPosition(self, tableLocator: tuple, column: int, row: int, expectedText):
        elementText = self.getCellTextByPosition(
            tableLocator,
            column,
            row
        )
        assert elementText == expectedText, f"Expected text to be '{expectedText}' but got '{elementText}'"

    def validateCellContentByColumnName(self, tableLocator: tuple, columnName, row: int, expectedText):
        elementText = self.getCellTextByColumnName(
            tableLocator,
            columnName,
            row
        )
        assert elementText == expectedText, f"Expected text to be '{expectedText}' but got '{elementText}'"