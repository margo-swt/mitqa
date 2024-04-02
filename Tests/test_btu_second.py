from Actions.registration_actions import click_submit_button
from Locators.registration_locators import RegistrationLocators, submit_button_error

registration_locator = RegistrationLocators()


# Function to run the test case
def test_registration():
    registration_locator.first_name_input.send_keys("test")
    registration_locator.last_name_input.send_keys("last name value")
    click_submit_button()

    actual_error_value = submit_button_error().text
    expected_error_value = "Please correct errors before submitting this form."

    assert expected_error_value in actual_error_value
