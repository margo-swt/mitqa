from selenium import webdriver


class DriverSetUp:
    # Set up Chrome browser and the website page to load before tests execution
    driver = webdriver.Chrome()
    driver.get("https://codenboxautomationlab.com/registration-form/")
