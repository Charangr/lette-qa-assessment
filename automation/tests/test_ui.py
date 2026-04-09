from playwright.sync_api import Page
from pages.login_page import LoginPage

def test_login(page: Page):
    # use page object model
    login = LoginPage(page)

    login.open()
    login.login("tomsmith", "SuperSecretPassword!")

    message = page.locator("#flash").text_content()

    # verify login success
    assert "You logged into a secure area!" in message