import requests
from faker import Faker
import random
import string
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from colorama import Fore, Style  # Importing colorama for colored print

# Initialize Faker
fake = Faker()

# Generate random email address
email = fake.email()

# Generate random first name
first_name = fake.first_name()

# Generate random phone number with length between 11 and 21 characters
phone_number = ''.join(random.choices(string.digits, k=random.randint(11, 21)))

# Generate random subject between 5 and 100 characters
subject = ''.join(random.choices(string.ascii_letters + string.digits + ' ', k=random.randint(5, 100)))

# Generate random text for description with length between 20 and 2000 characters
description = ''.join(random.choices(string.ascii_letters + string.digits + ' ', k=random.randint(20, 2000)))

# URL to send the request to
url = "https://automationintesting.online/message/"

# Payload data
payload = {
    "name": first_name,
    "email": email,
    "phone": phone_number,
    "subject": subject,
    "description": description
}

# Send the POST request
response = requests.post(url, json=payload)

# Variable to hold the extracted email
extracted_email = None

# Check the response status code and error field
if response.status_code == 400:
    response_data = response.json()
    if response_data.get("error") == "BAD_REQUEST":
        print(Fore.RED + "Response contains status code 400 and error BAD_REQUEST:")
        print(payload)
        print(response_data)
    else:
        print(Fore.RED + "Status code is 400, but error is not BAD_REQUEST.")
else:
    print(Fore.GREEN + f"Status code is {response.status_code}, not 400.")
    response_data = response.json()
    print(response_data)

    # Extract the email from the response and save it
    extracted_email = response_data.get("email")
    print(f"Extracted email: {extracted_email}")

# Check if email was extracted
if extracted_email:
    # Set up Selenium WebDriver (make sure to have the correct driver executable in your PATH)
    driver = webdriver.Chrome()  # or webdriver.Firefox() if using Firefox
    try:
        # Open the website
        driver.get("https://getbootstrap.com/docs/4.0/components/forms/")

        # Allow the page to load
        time.sleep(3)  # wait for 3 seconds (you might want to use explicit waits instead)

        # Find the element by its ID and interact with it
        email_element = driver.find_element(By.ID, "exampleInputEmail1")
        email_element.click()
        email_element.send_keys(extracted_email)

        # Retrieve the value from the form element to verify
        form_value = email_element.get_attribute("value")
        print(f"Value in form element: {form_value}")

        # Assert that the value in the form equals the extracted email
        assert form_value == extracted_email, "The value in the form element does not match the extracted email."

        print(Fore.GREEN + "Assertion passed: The value in the form element matches the extracted email.")

        # Add a delay to see the action (optional)
        time.sleep(5)
    finally:
        # Close the browser
        driver.quit()
else:
    print(Fore.RED + "Email was not extracted, so Selenium part is not executed.")

# Reset colors
print(Style.RESET_ALL)