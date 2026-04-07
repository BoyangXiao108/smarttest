from pages.base_page import BasePage


class SauceDemoCheckoutPage(BasePage):
    def click_checkout(self):
        self.page.locator('[data-test="checkout"]').click()

    def fill_checkout_info(self, first_name: str, last_name: str, postal_code: str):
        self.fill('[data-test="firstName"]', first_name)
        self.fill('[data-test="lastName"]', last_name)
        self.fill('[data-test="postalCode"]', postal_code)
        self.page.locator('[data-test="continue"]').click()