from selenium.webdriver.common.by import By
from conftest import DriverSetUp

driver = DriverSetUp.driver


# Per Page Locators - can be placed under one class
# Locators can also be placed under function


def submit_button_error():
    submit_error_text = driver.find_element(By.XPATH, "//*[@id='nf-form-errors-3']//*/div")
    return submit_error_text


class RegistrationLocators:
    first_name_input = driver.find_element(By.ID, "nf-field-17")
    last_name_input = driver.find_element(By.CSS_SELECTOR, "#nf-field-18")
    submit_button = driver.find_element(By.XPATH, "//*[@id='nf-field-15']")


