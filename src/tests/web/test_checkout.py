import pytest
from src.web.config.config import base_url, password, username
from src.web.pages.login_page import LoginPage
from src.web.pages.inventory_page import InventoryPage
from src.web.pages.cart_page import CartPage
from src.web.pages.checkout_page import CheckoutPage
from src.web.pages.checkout_summary_page import CheckoutSummaryPage
from src.web.pages.checkout_complete_page import CheckoutCompletePage
from src.utils.testrail_integration import update_test_result

@pytest.mark.testrail(id="8")
def test_checkout_process(driver):
    driver.get(base_url)
    login_page = LoginPage(driver)
    login_page.enter_username(username)
    login_page.enter_password(password)
    login_page.click_login()
    inventory_page = InventoryPage(driver)
    inventory_page.add_random_products_to_cart(count=2)
    inventory_page.go_to_cart()
    cart_page = CartPage(driver)
    cart_page.click_checkout()
    checkout_page = CheckoutPage(driver)
    checkout_page.fill_checkout_info(first_name="John", last_name="Snow", zip_code="01001")
    checkout_page.click_continue()
    summary_page = CheckoutSummaryPage(driver)
    summary_page.click_finish()
    confirmation_page = CheckoutCompletePage(driver)

    assert confirmation_page.is_order_complete(), "The order was not successfully placed!"
    confirmation_page.click_back_home()

    assert driver.current_url == "https://www.saucedemo.com/inventory.html", \
        f"Expected product page: https://www.saucedemo.com/inventory.html, but returned: {driver.current_url}"

    update_test_result(8, status=1)