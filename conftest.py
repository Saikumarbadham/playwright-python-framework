from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
import pytest


@pytest.fixture
def login(page: Page):

    login_page = LoginPage(page)

    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")

    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

    page.wait_for_load_state("networkidle")

    yield page