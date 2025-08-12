import pytest
import os
from playwright.sync_api import sync_playwright
from utils.helpers import capture_screenshot
from utils.json_reader import load_json

@pytest.fixture(scope="session")
def browser_context():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False) #Launch browser once for the whole session
        context = browser.new_context()
        yield context
        browser.close()

@pytest.fixture(scope="function")
def setup(request, browser_context):
    page = browser_context.new_page() #Create a fresh page for each test function.
    yield page
    # Capture screenshot if test fails
    if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
        test_name = request.node.name
        capture_screenshot(page, test_name)
    page.close()

def pytest_runtest_makereport(item, call): #Hook to make test result available in fixtures
    outcome = yield
    rep = outcome.get_result()
    setattr(item, f"rep_{rep.when}", rep)

@pytest.fixture(scope="session")
def test_data():
    return load_json("login_data.json") # Load JSON test data for all tests

