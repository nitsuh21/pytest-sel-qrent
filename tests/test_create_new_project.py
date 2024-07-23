from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, ElementNotInteractableException

# Configuration
url = "http://167.71.103.169:8072/web/login"
username = "qrent@gmail.com"
password = "admin"

# Initialize the WebDriver
driver = webdriver.Chrome()

try:
    # Open the Odoo login page
    driver.get(url)
    
    # Locate and fill the username field
    username_field = driver.find_element(By.NAME, "login")
    username_field.send_keys(username)
    
    # Locate and fill the password field
    password_field = driver.find_element(By.NAME, "password")
    password_field.send_keys(password)
    
    # Locate and click the login button
    login_button = driver.find_element(By.XPATH, "//button[contains(@class, 'btn-primary')]")
    login_button.click()

    print("Logged in successfully.")
    
    # Wait until the Projects menu item is present and click it
    WebDriverWait(driver, 50).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='result_app_6']"))
    ).click()
    
    # Wait until the "Create" button is present and click it
    WebDriverWait(driver, 50).until(
        EC.presence_of_element_located((By.XPATH, "//button[contains(@class, 'o-kanban-button-new')]"))
    ).click()
    
    # Wait until the project name input is present, scroll into view, and fill it
    new_project_field = WebDriverWait(driver, 50).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id='name']"))
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", new_project_field)
    
    # Fill the project name
    new_project_field.send_keys("New Demo Project 2")
    
    # Locate the save button and click it
    save_button = driver.find_element(By.XPATH, "//*[@id='dialog_1']/div/div/div/footer/footer/button[1]")
    driver.execute_script("arguments[0].click();", save_button)
    
    print("Project created successfully.")

    # Wait until the "Edit" button is present

    
except TimeoutException:
    print("An element was not found within the specified timeout.")
except ElementNotInteractableException:
    print("The element was not interactable.")
finally:
    # Close the WebDriver
    driver.quit()
