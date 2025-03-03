import pytest
from playwright.sync_api import sync_playwright, Page


@pytest.fixture(scope='function')
def test_search(page : Page):
    page.goto("https://duckduckgo.com")
    page.wait_for_timeout(2000)
    page.query_selector('//input[@placeholder="Pages without being tracked"]').fill('bhaskar')
    # search = page.query_selector('id="searchbox_input"').fill('bhaskar')
    page.wait_for_timeout(2000)
    page.locator('//button[@type="submit"]').click()
    # search_click = page.locator('type="submit"').click()
    page.wait_for_timeout(2000)
