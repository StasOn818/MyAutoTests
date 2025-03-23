import allure
from selenium.webdriver.common.by import By
from src.web.pages.base_page import BasePage

class CheckoutPage(BasePage):
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    ZIP_CODE = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")

    def fill_checkout_info(self, first_name, last_name, zip_code):
        with allure.step('Fill the First Name Field: ' + first_name):
            self.driver.find_element(*self.FIRST_NAME).send_keys(first_name)
        with allure.step('Fill the Last Name Field: ' + last_name):
            self.driver.find_element(*self.LAST_NAME).send_keys(last_name)
        with allure.step('Fill the Zip Code Field: ' + zip_code):
            self.driver.find_element(*self.ZIP_CODE).send_keys(zip_code)

    def click_continue(self):
        with allure.step('Click the Continue Button'):
            self.driver.find_element(*self.CONTINUE_BUTTON).click()
