from playwright.sync_api import Page


class DashboardPage:

    def __init__(self, page: Page):
        self.page = page

        self.page_title = page.locator(".title")
        self.shopping_cart = page.locator(".shopping_cart_link")
        self.menu_button = page.locator("#react-burger-menu-btn")
        self.logout_link = page.locator("#logout_sidebar_link")
        self.sort_dropdown = page.locator(".product_sort_container")
        self.first_add_to_cart = page.locator("button[id^='add-to-cart']")

    def verify_dashboard_loaded(self):
        return self.page_title.inner_text()

    def click_menu(self):
        self.menu_button.click()

    def logout(self):
        self.click_menu()
        self.logout_link.click()

    def open_cart(self):
        self.shopping_cart.click()

    def sort_products(self, value):
        self.sort_dropdown.select_option(value)

    def add_first_product(self):
        self.first_add_to_cart.first.click()