from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import LoginPageLocators
import time
class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        self.driver.find_element(*LoginPageLocators.USERNAME_INPUT).send_keys(username)
        self.driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(password)
        self.driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

    def get_password(self):
        print("Get Password:")
        return self.driver.find_element(*LoginPageLocators.PASSWORD_INPUT).get_attribute("value")
    
    def get_error_message(self):
        return self.driver.find_element(*LoginPageLocators.ERROR_MESSAGE).text

    def sort_products(self, sort_option):
        select = Select(self.driver.find_element(*LoginPageLocators.SORT_SELECT))
        select.select_by_visible_text(sort_option)

    def get_product_price(self):
        return self.driver.find_element(*LoginPageLocators.PRODUCT_PRICE).text

    def get_product_name(self):
        return self.driver.find_element(*LoginPageLocators.PRODUCT_NAME).text

    def add_to_cart(self):
        self.driver.find_element(*LoginPageLocators.ADD_TO_CART_BUTTON).click()

    def is_remove_button_displayed(self):
        return self.driver.find_element(*LoginPageLocators.REMOVE_BUTTON).is_displayed()

    def go_to_cart(self):
        self.driver.find_element(*LoginPageLocators.CART_ICON).click()

    def go_to_checkout(self):
        self.driver.find_element(*LoginPageLocators.CHECKOUT_BUTTON).click()

    def continue_checkout(self, first_name, last_name, postal_code):
        self.driver.find_element(*LoginPageLocators.FIRST_NAME_INPUT).send_keys(first_name)
        self.driver.find_element(*LoginPageLocators.LAST_NAME_INPUT).send_keys(last_name)
        self.driver.find_element(*LoginPageLocators.POSTAL_CODE_INPUT).send_keys(postal_code)
        self.driver.find_element(*LoginPageLocators.CONTINUE_BUTTON).click()
