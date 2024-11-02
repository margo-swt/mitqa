'''
Automate Login Process:
●	Open the practice test website: https://practicetestautomation.com/practice-test-login/.
●	Input the saved email and password into the login form.

Submit Login Form:
●	Click the submit button on the login form.

Validate Error Message:
●	Verify the error message displayed upon incorrect login.
●	Ensure that the error message is as expected.
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# URL of the practice test website
URL = 'https://practicetestautomation.com/practice-test-login/'

# Credentials
USERNAME = 'student'
PASSWORD = 'aksjdasli'

# Function to automate login and validate error message
def test_login():
    # Initialize Chrome WebDriver
    driver = webdriver.Chrome()
    driver.maximize_window()

    try:
        # Open the practice test website
        driver.get(URL)
        time.sleep(2)  # Optional: Add a delay to ensure page fully loads

        # Input email and password into the login form
        username_input = driver.find_element(By.ID, 'username')
        username_input.send_keys(USERNAME)

        password_input = driver.find_element(By.ID, 'password')
        password_input.send_keys(PASSWORD)

        # Submit login form
        submit_button = driver.find_element(By.ID, 'submit')
        submit_button.click()

        time.sleep(2)  # Optional: Add a delay to ensure next page fully loads or error message appears

        # Validate error message
        error_message_element = driver.find_element(By.ID, 'error')
        error_message = error_message_element.text

        expected_error_message = "Your password is invalid!"

        assert expected_error_message in error_message, f"Expected error message '{expected_error_message}' not found"

        print("Login test successful!")

    finally:
        # Close the browser
        driver.quit()

# Entry point to run the test
if __name__ == "__main__":
    test_login()