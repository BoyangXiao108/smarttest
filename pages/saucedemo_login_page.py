from pages.base_page import BasePage
from config.config import BASE_URL


class SauceDemoLoginPage(BasePage):
    def open(self):
        self.goto(BASE_URL)

    def login(self, username: str, password: str):
        self.fill('[data-test="username"]', username)
        self.fill('[data-test="password"]', password)
        self.page.locator('[data-test="login-button"]').click()