import pytest
from selenium import webdriver
from fixtures.browser import browserChrome
from pageObjects.test_automation_practice_page import TestAutomationPracticePage

def test_interactWithPage(browserChrome):
    # Variables for the test
    headerText = "Automation Testing Practice"
    userName = "Victor Machado"
    userEmail = "victormurilo@gmail.com"
    userPhone = "(62)99999-9999"
    userAddress = "Goiania - GO"
    userCountry = "Brazil"
    userAnimesh = "Animesh"
    userAmod = "Amod"
    color = "Green"
    authorColumnName = "Author"
    priceColumnName = "Price"
    product2Price = "$19.99"
    product3Price = "$5.99"
    pauseText = "Press enter in terminal to finish..."

    testAutomationPracticePage = TestAutomationPracticePage(browserChrome)
    testAutomationPracticePage.load()

    # Validating header
    testAutomationPracticePage.validateElementText(testAutomationPracticePage.headerInner, headerText)

    # Fill form
    testAutomationPracticePage.type(testAutomationPracticePage.nameInput, userName)
    testAutomationPracticePage.type(testAutomationPracticePage.emailInput, userEmail)
    testAutomationPracticePage.type(testAutomationPracticePage.phoneInput, userPhone)
    testAutomationPracticePage.type(testAutomationPracticePage.addressInput, userAddress)

    # Selecting gender
    testAutomationPracticePage.clickElement(testAutomationPracticePage.maleGenderRadioButton)

    # Selecting Tuesday on list
    testAutomationPracticePage.selectDayOfList(3)

    # Selecting country
    testAutomationPracticePage.select(testAutomationPracticePage.countryDropdown, userCountry)

    # Selecting colors
    testAutomationPracticePage.select(testAutomationPracticePage.colors, color)

    # Validating headless table content by position
    testAutomationPracticePage.validateCellContentByPosition(testAutomationPracticePage.webTable, 2, 3, userAnimesh)

    # Validating headless table content by column content
    testAutomationPracticePage.validateCellContentByColumnName(testAutomationPracticePage.webTable, authorColumnName, 5, userAmod)

    # Validating headed table content by position
    testAutomationPracticePage.validateCellContentByPosition(testAutomationPracticePage.paginationTable, 3, 2, product2Price)

    # Validating headed table content by column content
    testAutomationPracticePage.validateCellContentByColumnName(testAutomationPracticePage.paginationTable, priceColumnName, 3, product3Price)

    # Click on select by column name
    testAutomationPracticePage.selectProductOnPaginationTableByRowNumber(3)

    # Pause execution until press enter in terminal
    input(pauseText)