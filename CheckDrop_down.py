from playwright.sync_api import sync_playwright


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("www.google.com")
    page.select_option("drop-down xapath", label='text')
    page.wait_for_timeout(2000)
