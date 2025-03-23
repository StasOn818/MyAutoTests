import allure
from selenium.webdriver.common.by import By
from src.web.pages.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.username_field = (By.ID, "user-name")
        self.password_field = (By.ID, "password")
        self.login_button = (By.NAME, "login-button")
        self.error_message = "Epic sadface: Username and password do not match any user in this service"

    def enter_username(self, username):
        with allure.step('Enter the value in username field: ' + username):
            self.driver.find_element(*self.username_field).send_keys(username)

    def enter_password(self, password):
         with allure.step('Enter the value in password field: ' + password):
             self.driver.find_element(*self.password_field).send_keys(password)

    def click_login(self):
        with allure.step('Click the login button'):
            self.driver.find_element(*self.login_button).click()

    def is_login_page_displayed(self):
        with allure.step('Login page displayed'):
            return self.is_element_visible(self.login_button)