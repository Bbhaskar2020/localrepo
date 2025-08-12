from playwright.sync_api import Page
from typing import List


class duckResultPage:

    def __init__(self, page: Page):
        self.page = page
        self.result = page.locator('//input[@id="search_form_input"]')
        self.result_display = page.locator('//input[@id="search_form_input"]')