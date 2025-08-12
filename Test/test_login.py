import pytest
from Pages.login_page import LoginPage
from utils.json_reader import load_json

test_data = load_json("login_data.json")

@pytest.mark.parametrize("username", "password", [test_data, ["valid_login"]["username"]
                                                  test_data, ["valid_login"]["password"]])


def test_valid_login(setup, username, password):
    page = setup
    login = LoginPage(page)
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    login.login(username, password)
    assert "Dashboard" in login.get_dashboard_text()