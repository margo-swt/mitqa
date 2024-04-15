from selenium.webdriver.common.by import By
from conftest import DriverSetUp
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = DriverSetUp.driver
wait = WebDriverWait(driver, 10)


class Regitration_Locators:
    first_name_input = driver.find_element(By.ID, "nf-field-17")

    # element = wait.until(EC.visibility_of_element_located((By.ID, 'locator_value')))

    # last_name_input = driver.find_element(By.CSS_SELECTOR, "#nf-field-18")
    submit_button = driver.find_element(By.XPATH, "//*[@id='nf-field-15']")
    last_name_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#nf-field-18')))

    def sumbit_button_error(self):
        submit_error_text = driver.find_element(By.XPATH, "//*[@id='nf-form-errors-3']//*/div")
        return submit_error_text
