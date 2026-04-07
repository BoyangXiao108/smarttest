class BasePage:
    def __init__(self, page):
        self.page = page

    def goto(self, url: str):
        self.page.goto(url)

    def fill(self, selector: str, value: str):
        self.page.locator(selector).fill(value)

    def press(self, selector: str, key: str):
        self.page.locator(selector).press(key)

    def get_title(self):
        return self.page.title()

    def get_url(self):
        return self.page.url

    def wait_for_url_contains(self, text: str):
        self.page.wait_for_url(f"**{text}**")

    def wait_for_selector(self, selector: str):
        self.page.locator(selector).wait_for()