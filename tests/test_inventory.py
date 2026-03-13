import pytest
from playwright.sync_api import sync_playwright

def login(page):
    page.goto("https://www.saucedemo.com")
    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")

def test_inventory_page_loads():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        login(page)
        
        items = page.locator(".inventory_item")
        assert items.count() == 6
        
        browser.close()

def test_sort_by_price_low_to_high():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        login(page)
        
        page.select_option(".product_sort_container", "lohi")
        prices = page.locator(".inventory_item_price").all_text_contents()
        prices = [float(p.replace("$", "")) for p in prices]
        assert prices == sorted(prices)
        
        browser.close()

def test_add_item_to_cart():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        login(page)
        
        page.click("#add-to-cart-sauce-labs-backpack")
        badge = page.locator(".shopping_cart_badge")
        assert badge.text_content() == "1"
        
        browser.close()