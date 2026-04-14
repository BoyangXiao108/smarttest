from pages.base_page import BasePage


class SauceDemoCheckoutPage(BasePage):
    def fill_checkout_info(self, first_name: str, last_name: str, postal_code: str):
        self.fill('[data-test="firstName"]', first_name)
        self.fill('[data-test="lastName"]', last_name)
        self.fill('[data-test="postalCode"]', postal_code)
        self.page.locator('[data-test="continue"]').click()

    def click_finish(self):
        self.page.locator('[data-test="finish"]').click()

    def complete_header_text(self):
        return self.page.locator('[data-test="complete-header"]').text_content()