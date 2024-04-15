from selenium import webdriver


class DriverSetUp:
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://codenboxautomationlab.com/registration-form/")
    # driver.implicitly_wait(10)
