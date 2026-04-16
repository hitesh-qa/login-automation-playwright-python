import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as playwright:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()

@pytest.fixture(scope="function")
def page(browser):
    page = browser.new_page()
    page.goto("https://www.automationexercise.com")
    yield page
    page.close()


#browser fixture -> opens chrome once for all tests
#page fixture -> opens a new tab for each test and goes to the site
#headleass = False -> you can see the browser running during tests