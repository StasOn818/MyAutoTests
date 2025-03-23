import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions

@pytest.fixture
def driver(request):
    browser = request.config.getoption("--browser")
    headless = request.config.getoption("--headless").lower() == "true"

    if browser == "chrome":
        options = ChromeOptions()
        if headless:
            options.add_argument("--headless")
            options.add_argument("--disable-gpu")
            options.add_argument("--window-size=1920x1080")
        driver = webdriver.Chrome(options=options)

    elif browser == "firefox":
        driver = webdriver.Firefox()

    elif browser == "safari":
        driver = webdriver.Safari()

    else:
        raise ValueError(f"Unsupported browser: {browser}. Choose chrome, firefox or safari.")

    yield driver
    driver.quit()

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Choose browser: chrome, firefox, safari")
    parser.addoption("--headless", action="store", default="false", help="Run Chrome in headless mode (true/false)")












