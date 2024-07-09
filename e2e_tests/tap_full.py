import pytest
from selenium import webdriver
from fixtures.browser import browserChrome
from pageObjects.test_automation_practice_page import TestAutomationPracticePage
import pprint

def test_interactWithPage(browserChrome):
    # Variables for the test
    headerText = "Automation Testing Practice"
    userName = "Victor Machado"
    userEmail = "victormurilo@gmail.com"
    userPhone = "(62)99999-9999"
    userAddress = "Goiania - GO"
    userCountry = "Brazil"
    sundayText = "Sunday"
    mondayText = "Monday"
    tuesdayText = "Tuesday"
    wednesdayText = "Wednesday"
    thursdayText = "Thursday"
    fridayText = "Friday"
    saturdayext = "Saturday"
    targetDate = '12/25/2022'
    openCartLink = 'https://demo.opencart.com/'
    orangeHRMLink = 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'
    userAmit = "Amit"
    thirdBook = "Learn JS"
    fourthBook = "Master In Selenium"
    sixthBook = "Master In JS"
    javascriptSubject = "Javascript"
    fourthBookPrice = "3000"
    color = "Green"
    product4Name = "Product 4"
    product4Price = "$7.99"
    pauseText = "\n\nPress enter in terminal to finish..."

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
    testAutomationPracticePage.clickElement(testAutomationPracticePage.femaleGenderRadioButton)

    # Selecting Monday and Wednesday on list
    testAutomationPracticePage.selectDayOfListByValue(mondayText)
    testAutomationPracticePage.selectDayOfListByValue(wednesdayText)

    # Validating Days selection
    testAutomationPracticePage.validateWeekdayIsNotChecked(sundayText)
    testAutomationPracticePage.validateWeekdayIsChecked(mondayText)
    testAutomationPracticePage.validateWeekdayIsNotChecked(tuesdayText)
    testAutomationPracticePage.validateWeekdayIsChecked(wednesdayText)
    testAutomationPracticePage.validateWeekdayIsNotChecked(thursdayText)
    testAutomationPracticePage.validateWeekdayIsNotChecked(fridayText)
    testAutomationPracticePage.validateWeekdayIsNotChecked(saturdayext)

    # Selecting country
    testAutomationPracticePage.select(testAutomationPracticePage.countryDropdown, userCountry)

    # Selecting colors
    testAutomationPracticePage.select(testAutomationPracticePage.colors, color)

    # Select an date on calendar
    testAutomationPracticePage.selectDate(testAutomationPracticePage.calendar, targetDate)

    # Validate Links
    testAutomationPracticePage.validateElementHref(testAutomationPracticePage.openCartLink, openCartLink)
    testAutomationPracticePage.validateElementHref(testAutomationPracticePage.orangeHRMLink, orangeHRMLink)

    # Validate Author from given book
    testAutomationPracticePage.validateBookAuthor(sixthBook, userAmit)

    # Validate Subject from given book
    testAutomationPracticePage.validateBookSubject(thirdBook, javascriptSubject)

    # Validate Price from given book
    testAutomationPracticePage.validateBookPrice(fourthBook, fourthBookPrice)

    # Click on select by given product name
    testAutomationPracticePage.selectProductByName(product4Name)

    # Validate Price from given product
    testAutomationPracticePage.validateProductPrice(product4Name, product4Price)

    # Submit form and validate iframe
    testAutomationPracticePage.submitFormAndValidate()

    # Pause execution until press enter in terminal
    input(pauseText)