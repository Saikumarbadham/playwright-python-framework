from playwright.sync_api import Page


class LoginPage:
    def __init__(self, page: Page):
        self.page = page

        # Locators
        self.username_input = page.locator("#user-name")
        self.password_input = page.locator("#password")
        self.login_button = page.locator("#login-button")
        self.error_message = page.locator("[data-test='error']")

    def navigate(self) -> None:
        self.page.goto("https://www.saucedemo.com/")

    def enter_username(self, username: str) -> None:
        self.username_input.fill(username)

    def enter_password(self, password: str) -> None:
        self.password_input.fill(password)

    def click_login(self) -> None:
        self.login_button.click()

    def login(self, username: str, passw: str) -> None:
        self.enter_username(username)
        self.enter_password(passw)
        self.click_login()

    def get_error_message(self) -> str:
        return self.error_message.inner_text()


   