from Pages.Search import DuckDuck_searchPage
from playwright.sync_api import sync_playwright, Page


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    search_page = DuckDuck_searchPage(page)

    search_page.load()

    search_page.search('bhaskar')
