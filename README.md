# SmartTest --- Test Automation Framework

A production-style test automation framework built with **Python**,
**Pytest**, and **Playwright**, designed to simulate real-world QA and
SDET workflows.

The framework supports both **UI and API testing**, parallel execution,
automatic retry for flaky tests, structured logging, HTML and coverage
reporting, Docker-based execution, and CI integration using **GitHub
Actions**.

This project demonstrates end-to-end automated test coverage for a
sample e-commerce application and follows common engineering practices
used in modern test automation environments.

------------------------------------------------------------------------

# Tech Stack

-   Python 3.12\
-   Pytest\
-   Playwright\
-   Requests (API testing)\
-   Page Object Model (POM)\
-   Pytest-xdist (parallel execution)\
-   Pytest-rerunfailures (retry logic)\
-   Pytest-cov (coverage reporting)\
-   Docker\
-   GitHub Actions (CI)

------------------------------------------------------------------------

# Key Features

## UI and API Test Automation

The framework supports:

-   UI automation using Playwright
-   API testing using Requests
-   Unified execution using Pytest

Example:

    pytest

This runs:

-   UI test suites
-   API tests
-   Coverage reporting
-   HTML reporting
-   Parallel execution
-   Retry logic

------------------------------------------------------------------------

## Parallel Test Execution

Tests run concurrently using:

    pytest -n 2

Benefits:

-   Faster regression cycles\
-   Real-world CI performance simulation

------------------------------------------------------------------------

## Retry Mechanism for Flaky Tests

Automatically reruns failed tests:

    --reruns 1

Benefits:

-   Improved stability\
-   Reduced false failures

------------------------------------------------------------------------

## Test Coverage Reporting

Code coverage is automatically generated:

    pytest

Output:

    reports/coverage/index.html

Current coverage:

    98%

------------------------------------------------------------------------

## Docker-Based Test Execution

Build:

    docker build -t smarttest .

Run:

    docker run --rm smarttest

Benefits:

-   Environment consistency\
-   CI compatibility\
-   Production-style execution

------------------------------------------------------------------------

# Project Structure

    smarttest/
    │
    ├── pages/
    ├── tests/
    ├── utils/
    ├── test_data/
    ├── reports/
    ├── Dockerfile
    ├── pytest.ini
    ├── requirements.txt
    └── README.md

------------------------------------------------------------------------

# Test Scenarios Covered

UI workflows:

-   User login\
-   Invalid login\
-   Add item to cart\
-   Remove item from cart\
-   Checkout process

API workflows:

-   Retrieve post data
-   Validate JSON response structure
-   Validate response status

------------------------------------------------------------------------

# Installation

Clone repository:

    git clone https://github.com/BoyangXiao108/smarttest.git
    cd smarttest

Create virtual environment:

    python3.12 -m venv .venv
    source .venv/bin/activate

Install dependencies:

    pip install -r requirements.txt

Install browser:

    playwright install

------------------------------------------------------------------------

# Run Tests

Run all tests:

    pytest

Run in parallel:

    pytest -n 2

Run with Docker:

    docker build -t smarttest .
    docker run --rm smarttest

------------------------------------------------------------------------

# Author

Boyang Xiao\
Master of Science in Computer Science\
Boston University\
Expected Graduation: May 2026
