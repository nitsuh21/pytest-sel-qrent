from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

class LoginPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.login_field = (By.ID, "login")
        self.password_field = (By.ID, "password")
        self.login_button = (By.XPATH, "//button[@type='submit']")

    def open(self):
        self.driver.get('http://167.71.103.169:8072/web/login') 

    def login(self, username: str, password: str):
        self.driver.find_element(*self.login_field).send_keys(username)
        self.driver.find_element(*self.password_field).send_keys(password)
        self.driver.find_element(*self.login_button).click()
