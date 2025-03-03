from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://gorest.co.in/chandamama-stories")
    #page.wait_for_timeout(3000)
    Tools_locator = page.get_by_role("button", name="Tools").is_visible()
    page.screenshot(path='test-png', full_page=True)
    Tools_locator1 = page.get_by_role("button", name="Tools").click()
    page.wait_for_timeout(2000)
    Tools_locator2 = page.get_by_text("Url Encode/Decode").click()
    page.wait_for_timeout(3000)