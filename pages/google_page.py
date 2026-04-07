from pages.base_page import BasePage


class GooglePage(BasePage):
    def open(self):
        self.goto("https://www.google.com")

    def search(self, keyword: str):
        self.fill('textarea[name="q"]', keyword)
        self.press('textarea[name="q"]', "Enter")