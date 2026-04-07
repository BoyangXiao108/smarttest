from pages.base_page import BasePage


class SauceDemoInventoryPage(BasePage):
    def add_backpack_to_cart(self):
        self.page.locator('[data-test="add-to-cart-sauce-labs-backpack"]').click()

    def remove_backpack_from_cart(self):
        self.page.locator('[data-test="remove-sauce-labs-backpack"]').click()

    def open_cart(self):
        self.page.locator('[data-test="shopping-cart-link"]').click()

    def cart_badge_count(self):
        badge = self.page.locator('[data-test="shopping-cart-badge"]')
        if badge.count() == 0:
            return 0
        return int(badge.text_content())