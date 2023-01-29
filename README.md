# hudl-selenium-project
Hudl's take-home technical project

## Description
Automate valid and invalid login test cases against hudl.com using Selenium Python on Google Chrome.

I've implemented two methods of testing: validate login with URL, and validate login with page title. There are two test cases for each method, a positive test case with correct login credentials, and a negative test case with incorrect login credentials.

The validation by page title is implemented using Selenium's explicit wait functions.
The validation by URL is implemented using Python's `time.sleep()` to mimic wait.

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

Please enter the correct login email/password on lines 43, 46 for URL and on lines 83, 86 for Title.
```
email.send_keys("someValidHudlEmail@hudl.com")
```
```
password.send_keys("SomeValidPassword123")
```
Note: False/Invalid login credentials will already be inputted for the negative test cases.
