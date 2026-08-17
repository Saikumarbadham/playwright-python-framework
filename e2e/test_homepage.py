
# from playwright.sync_api import expect
# from pages.dash_board import DashboardPage
from playwright.sync_api import Page,playwright
from playwright.sync_api import expect
import pytest
from playwright.async_api import async_playwright

# class home:
#  def test_homepage(login):

#     dashboard = DashboardPage(login)

#     dashboard.click_menu()

#     expect(dashboard.logout_link).to_be_visible()

# def testpage(page:Page):

#   page.locator("#add-to-cart-sauce-labs-backpack").click()
#   page.locator('[data-test="shopping-cart-link"]').click()
#   page.locator(".btn btn_action btn_medium checkout_button").click()
#   fill_the_name= page.get_by_placeholder('First Name').type("sai")
#   fill_the_name.fill("ssddfd",delay=200)
#   fill_the_name.clear 
#   page.get_by_text('').click()
#   page.get_by_test_id('').click()
#   page.get_by_label('').click()
#   page.get_by_role("link",name="jgugig").nth(1).click()
#   page.locator("button").first.click()
#   page.locator("button").press("BackSpace")
#   product = page.locator(".product").filter(
#     has_text="Laptop")
#   product.get_by_role("button",name="add_to_cart").click()

#   # actions
#   page.locator("#product-sort-container").select_option("Name (A to Z)")


def test_file_upload(page:Page):
   page.goto("https://commitquality.com/practice-file-upload")
   file_path=r"C:\Users\RK REDDY\Downloads\sample.pdf"
   page.get_by_test_id("file-input").set_input_files(file_path)
   page.wait_for_load_state("domcontentloaded")
   # expect(page.get_by_text("sample.pdf)).to_be_visible
   page.get_by_role("button",name="Submit").click()

def test_radio_button(page:Page):
   page.goto("https://commitquality.com/practice")
   expect(page).to_have_url("https://commitquality.com/practice")
   page.get_by_text("Radio Buttons ").click()
   page.get_by_test_id("option1").click()
   expect(page.get_by_test_id("option1")).to_be_checked()
   expect(page.get_by_test_id("option2")).not_to_be_checked()
    
def test_assertions(page:Page):
   page.goto("https://www.saucedemo.com/")
   page.wait_for_url("https://www.saucedemo.com/")
   page.wait_for_timeout(15000)
   expect(page).to_have_url("https://www.saucedemo.com/")   
   expect(page).to_have_title("Swag Labs")
   usernames = page.locator("#user-name")
   expect(usernames).to_be_visible()
   expect(usernames).to_be_enabled()
   usernames.fill("standard_user")
   expect(usernames).to_have_value("standard_user")
   passd= page.get_by_placeholder("Password")
   passd.fill("secret_sauce")
   expect(passd).to_be_visible()
   login_button = page.locator("#login-button")
   expect(login_button).to_be_visible()
   expect(login_button).to_be_enabled()
   login_button.click()
   expect(page).to_have_url(
        "https://www.saucedemo.com/inventory.html"
    )

   expect(page.get_by_text("Products")).to_be_visible()

def test_iframesd(page:Page):
   page.goto("https://commitquality.com/practice")
   page.get_by_text("Iframes", exact=True).click()
   frame = page.frame_locator("iframe")
   frame.get_by_placeholder("Filter by product name").fill("hiuuh")
   frame.locator(".filter-button").nth(0).click()

def test_accordion(page: Page):
    page.goto("https://www.geeksforgeeks.org/computer-networks/web-pages/")

    accordion = page.get_by_role("button", name="Computer Networks")
    accordion.click()

    expect(page.get_by_text("Web Pages")).to_be_visible()

def test_get(playwright:playwright):
   request=playwright.request.new_context(

      base_url="https://jsonplaceholder.typicode.com"
   )
   response=request.get("/users/1")
   print(response.json())
   print(response.status)
   request.dispose

def test_post(playwright:playwright):
   request=playwright.request.new_context(
   
         base_url="https://jsonplaceholder.typicode.com"
      )
   response=request.patch("/users/1", data={
      "name": "Saik",
      "role": "QA Engineers"

   })
   assert response.status == 200

   # data = response.json()

   # assert data["name"] == "Saik"

   # request.dispose()








   
   