# Selenium Pytest Project

This is a practice project using Selenium and Pytest on the site [Test Automation Practice](https://testautomationpractice.blogspot.com/).

## Requirements

- Python 3.x
- Selenium
- Chrome WebDriver
- Allure-pytest for reports

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your_username/your_repository.git
    cd your_repository
    ```

2. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Download the Chrome WebDriver compatible with your browser version and add it to your PATH. You can download the Chrome WebDriver [here](https://sites.google.com/a/chromium.org/chromedriver/downloads).

## Running the Tests

To run the tests, use the following command inside the `e2e_tests` folder:
```bash
pytest -s tap_full.py
```

## Reports

To generate reports with Allure, follow the steps below:

1. Install Allure:
    ```bash
    pip install allure-pytest
    ```

2. Run the tests with report generation:
    ```bash
    pytest -s --alluredir=./reports tap_full.py
    ```

3. Generate and view the report:
    ```bash
    allure serve ./reports
    ```

## Project Structure

`commonElements/` : Folder for common classes used in the tests.

`drivers/` : Folder for drivers files used to set up the project.

`e2e_tests/` : Folder containing the end-to-end tests.

`fixtures/` : Folder for fixtures used in the tests.

`k8s/` : Folder for YAML files used to set up docker.

`pageObjects/` : Folder for page objects used in the tests.

`reports/` : Folder for generated reports from Allure.
