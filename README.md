# hudl-selenium-project
My attempt for Hudl's take-home technical project for the Quality Assurance Engineer I position.

## Description
Automate valid and invalid login test cases against hudl.com using Selenium Python on Google Chrome.

I've implemented two methods of testing: validate login with URL, and validate login with page title. There are two test cases for each method, a positive test case with correct login credentials, and a negative test case with incorrect login credentials. The built-in python testing framework `unittest` is used to assert the test cases.

The validation by page title is implemented using Selenium's explicit wait functions. The negative test case will fail due to the explicit wait function.

The validation by URL is implemented using Python's `time.sleep()` function to mimic `wait()`. The negative test case will fail due to the assertion.


## Setup
To install Selenium using pip3:
```
pip3 install selenium
```
To install Webdriver manager for Python:
```
pip3 install webdriver-manager
```
To run the automated tests:
```
python3 loginhudl.py
```

## Notes
It is important to note that Selenium Webdriver, Python3, and Chromedriver must be installed.
---
Please enter the correct login email/password on lines 35, 39 for URL and on lines 89, 93 for Title.
```
email.send_keys("someValidHudlEmail@hudl.com")
```
```
password.send_keys("SomeValidPassword123")
```
Note: False/Invalid login credentials will already be inputted for the negative test cases, but you may add any to your preference.

---
If you receive this warning:
```
DeprecationWarning: executable_path has been deprecated, please pass in a Service object
```
Then uncomment lines 15-18:
```
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
```
