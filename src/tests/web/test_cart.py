import allure
import pytest
from src.web.pages.login_page import LoginPage
from src.web.pages.inventory_page import InventoryPage
from src.web.pages.cart_page import CartPage
from src.web.config.config import base_url, password, username
from src.utils.testrail_integration import update_test_result

@pytest.mark.testrail(id="1")
@allure.story('Add Two Random Products to Cart')
@allure.severity('normal')
def test_add_two_random_products_to_cart(driver):
    login_page = LoginPage(driver)
    driver.get(base_url)
    login_page.enter_username(username)
    login_page.enter_password(password)
    login_page.click_login()
    inventory_page = InventoryPage(driver)
    initial_cart_count = inventory_page.get_cart_badge_count()
    with allure.step('Verify that the cart badge count is 0'):
        assert initial_cart_count == 0,f"The cart was expected to be empty, but: {initial_cart_count} items were found"

    inventory_page.add_random_products_to_cart(count=2)
    updated_cart_count = inventory_page.get_cart_badge_count()
    with allure.step('Verify that the cart badge count is updated to 2'):
        assert updated_cart_count == 2, f"2 items were expected in the cart, but: {updated_cart_count}  items were found "

    inventory_page.go_to_cart()
    cart_page = CartPage(driver)
    cart_count = cart_page.get_cart_items_count()
    with allure.step('Verify that the cart displays exactly two items'):
        assert cart_count == 2, f"2 items were expected in the cart, but {cart_count} items were found!"

    update_test_result(1, status=1)

@pytest.mark.testrail(id="2")
@allure.story('Cart Displays Correct Products')
@allure.severity('normal')
def test_cart_products_display_correctly(driver):
    login_page = LoginPage(driver)
    driver.get(base_url)
    login_page.enter_username(username)
    login_page.enter_password(password)
    login_page.click_login()
    inventory_page = InventoryPage(driver)
    with allure.step('Add specific products to the cart ("Sauce Labs Bolt T-Shirt", "Sauce Labs Fleece Jacket").'):
        expected_products = inventory_page.add_specific_products_to_cart([2, 3])
    inventory_page.go_to_cart()
    cart_page = CartPage(driver)
    cart_products = cart_page.get_cart_product_names()
    with allure.step('The Cart Page displays only the added products with the correct names and descriptions.'):
        assert sorted(cart_products) == sorted(expected_products), \
        f"Expected items: {expected_products}, but in the cart: {cart_products}"

    update_test_result(2, status=1)

@pytest.mark.testrail(id="3")
@allure.story('Add and Remove Products from Cart')
@allure.severity('normal')
def test_add_and_remove_products_from_cart(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)
    driver.get(base_url)
    login_page.enter_username(username)
    login_page.enter_password(password)
    login_page.click_login()
    initial_cart_count = inventory_page.get_cart_badge_count()

    with allure.step('Verify that the cart badge count is 0'):
        assert initial_cart_count == 0, f"The cart was expected to be empty, but {initial_cart_count} items were found!"
    inventory_page.add_random_products_to_cart(count=2)
    updated_cart_count = inventory_page.get_cart_badge_count()

    with allure.step('Verify that the cart badge count is updated to 2'):
        assert updated_cart_count == 2, f"2 items were expected in the cart, but {updated_cart_count} items were found!"
    inventory_page.go_to_cart()
    cart_count = cart_page.get_cart_items_count()

    with allure.step('Verify that the cart displays two items'):
        assert cart_count == 2, f"2 items were expected in the cart, but {cart_count} items were found!"
    cart_page.remove_item_from_cart(0)
    cart_page.remove_item_from_cart(0)

    with allure.step('Verify that the  cart is completely empty'):
        assert cart_page.is_cart_empty(), "The cart was expected to be empty after deleting all items!"
    update_test_result(3, status=1)