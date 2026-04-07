from pages.saucedemo_login_page import SauceDemoLoginPage
from pages.saucedemo_inventory_page import SauceDemoInventoryPage
from pages.saucedemo_cart_page import SauceDemoCartPage
from config.config import USERNAME, PASSWORD
from utils.logger import get_logger


logger = get_logger(__name__)


def test_saucedemo_add_to_cart(page):
    logger.info("Start add-to-cart test")

    login_page = SauceDemoLoginPage(page)
    inventory_page = SauceDemoInventoryPage(page)
    cart_page = SauceDemoCartPage(page)

    login_page.open()
    login_page.login(USERNAME, PASSWORD)
    login_page.wait_for_url_contains("inventory")
    logger.info("Login succeeded")

    inventory_page.add_backpack_to_cart()
    logger.info("Added backpack to cart")

    inventory_page.open_cart()
    cart_page.wait_for_url_contains("cart")
    logger.info("Opened cart page")

    assert cart_page.cart_item_count() == 1