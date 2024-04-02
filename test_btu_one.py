from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


# Function to run the test case
def test_demo():
    # Set up Selenium webdriver (Assuming Chrome webdriver is installed)
    driver = webdriver.Chrome()

    try:
        # Open the webpage
        driver.get("https://www.example.com")
        time.sleep(2)  # Let the page load

        # Find the search box and enter a search query
        search_box = driver.find_element_by_name("q")
        search_box.send_keys("Selenium automation")
        search_box.send_keys(Keys.RETURN)
        time.sleep(2)  # Let the search results load

        # Assert if the search results page title contains the search query
        assert "Selenium automation" in driver.title

        # Find the first search result link and click on it
        first_result = driver.find_element_by_css_selector("h3 > a")
        first_result.click()
        time.sleep(2)  # Let the page load

        # Assert if the page title contains the expected keyword
        assert "Selenium" in driver.title

        # Print success message if all assertions pass
        print("Test passed successfully!")

    except Exception as e:
        print(f"Test failed: {e}")

    finally:
        # Close the browser window
        driver.quit()
