# Automation Testing Pet Project

This is a personal automation testing project designed to demonstrate proficiency in automated testing for both **web applications** and **APIs**. The project includes end-to-end (E2E) tests for a web application and API tests, integrated with **TestRail** for test case management and **Allure Report** for detailed reporting. It serves as a continuously evolving sandbox to explore and implement best practices in test automation.



---

## Project Overview

The project consists of two main testing modules:
1. **Web Testing**:
   - **Target**: [SauceDemo](https://www.saucedemo.com/) - a demo e-commerce website.
   - **Purpose**: End-to-end (E2E) testing of user workflows such as login, product selection, cart management, and checkout.
   - **Tools**: Selenium WebDriver with Python for browser automation.

2. **API Testing**:
   - **Target**: [TMDb API](https://www.themoviedb.org/) - The Movie Database API.
   - **Purpose**: Testing API endpoints for movies, TV shows, search functionality, and authenticated actions (e.g., rating movies).
   - **Tools**: Python with `requests` library for API interactions.

---

## Features

- **Web E2E Tests**:
  - Automated login with valid/invalid credentials.
  - Product browsing, adding to cart, and checkout processes.
  - Validation of UI elements and user interactions.

- **API Tests**:
  - Testing GET endpoints (e.g., popular movies, movie details).
  - Testing POST and DELETE endpoints (e.g., rating movies) with v4 Access Token authentication.
  - Parameterized tests for multiple scenarios.

- **Logging**:
  - Comprehensive logging for both web and API tests.
  - Logs are written to `logs/` directory and displayed in the console with timestamps, levels (INFO, ERROR), and detailed messages.

- **TestRail Integration**:
  - Test cases are synchronized with TestRail for tracking and management.
  - Automated updates of test results after test runs.
  - A link to the test cases in TestRail is available for reference:https://drive.google.com/drive/folders/1zGJvJS1KQKHKXvgl8JQja4BvzR3ssBAd?usp=drive_link.
    This is a link to my storage google drive, where you can find two folders. Each folder contains screenshots of my project's test cases in Testrail and a .csv file that can be imported into TestRail.


- **Allure Report Integration**:
  - Detailed test reports with steps, screenshots (for web), request/response details (for API), and pass/fail statuses.
  - Generated after each test run for easy analysis. End.

---
