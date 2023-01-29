# 
## Author: Brian Bui
## Date: January 29, 2023
## Desc: Automate valid and invalid login test cases against hudl.com using Selenium Python on Google Chrome.
# 
import unittest
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager

# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

class LoginValidation(unittest.TestCase):
    
    # initialization of webdriver
    def setUp(self):
        self.driver = webdriver.Chrome()

    # test case 1: test valid login credentials by using URLs
    def test_valid_login_by_url(self):
        # retrieve the hudl login page with selenium
        driver = self.driver
        driver.get("https://www.hudl.com/login")
        driver.maximize_window()

        # retrieve the username field & insert valid email
        email = driver.find_element("id", "email")
        email.send_keys("") # insert valid login email as a string here

        # retrieve the password field & insert valid password
        password = driver.find_element("id", "password")
        password.send_keys("") # insert valid login password as a string here

        # navigate to the next page via the log in button
        loginBtn = driver.find_element("id", "logIn")
        loginBtn.click()

        # wait for the page to load
        time.sleep(5)

        # assert to compare URLs
        successfulLoginUrl = "https://www.hudl.com/home"
        expectedUrl = driver.current_url
        self.assertEqual(successfulLoginUrl, expectedUrl, "URLs do not match: Invalid username or password at login")

    # test case 2: test invalid login credentials by using URLs
    def test_invalid_login_by_url(self):
        # retrieve the hudl login page with selenium
        driver = self.driver
        driver.get("https://www.hudl.com/login")
        driver.maximize_window()

        # retrieve the username field & insert invalid email
        email = driver.find_element("id", "email")
        email.send_keys("fakeemail@gmail.com") # insert invalid login email as a string here

        # retrieve the password field & insert invalid password
        password = driver.find_element("id", "password")
        password.send_keys("FakePassword123") # insert invalid login password as a string here

        # navigate to the next page via the log in button
        loginBtn = driver.find_element("id", "logIn")
        loginBtn.click()

        # wait for the page to load
        time.sleep(5)

        # assert to compare URLs
        successfulLoginUrl = "https://www.hudl.com/home"
        expectedUrl = driver.current_url
        self.assertEqual(successfulLoginUrl, expectedUrl, "URLs do not match: Invalid username or password at login")

    # test case 3: test valid login credentials by using page titles
    def test_valid_login_by_title(self):
        # retrieve the hudl login page with selenium
        driver = self.driver
        driver.get("https://www.hudl.com/login")
        driver.maximize_window()

        # retrieve the username field & insert valid email
        email = driver.find_element("id", "email")
        email.send_keys("") # insert valid login email as a string here

        # retrieve the password field & insert valid password
        password = driver.find_element("id", "password")
        password.send_keys("") # insert valid login password as a string here

        # navigate to the next page via the log in button
        loginBtn = driver.find_element("id", "logIn")
        loginBtn.click()

        # explicitly wait for the page title & assert to compare titles
        desiredUrl = "Home - Hudl"
        wait = WebDriverWait(driver, 5)
        wait.until(EC.title_is("Home - Hudl"))
        expectedUrl = driver.title
        self.assertEqual(desiredUrl, expectedUrl, "Titles do not match: Invalid username or password at login")

    # test case 4: test invalid login credentials by using page titles
    def test_invalid_login_by_title(self):
        # retrieve the hudl login page with selenium
        driver = self.driver
        driver.get("https://www.hudl.com/login")
        driver.maximize_window()

        # retrieve the username field & insert invalid email
        email = driver.find_element("id", "email")
        email.send_keys("fakeemail@gmail.com") # insert invalid login email as a string here

        # retrieve the password field & insert invalid password
        password = driver.find_element("id", "password")
        password.send_keys("FakePassword123") # insert invalid login password as a string here

        # navigate to the next page via the log in button
        loginBtn = driver.find_element("id", "logIn")
        loginBtn.click()

        # explicitly wait for the page title & assert to compare titles
        desiredUrl = "Home - Hudl"
        wait = WebDriverWait(driver, 5)
        wait.until(EC.title_is("Home - Hudl"))
        expectedUrl = driver.title
        self.assertEqual(desiredUrl, expectedUrl, "Titles do not match: Invalid username or password at login")

    # clean up method called after every test performed
    def tearDown(self):
        self.driver.close()

# main function
if __name__ == "__main__":
    unittest.main()
