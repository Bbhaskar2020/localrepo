from playwright.sync_api import sync_playwright


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("www.google.com")
    radio_button = page.query_selector("xpath")
    radio_button.click()
    # radio_button.check()
    if radio_button.is_checked():
        print("Radio button checked")
    else:
        print("Radio button not checked")

    check_box = page.query_selector("xpath")
    check_box.check()
    check_box.click()
    if check_box.is_checked():
        print("Check box is checked..")
    else:
        print("checked box is not checked")