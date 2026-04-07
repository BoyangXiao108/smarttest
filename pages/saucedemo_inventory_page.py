from pages.base_page import BasePage


class SauceDemoInventoryPage(BasePage):
    def add_backpack_to_cart(self):
        self.page.locator('[data-test="add-to-cart-sauce-labs-backpack"]').click()

    def open_cart(self):
        self.page.locator('[data-test="shopping-cart-link"]').click()