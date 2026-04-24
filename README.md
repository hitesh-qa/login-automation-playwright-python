# Login-Automation - Playwright - Python

Automated login and signup testing for automationexercise.com using Playwright + Python + Pytest.

## What This Project Covers
- Valid login test
- Invalid login tests (wrong email, wrong password)
- Empty field validation tests
- Data-driven testing using CSV
- Valid signup automation
- Existing email signup validation

## Tech Stack
- Python 3.14
- Playwright
- pytest

## Project Structure
- pages/ -> Page Object classes (LoginPage, SignupPage)
- tests/ -> Test cases (test_login.py, test_signup.py)
- test_data/ -> CSV test data
- conftest.py -> Browser setup and fixtures

## How to Run 
1. pip install -r requirements.txt
2. playwright install
3. cd mini_login_project
4. pytest tests/ -v

## Test Results
7 tests passing
- 5 login tests (1 positive, 4 negative)
- 2 signup tests (1 positive, 1 negative