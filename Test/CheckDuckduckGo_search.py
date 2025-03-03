from playwright.sync_api import sync_playwright, expect


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://duckduckgo.com/")
    page.wait_for_timeout(2000)
    page.query_selector('//input[@placeholder="Pages without being tracked"]').fill('bhaskar')
    # search = page.query_selector('id="searchbox_input"').fill('bhaskar')
    page.wait_for_timeout(2000)
    page.locator('//button[@type="submit"]').click()
    # search_click = page.locator('type="submit"').click()
    page.wait_for_timeout(2000)
    expect(page.locator('//input[@id="search_form_input"]')).to_have_value('bhaskar')
    print("Yes value is 'bhaskar'  ")
    assert 'bhaskar' == page.input_value('//input[@id="search_form_input"]')
    print("Yes assertion passed  ")