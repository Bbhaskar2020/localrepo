import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope='module')
def browser_handle():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()


@pytest.fixture(scope='function')
def page_handel(browser_handle):
    page = browser_handle.new_page()
    yield page
    page.close()



@pytest.mark.parametrize('valid_user_name, valid_password',[('Admin', 'admin123')])
def test_valid_signIn(page_handel, valid_user_name, valid_password):
    page_handel.goto('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
    page_handel.wait_for_selector('//input[@name="username"]').type(valid_user_name)
    page_handel.wait_for_selector('//input[@name="password"]').type(valid_password)
    page_handel.wait_for_selector('//button[@type="submit"]').click()
    page_handel.wait_for_timeout(3000)
    message = page_handel.get_by_role('heading', name = 'Dashboard').text_content()
    assert 'Dashboard' == message