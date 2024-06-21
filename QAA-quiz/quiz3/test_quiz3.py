from selenium import webdriver
from actions import LoginPage
import time

def test_quiz3():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get('https://www.saucedemo.com/')
    driver.maximize_window()
    
    page = LoginPage(driver)

    # page.login("invalid_user", "password")
    # error_text = page.get_error_message()
    # assert error_text == "Epic sadface: Username and password do not match any user in this service", \
    #        "Expected error message for invalid login credentials"
    
    page.login("standard_user", "secret_sauce")
    assert "inventory" in driver.current_url

    page.sort_products("Price (low to high)")
    
    page.add_to_cart()
    assert page.is_remove_button_displayed(), "Expected 'Remove' button to be displayed after adding to cart"
    
    product_price = page.get_product_price()
    product_name = page.get_product_name()
    print(product_price, product_name)
    assert product_price == "$7.99", "Expected price to be $7.99"

    page.go_to_cart()

    print(page.get_product_price(), page.get_product_name())
    assert page.get_product_price() == product_price, "Expected product price in cart to match"
    assert page.get_product_name() == product_name, "Expected product name to match"
    
    page.go_to_checkout()

    page.continue_checkout("", "", "")
    error_message = page.get_error_message()
    assert "Error: First Name is required" in error_message, "Expected error message for missing first name"

    driver.quit()

if __name__ == "__main__":
    test_quiz3()
