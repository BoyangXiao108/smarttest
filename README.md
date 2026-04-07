# SmartTest — UI Test Automation Framework

A production-style UI test automation framework built with **Python**, **Pytest**, and **Playwright**, designed to simulate real-world software testing workflows.
The framework implements **Page Object Model (POM)** architecture, structured logging, HTML reporting, failure screenshots, and CI integration using **GitHub Actions**.

This project demonstrates end-to-end automated test coverage for a sample e-commerce application and follows common practices used in QA / SDET environments.

---

# Tech Stack

* Python 3.12
* Pytest
* Playwright
* Page Object Model (POM)
* GitHub Actions (CI)
* HTML Reports
* Logging
* Screenshots on Failure

---

# Project Structure

```
smarttest/
│
├── pages/
│   ├── base_page.py
│   ├── saucedemo_login_page.py
│   ├── saucedemo_inventory_page.py
│   ├── saucedemo_cart_page.py
│   └── saucedemo_checkout_page.py
│
├── tests/
│   ├── test_google_search.py
│   ├── test_saucedemo_login.py
│   ├── test_saucedemo_invalid_login.py
│   ├── test_saucedemo_add_to_cart.py
│   ├── test_saucedemo_remove_from_cart.py
│   └── test_saucedemo_checkout.py
│
├── utils/
│   └── logger.py
│
├── test_data/
│   └── test_data.py
│
├── reports/
│   ├── report.html
│   └── screenshots/
│
├── pytest.ini
├── requirements.txt
└── README.md
```

---

# Key Features

## Page Object Model (POM)

Encapsulates UI elements and actions into reusable page classes to improve:

* Maintainability
* Readability
* Scalability
* Test stability

Example:

```
login_page.login(username, password)
inventory_page.add_backpack_to_cart()
checkout_page.click_finish()
```

---

## Smoke and Regression Test Suites

Tests are organized using Pytest markers.

Smoke tests:

```
pytest -m smoke
```

Regression tests:

```
pytest -m regression
```

Example marker:

```
@pytest.mark.smoke
def test_saucedemo_login(page):
```

---

## Logging

Structured logging helps debugging and traceability.

Example log output:

```
INFO - Start SauceDemo login test
INFO - Opened SauceDemo login page
INFO - Submitted login credentials
INFO - Login succeeded
```

Logger location:

```
utils/logger.py
```

---

## HTML Test Report

Automatically generated after each test run.

Command:

```
pytest --html=reports/report.html --self-contained-html
```

Output:

```
reports/report.html
```

The report includes:

* Test results
* Execution time
* Pass / Fail status
* Failure details

---

## Screenshot on Failure

Automatically captures screenshots when a test fails.

Saved to:

```
reports/screenshots/
```

This behavior simulates production QA debugging workflows.

---

# Test Scenarios Covered

The framework includes automated UI tests for the following user flows:

* Google search validation
* User login
* Invalid login
* Add item to cart
* Remove item from cart
* Checkout process
* Order completion confirmation

Example checkout flow:

```
Login
→ Add product
→ Open cart
→ Checkout
→ Fill information
→ Complete order
→ Verify success message
```

---

# Installation

Clone the repository:

```
git clone https://github.com/BoyangXiao108/smarttest.git
cd smarttest
```

Create virtual environment:

```
python3.12 -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```
pip install -r requirements.txt
```

Install Playwright browser:

```
playwright install
```

---

# Run Tests

Run all tests:

```
pytest
```

Run smoke tests only:

```
pytest -m smoke
```

Run regression tests:

```
pytest -m regression
```

Run tests with HTML report:

```
pytest --html=reports/report.html --self-contained-html
```

---

# Continuous Integration (CI)

GitHub Actions automatically runs smoke tests on:

* push
* pull request

Workflow file:

```
.github/workflows/tests.yml
```

CI performs:

* dependency installation
* browser setup
* test execution
* report generation
* artifact upload

This simulates real-world automated testing pipelines.

---

# Example CI Workflow

```
Push code
    ↓
GitHub Actions triggered
    ↓
Install dependencies
    ↓
Run smoke tests
    ↓
Generate report
    ↓
Upload artifacts
```

---

# Future Improvements

Potential enhancements:

* Parallel test execution
* Test retry mechanism
* API testing integration
* Docker test environment
* Test data parameterization
* Allure reporting
* Performance testing
* Headless execution optimization

---

# Author

Boyang Xiao
Master of Science in Computer Science
Boston University
Expected Graduation: May 2026

---

# Purpose of This Project

This project demonstrates practical experience in:

* Software testing
* Test automation
* Framework design
* CI/CD workflows
* Debugging and reporting
* Maintainable test architecture

It is intended to showcase real-world engineering practices for entry-level QA, SDET, and automation roles.
