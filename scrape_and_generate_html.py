from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Replace with your actual credentials
username = "User"  # Replace with your actual username
password = "Pass"  # Replace with your actual password

# Initialize the WebDriver (Firefox)
driver = webdriver.Firefox()  # Use webdriver.Firefox() for Firefox

try:
    # Navigate to the dice.com website
    driver.get("https://www.dice.com/dashboard/login")

    # Wait for the username field to be present using XPath
    wait = WebDriverWait(driver, 50)
    username_field = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@name='email']"))) 

    # Enter the username
    username_field.send_keys(username)


    login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))  
    login_button.click()


    password_field = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@name='password']"))) 
    password_field.send_keys(password)


    
    login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))) 
    login_button.click()


    import time
    time.sleep(15)


finally:
    # Close the browser
    driver.quit()
