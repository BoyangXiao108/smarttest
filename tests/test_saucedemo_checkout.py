import pytest
from pages.saucedemo_login_page import SauceDemoLoginPage
from pages.saucedemo_inventory_page import SauceDemoInventoryPage
from pages.saucedemo_cart_page import SauceDemoCartPage
from pages.saucedemo_checkout_page import SauceDemoCheckoutPage
from test_data.test_data import (
    LOGIN_USERNAME,
    LOGIN_PASSWORD,
    CHECKOUT_FIRST_NAME,
    CHECKOUT_LAST_NAME,
    CHECKOUT_POSTAL_CODE,
)
from utils.logger import get_logger


logger = get_logger(__name__)

@pytest.mark.smoke
def test_saucedemo_checkout(page):
    logger.info("Start checkout test")

    login_page = SauceDemoLoginPage(page)
    inventory_page = SauceDemoInventoryPage(page)
    cart_page = SauceDemoCartPage(page)
    checkout_page = SauceDemoCheckoutPage(page)

    login_page.open()
    login_page.login(LOGIN_USERNAME, LOGIN_PASSWORD)
    login_page.wait_for_url_contains("inventory")

    inventory_page.add_backpack_to_cart()
    inventory_page.open_cart()
    cart_page.wait_for_url_contains("cart")

    assert cart_page.cart_item_count() == 1

    cart_page.click_checkout()
    checkout_page.wait_for_url_contains("checkout-step-one")

    checkout_page.fill_checkout_info(
        CHECKOUT_FIRST_NAME,
        CHECKOUT_LAST_NAME,
        CHECKOUT_POSTAL_CODE,
    )
    checkout_page.wait_for_url_contains("checkout-step-two")

    assert "checkout-step-two" in checkout_page.get_url().lower()