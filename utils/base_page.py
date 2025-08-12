class Basepage:
    def __init__(self, page):
        self.page = page

    def click(self, selector):
        self.page.click(selector)

    def fill(self, selector, value):
        self.page.fill(selector, value)

    def get_text(self, selector):
        return self.page.text_content(selector)

    def get_page_title(self):
        """Returns the current page title."""
        return self.page.title()