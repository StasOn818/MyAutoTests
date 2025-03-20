from selenium.webdriver.common.by import By
from src.web.pages.base_page import BasePage

class CheckoutCompletePage(BasePage):
    COMPLETE_TEXT = (By.CLASS_NAME, "complete-header")
    BACK_HOME_BUTTON = (By.XPATH, "//button [@ class= 'btn btn_primary btn_small']")

    def is_order_complete(self):
        return self.is_element_visible(self.COMPLETE_TEXT)

    def click_back_home(self):
        back_home_button = self.driver.find_element(*self.BACK_HOME_BUTTON)
        back_home_button.click()