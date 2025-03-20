from selenium.webdriver.common.by import By
from src.web.pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage(BasePage):
    CART_ITEMS = (By.CLASS_NAME, "cart_item")
    CHECKOUT_BUTTON = (By.ID, "checkout")
    REMOVE_BUTTON = (By.XPATH, "//button[text()='Remove']")
    ITEM_NAMES = (By.CLASS_NAME, "inventory_item_name")

    def get_cart_items_count(self):
        return len(self.driver.find_elements(*self.CART_ITEMS))

    def remove_item_from_cart(self, index=0):
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_all_elements_located(self.REMOVE_BUTTON)
        )
        remove_buttons = self.driver.find_elements(*self.REMOVE_BUTTON)
        if len(remove_buttons) > index:
            remove_buttons[index].click()
            WebDriverWait(self.driver, 5).until(
                lambda d: len(d.find_elements(*self.CART_ITEMS)) < len(remove_buttons)
            )
        else:
            raise ValueError(f"Can't delete item {index}, only {len(remove_buttons)} items in cart.")

    def click_checkout(self):
        self.driver.find_element(*self.CHECKOUT_BUTTON).click()

    def get_cart_product_names(self):
        items = self.driver.find_elements(*self.ITEM_NAMES)
        return [item.text for item in items]

    def is_cart_empty(self):
        return len(self.driver.find_elements(*self.CART_ITEMS)) == 0