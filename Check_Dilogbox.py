from playwright.sync_api import sync_playwright
text_alert = []


def print_dialog(dialog):
    message = dialog.message
    text_alert.append(message)
    dialog.dismiss() #dismiss means clicking on cancel button on dialog pop-up
    # dialog.accept() #accept means clicking on OK button on dialog pop-up


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://demo.automationtesting.in/Alerts.html")
    # page.wait_for_selector('//div[@id="OKTab"]/button').click()
    page.wait_for_selector('//a[@href="#CancelTab"]').click()
    page.wait_for_timeout(2000)
    # contraol alert
    # page.on("dialog", lambda dialog: dialog.accept()) #dismiss means clicking on OK button on dialog pop-up
    # page.on("dialog", lambda dialog : dialog.dismiss()) #dismiss means clicking on cancel button on dialog pop-up
    # page.on("dialog", lambda dialog: print(dialog.message) #dismiss means clicking on cancel button on dialog pop-up
    page.on("dialog", print_dialog) #this line means calling the method print_dialog to print the message on dialog pop-up
    page.wait_for_selector('//div[@id="CancelTab"]/button').click()
    page.wait_for_timeout(2000)
    print(text_alert[0])