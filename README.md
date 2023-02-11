# Hybrid_Framework_Selenium_Python
Hybrid driven Framework with:
* Python
* Selenium
* Pytest
* Pytest-html
* Pytest-xdist
* Openpyxl
* Allure-pytest

The framework has:
* Login test case(test_login.py)
* POM (LoginPage.py)
* Ability to take screenshots in case of failure (Screenshot folder)
* Ability to use common actions for test steps (conftest.py)
* Common fields stored in configuration file(config.ini)
* File to read the stored configuration in order to be used in tests (readProperties.py)
* Log mechanism to log the execution of test cases (customLogger.py)
* Ability to Run parallel test/ Cross browser tests (conftest.py)
* Ability to Generate HTML report in Reports folder (conftest.py)
* Data Driven Test Case(test_login_ddt, XLUtils.py, LoginData.xlsx)
* The ability to add tests to existing framework (AddcustomerPage.py, test_addCustomer.py, SearchCustomerPage.py, test_searchCustomerByEmail.py, test_searchCustomerByName.py)

AUT:
* FrontEnd: https://demo.nopcommerce.com
* BackEnd: https://admin-demo.nopcommerce.com/

### Notes:
#### To run tests on desired browser:
* pytest -v -s test_Cases/test_login.py --browser chrome
* pytest -v -s test_Cases/test_login.py --browser firefox

#### To run tests parallel:
* pytest -v -s -n=3 test_Cases/test_login.py --browser chrome
* pytest -v -s -n=3 test_Cases/test_login.py --browser firefox

#### To Generate Pytest HTML Reports:
* pytest -v -s -n=3 --html=Reports/report.html test_Cases/test_login.py --browser chrome

#### To Run specific Pytest tests with markers:
* pytest -s -v -m "sanity and regression" --html=Reports/report.html testCases/ --browser chrome (This means sanity and regression tests)
* pytest -s -v -m "sanity and regression" --html=Reports/report.html testCases/ --browser chrome (This means sanity or regression tests)
* pytest -s -v -m "sanity" --html=Reports/report.html testCases/ --browser chrome (This means only sanity tests)


