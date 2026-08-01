from playwright.sync_api import sync_playwright

def test_google_search():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://www.saucedemo.com/?utm_source=chatgpt.com")

        page.locator('textarea[name="q"]').fill("Playwright Python")
        page.keyboard.press("Enter")

        page.wait_for_load_state("networkidle")

        assert "Playwright Python" in page.title()

        browser.close()
        