from Locators.registration_locators import RegistrationLocators

registration_locator = RegistrationLocators()


def click_submit_button():
    registration_locator.submit_button.click()
