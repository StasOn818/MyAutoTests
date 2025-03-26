import random
import allure
from selenium.webdriver.common.by import By
from src.web.pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class InventoryPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.username_field = (By.ID, "user-name")
        self.burger_menu_button = (By.ID, 'react-burger-menu-btn')
        self.logout_button = (By.ID,'logout_sidebar_link')
    PRODUCT_LIST = (By.CLASS_NAME, "inventory_container")
    PRODUCT_NAMES = (By.CLASS_NAME, "inventory_item_name")
    ADD_TO_CART_BUTTONS = (By.CLASS_NAME, "btn_inventory")
    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    TWITTER_ICON = (By.XPATH, "//a[@href='https://twitter.com/saucelabs']")
    FACEBOOK_ICON = (By.XPATH, "//a[@href='https://www.facebook.com/saucelabs']")
    LINKEDIN_ICON = (By.XPATH, "//a[@href='https://www.linkedin.com/company/sauce-labs/']")



    def click_burger_menu_button(self):
        with allure.step('Click the Burger Menu button'):
            self.driver.find_element(*self.burger_menu_button).click()

    def wait_for_logout_button(self, timeout=5):
        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(self.logout_button),
            "The 'Logout' button did not appear after opening the menu."
        )
    def click_logout_button(self):
        with allure.step('Click the Logout button'):
            self.driver.find_element(*self.logout_button).click()

    def get_product_count(self):
        with allure.step('The inventory page with product carts  displayed'):
            return len(self.driver.find_elements(*self.PRODUCT_LIST))

    def is_login_page_displayed(self):
        with allure.step('Login page displayed'):
            return self.is_element_visible(*self.username_field)

    def add_specific_products_to_cart(self, indexes):
        product_elements = self.driver.find_elements(*self.PRODUCT_NAMES)
        add_buttons = self.driver.find_elements(*self.ADD_TO_CART_BUTTONS)
        selected_products = []
        for index in indexes:
            if index < len(add_buttons):
                selected_products.append(product_elements[index].text)
                add_buttons[index].click()
        return selected_products

    def add_random_products_to_cart(self, count=2):
        add_buttons = self.driver.find_elements(*self.ADD_TO_CART_BUTTONS)
        indexes = random.sample(range(len(add_buttons)), count)
        with allure.step('Add two random products to the cart'):
            self.add_specific_products_to_cart(indexes)

    def go_to_cart(self):
        with allure.step('Go to the cart'):
            self.driver.find_element(*self.CART_ICON).click()

    def get_cart_badge_count(self):
        try:
            return int(self.driver.find_element(*self.CART_BADGE).text)
        except:
            return 0

    def open_social_link_and_return(self, social_icon, expected_url):
        icon = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(social_icon))
        icon.click()
        WebDriverWait(self.driver, 5).until(lambda d: len(d.window_handles) > 1)
        new_tab = self.driver.window_handles[1]
        self.driver.switch_to.window(new_tab)
        WebDriverWait(self.driver, 10).until(EC.url_contains(expected_url))
        current_url = self.driver.current_url

        assert expected_url in current_url, f"Expected URL for {social_icon} '{expected_url}', but opened {current_url}"

        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])

    def open_twitter_and_return(self):
        with allure.step('The user goes to the Sauce Labs Twitter page (x.com/saucelabs).'):
            self.open_social_link_and_return(self.TWITTER_ICON, "x.com/saucelabs")

    def open_facebook_and_return(self):
        with allure.step('The user goes to the Sauce Labs Facebook page (facebook.com/saucelabs).'):
            self.open_social_link_and_return(self.FACEBOOK_ICON, "facebook.com/saucelabs")

    def open_linkedin_and_return(self):
        with allure.step('The user goes to the Sauce Labs LinkedIn page (linkedin.com/company/sauce-labs).'):
            self.open_social_link_and_return(self.LINKEDIN_ICON, "linkedin.com/company/sauce-labs/")