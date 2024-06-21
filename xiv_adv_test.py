import requests
from faker import Faker
import random
import string
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest
import logging

logging.basicConfig(level=logging.INFO)  # Example logging configuration

fake = Faker()


@pytest.fixture(scope="module")
def setup_selenium():
    # Setup Selenium WebDriver
    driver = webdriver.Chrome()  # Initialize WebDriver (could be parameterized)
    yield driver  # Provide the fixture object
    driver.quit()  # Teardown: Close WebDriver after all tests in module are completed


def send_api_request():
    # Generate random data
    email = fake.email()
    first_name = fake.first_name()
    phone_number = ''.join(random.choices(string.digits, k=random.randint(11, 21)))
    subject = ''.join(random.choices(string.ascii_letters + string.digits + ' ', k=random.randint(5, 100)))
    description = ''.join(random.choices(string.ascii_letters + string.digits + ' ', k=random.randint(20, 2000)))

    url = "https://automationintesting.online/message/"
    payload = {
        "name": first_name,
        "email": email,
        "phone": phone_number,
        "subject": subject,
        "description": description
    }

    response = requests.post(url, json=payload)
    return response


def test_api_request():
    # Test API request and response
    response = send_api_request()

    assert response.status_code == 201, f"Expected status code 201 but got {response.status_code}"
    response_data = response.json()
    assert "email" in response_data, "Response JSON does not contain 'email' field"

    extracted_email = response_data["email"]
    logging.info(f"Extracted email: {extracted_email}")


@pytest.mark.usefixtures("setup_selenium")
def test_selenium_interaction():
    # Test Selenium interaction with extracted email
    response = send_api_request()
    response_data = response.json()
    extracted_email = response_data.get("email")

    if extracted_email:
        driver = webdriver.Chrome()
        try:
            driver.get("https://getbootstrap.com/docs/4.0/components/forms/")
            time.sleep(3)

            email_element = driver.find_element(By.ID, "exampleInputEmail1")
            email_element.click()
            email_element.send_keys(extracted_email)

            form_value = email_element.get_attribute("value")
            assert form_value == extracted_email, "The value in the form element does not match the extracted email."

        finally:
            driver.quit()
    else:
        pytest.fail("Email was not extracted, so Selenium test cannot proceed")


if __name__ == "__main__":
    pytest.main()
