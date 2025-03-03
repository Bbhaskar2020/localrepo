import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="module")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()

@pytest.fixture(scope="function")
def page(browser):
    page = browser.new_page()
    yield page
    page.close()


def test_goRest(page):
    page.goto("https://gorest.co.in/chandamama-stories")
    page.wait_for_timeout(3000)
    assert 'Chandamama Stories | GO REST' == page.title()


def test_goGoogle(page):
    page.goto("https://www.google.com")
    assert 'Google' == page.title()


def test_gotoRedBus(page):
    page.goto("https://www.redbus.com/")
    assert 'Book Bus Tickets Online with redBus!' == page.title()