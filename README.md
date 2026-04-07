# SmartTest -- UI Automation Testing Framework

## Overview

SmartTest is a lightweight UI automation testing framework built with
Python, Pytest, and Playwright. It demonstrates a maintainable test
architecture using the Page Object Model (POM) design pattern, along
with logging, HTML reporting, and automatic screenshot capture on
failures.

------------------------------------------------------------------------

## Tech Stack

-   Python 3.12
-   Pytest
-   Playwright
-   Page Object Model (POM)
-   HTML Test Reports
-   Logging
-   Automatic Screenshot on Failure

------------------------------------------------------------------------

## Project Structure

smarttest/

config/ config.py

pages/ base_page.py google_page.py saucedemo_login_page.py
saucedemo_inventory_page.py saucedemo_cart_page.py

tests/ test_google_search.py test_saucedemo_login.py
test_saucedemo_add_to_cart.py

utils/ logger.py

reports/ report.html

conftest.py pytest.ini requirements.txt README.md

------------------------------------------------------------------------

## Installation

Create virtual environment:

python3.12 -m venv .venv source .venv/bin/activate

Install dependencies:

pip install -r requirements.txt playwright install

------------------------------------------------------------------------

## Run Tests

pytest -s

------------------------------------------------------------------------

## Generate HTML Report

pytest -s --html=reports/report.html --self-contained-html

Open report:

open reports/report.html

------------------------------------------------------------------------

## Example Test Scenarios

1.  Google Search
    -   Open Google
    -   Enter search keyword
    -   Verify results page loads
2.  SauceDemo Login
    -   Open login page
    -   Submit username and password
    -   Verify successful login
3.  Add Item to Cart
    -   Login to application
    -   Add product to cart
    -   Open cart
    -   Verify item count

------------------------------------------------------------------------

## Future Improvements

-   Parallel test execution
-   CI/CD integration (GitHub Actions)
-   API testing integration
-   Environment configuration
-   Retry mechanism
