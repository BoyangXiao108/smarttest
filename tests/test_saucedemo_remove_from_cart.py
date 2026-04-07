import pytest
from pages.saucedemo_login_page import SauceDemoLoginPage
from pages.saucedemo_inventory_page import SauceDemoInventoryPage
from test_data.test_data import LOGIN_USERNAME, LOGIN_PASSWORD
from utils.logger import get_logger


logger = get_logger(__name__)

@pytest.mark.regression
def test_saucedemo_remove_from_cart(page):
    logger.info("Start remove-from-cart test")

    login_page = SauceDemoLoginPage(page)
    inventory_page = SauceDemoInventoryPage(page)

    login_page.open()
    login_page.login(LOGIN_USERNAME, LOGIN_PASSWORD)
    login_page.wait_for_url_contains("inventory")
    logger.info("Login succeeded")

    inventory_page.add_backpack_to_cart()
    logger.info("Added backpack to cart")
    assert inventory_page.cart_badge_count() == 1

    inventory_page.remove_backpack_from_cart()
    logger.info("Removed backpack from cart")
    assert inventory_page.cart_badge_count() == 0