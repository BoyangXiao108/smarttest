import pytest
from pages.saucedemo_login_page import SauceDemoLoginPage
from utils.logger import get_logger


logger = get_logger(__name__)

@pytest.mark.regression
@pytest.mark.parametrize(
    "username, password",
    [
        ("locked_out_user", "wrong_password"),
        ("standard_user", "wrong_password"),
        ("", "secret_sauce"),
        ("standard_user", ""),
    ],
)
def test_saucedemo_invalid_login(page, username, password):
    logger.info("Start invalid login test")

    login_page = SauceDemoLoginPage(page)
    login_page.open()

    login_page.login(username, password)

    error_text = login_page.error_message()
    logger.info(f"Error message: {error_text}")

    assert "Epic sadface" in error_text