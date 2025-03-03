from playwright.sync_api import sync_playwright

with sync_playwright() as login:
    browser = login.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://workspace.google.com/intl/en-US/gmail/")
    signinButton = page.wait_for_selector('//span[text()="Sign in"]')
    signinButton.click()
    page.wait_for_timeout(10000)

