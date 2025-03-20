from selenium.webdriver.common.by import By
from src.web.pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
class CheckoutSummaryPage(BasePage):
    PRODUCT_NAMES = (By.CLASS_NAME, "inventory_item_name")
    FINISH_BUTTON = (By.ID, "finish")

    def get_summary_product_names(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located((By.CLASS_NAME, "inventory_item_name"))
            )
            elements = self.driver.find_elements(By.CLASS_NAME, "inventory_item_name")
            return [element.text for element in elements] if elements else []
        except Exception as e:
            print(f"Error during getting summary product names: {e}")
            return []

    def click_finish(self):
        self.driver.find_element(*self.FINISH_BUTTON).click()