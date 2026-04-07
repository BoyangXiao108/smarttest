import pytest
from pages.google_page import GooglePage
from test_data.test_data import GOOGLE_SEARCH_KEYWORD

@pytest.mark.regression
def test_google_search(page):
    google_page = GooglePage(page)
    google_page.open()
    google_page.search(GOOGLE_SEARCH_KEYWORD)
    google_page.wait_for_url_contains("search")
    assert "search" in google_page.get_url().lower()