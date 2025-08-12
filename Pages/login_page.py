from locators.xpath_locators import login_locators
from utils.base_page import Basepage

class LoginPage(Basepage):
    def __init__(self, page):
        super().__init__(page)

    def login(self, username, password):
        self.page.fill(login_locators.user_name, username)
        self.page.fill(login_locators.user_pass, password)
        self.page.click(login_locators.login_button)

    def get_dashboard_text(self):
        return self.page.text_content(LoginLocators.DASHBOARD_HEADER)
