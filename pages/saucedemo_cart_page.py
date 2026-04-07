from pages.base_page import BasePage


class SauceDemoCartPage(BasePage):
    def cart_item_count(self):
        return self.page.locator('[data-test="inventory-item"]').count()