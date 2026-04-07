from pages.google_page import GooglePage


def test_google_search(page):
    google_page = GooglePage(page)
    google_page.open()
    google_page.search("Playwright Python")
    google_page.wait_for_url_contains("search")
    assert "search" in google_page.get_url().lower()