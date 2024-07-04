# fixtures.py
import pytest
from selenium import webdriver

@pytest.fixture
def browserChrome():
    # WebDriver configuration (using Chrome as example)
    driver = webdriver.Chrome() # Be sure that ChromeDriver is installed and added into PATH
    yield driver
    driver.quit()