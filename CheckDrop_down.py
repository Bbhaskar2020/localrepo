from playwright.sync_api import sync_playwright


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://demo.automationtesting.in/register.hrml")
    select_dropdown = page.query_selector('//select[@id='skills']')
    select_dropdown.select_option(label='Art Design')
    page.wait_for_timeout(4000)

    # page.select_option('//select[@id='skills']', label='Art Design')
