from Actions.registration_actions import click_submit_button
from Locators.registration_locators import Regitration_Locators
from conftest import DriverSetUp
from qaseio.pytest import qase

registration_locator = Regitration_Locators()


# Function to run the test case
# @qase.step("First step") # test step name
@qase.id(2)  # existing test case id - can replace your test case
def test_registration():
    registration_locator.first_name_input.send_keys("test")
    registration_locator.last_name_input.send_keys("last name value")
    click_submit_button()

    actual_error_value = registration_locator.sumbit_button_error().text
    expected_error_value = "Please correct errors before submitting this form."

    assert expected_error_value in actual_error_value

    DriverSetUp.driver.quit()
