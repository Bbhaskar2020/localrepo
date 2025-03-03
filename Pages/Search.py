from playwright.sync_api import Page

class DuckDuck_searchPage:
    url = 'https://duckduckgo.com'

    def __init__(self, page: Page):
        self.page = page
        self.searchInput = page.locator('//input[@placeholder="Search without being tracked"]')
        self.searchButton = page.locator('//button[@type="submit"]')
    def load(self):
        self.page.goto(self.url)
    def search(self, phrase: str):
        self.searchInput.fill(phrase)
        self.searchButton.click()


