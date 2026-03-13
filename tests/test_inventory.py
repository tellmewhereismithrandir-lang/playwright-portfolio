import pytest
from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def test_inventory_page_loads():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        login_page = LoginPage(page)
        login_page.goto()
        login_page.login("standard_user", "secret_sauce")

        inventory_page = InventoryPage(page)
        assert inventory_page.get_item_count() == 6

        browser.close()

def test_sort_by_price_low_to_high():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        login_page = LoginPage(page)
        login_page.goto()
        login_page.login("standard_user", "secret_sauce")

        inventory_page = InventoryPage(page)
        inventory_page.sort_by("lohi")
        prices = inventory_page.get_prices()
        assert prices == sorted(prices)

        browser.close()

def test_add_item_to_cart():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        login_page = LoginPage(page)
        login_page.goto()
        login_page.login("standard_user", "secret_sauce")

        inventory_page = InventoryPage(page)
        inventory_page.add_backpack_to_cart()
        assert inventory_page.get_cart_count() == "1"

        browser.close()