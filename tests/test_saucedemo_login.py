import pytest
from pages.saucedemo_login_page import SauceDemoLoginPage
from test_data.test_data import LOGIN_USERNAME, LOGIN_PASSWORD
from utils.logger import get_logger


logger = get_logger(__name__)

@pytest.mark.smoke
def test_saucedemo_login(page):
    logger.info("Start SauceDemo login test")

    login_page = SauceDemoLoginPage(page)
    login_page.open()
    logger.info("Opened SauceDemo login page")

    login_page.login(LOGIN_USERNAME, LOGIN_PASSWORD)
    logger.info("Submitted login credentials")

    login_page.wait_for_url_contains("inventory")
    logger.info("Login succeeded, inventory page loaded")

    assert "inventory" in login_page.get_url().lower()