from Locators.registration_locators import Regitration_Locators

registration_locator = Regitration_Locators()


def click_submit_button():
    registration_locator.submit_button.click()
