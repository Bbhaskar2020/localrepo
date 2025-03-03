from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://gorest.co.in/chandamama-stories")
    HindiStoryTile = page.wait_for_selector('//p[text()="Read amazing stories in hindi language"]').is_visible()
    page.wait_for_timeout(3000)


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('https://gorest.co.in/chandamama-stories')

