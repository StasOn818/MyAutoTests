import pytest
import allure
from src.web.pages.base_page import BasePage
from src.web.pages.login_page import LoginPage
from src.utils.testrail_integration import update_test_result
from src.web.config.config import base_url, password, username, incorrect_data

@pytest.mark.testrail(id="4")
@allure.severity('critical')
@allure.story('User login with correct Credentials')
def test_user_login_with_correct_data(driver):
    base_page = BasePage(driver)
    login_page = LoginPage(driver)
    driver.get(base_url)
    login_page.enter_username(username)
    login_page.enter_password(password)
    login_page.click_login()

    with allure.step('The user successfully logs in'):
        assert "inventory" in driver.current_url

    base_page.is_text_present("Products")
    update_test_result(4, status=1)

@pytest.mark.testrail(id="5")
@allure.story('User login with incorrect password')
@allure.severity('critical')
def test_user_login_with_incorrect_password(driver):
    base_page = BasePage(driver)
    login_page = LoginPage(driver)
    driver.get(base_url)
    login_page.enter_username(username)
    login_page.enter_password(incorrect_data)
    login_page.click_login()

    with allure.step('An error message appears'):
        assert base_page.is_text_present(login_page.error_message), f"Text '{login_page.error_message}' not found on the page!"

    update_test_result(5, status=1)

@pytest.mark.testrail(id="6")
@allure.story('User login with incorrect username')
@allure.severity('critical')
def test_user_login_with_incorrect_login(driver):
    base_page = BasePage(driver)
    login_page = LoginPage(driver)
    driver.get(base_url)
    login_page.enter_username(incorrect_data)
    login_page.enter_password(password)
    login_page.click_login()

    with allure.step('An error message appears'):
        assert base_page.is_text_present(
    login_page.error_message), f"Text '{login_page.error_message}' not found on the page!"

    update_test_result(6, status=1)

