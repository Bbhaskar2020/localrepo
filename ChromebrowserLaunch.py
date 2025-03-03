from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://workspace.google.com/intl/en-US/gmail/")
    print("Successfully chrome opened")
    print(page.title())
    page.wait_for_timeout(1000)
    browser.close()