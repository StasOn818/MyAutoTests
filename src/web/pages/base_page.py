from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import TimeoutException

class BasePage:
    def __init__(self, driver):
        self.driver = driver

        # TEST - 2

    def is_text_present(self, text):
        try:
            body_text = self.driver.find_element(By.TAG_NAME, "body").text
            return text in body_text
        except NoSuchElementException:
            return False

    def is_element_visible(self, locator, timeout=5):
        try:
            WebDriverWait(self.driver, timeout).until(expected_conditions.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False
