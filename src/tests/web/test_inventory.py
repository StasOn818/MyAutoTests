import pytest
from src.web.config.config import base_url, password, username
from src.web.pages.login_page import LoginPage
from src.web.pages.inventory_page import InventoryPage
from src.utils.testrail_integration import update_test_result

@pytest.mark.testrail(id="9")
def test_inventory_items(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    driver.get(base_url)
    login_page.enter_username(username)
    login_page.enter_password(password)
    login_page.click_login()
    product_count = inventory_page.get_product_count()

    assert product_count > 0, "No products on the page!"

    update_test_result(9, status=1)

@pytest.mark.testrail(id="10")
def test_logout_button_work(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    driver.get(base_url)
    login_page.enter_username(username)
    login_page.enter_password(password)
    login_page.click_login()
    inventory_page.click_burger_menu_button()
    inventory_page.wait_for_logout_button()
    inventory_page.click_logout_button()

    assert login_page.is_login_page_displayed(), "The user did not return to the login page!"

    update_test_result(10, status=1)

@pytest.mark.testrail(id="12")
def test_social_icons_work_correctly(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    driver.get(base_url)
    login_page.enter_username(username)
    login_page.enter_password(password)
    login_page.click_login()
    inventory_page.open_twitter_and_return()
    inventory_page.open_facebook_and_return()
    inventory_page.open_linkedin_and_return()
    update_test_result(12, status=1)
