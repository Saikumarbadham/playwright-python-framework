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


@pytest.fixture(scope="function",autouse="True")
def auth(browser):

    context = browser.new_context()
    page = context.new_page()

    page.goto("https://www.saucedemo.com/")

    page.locator("#user-name").fill("standard_user")
    page.locator("#password").fill("secret_sauce")
    page.locator("#login-button").click()

    page.wait_for_url("**/inventory.html")

    context.storage_state(path="auth.json")

    yield page

    context.close()