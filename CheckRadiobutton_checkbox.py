from playwright.sync_api import sync_playwright


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://demo.automationtesting.in/register.hrml")
    radiobutton = page.locator('//input[@value="Female"]')
    # click and checked
    #radiobutton.click()
    radiobutton.check()
    if radiobutton.is_checked():
        print("Passed")
    else:
        print("Failed")
    page.wait_for_timeout(3000)

    # checkbox
    checkbox = page.locator('//input[@value="cricket"]')
    checkbox.click()
    if checkbox.is_checked():
        print("Passed")
    else:
        print("Failed")

