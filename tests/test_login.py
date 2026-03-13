import pytest
from playwright.sync_api import sync_playwright

def test_valid_login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        page.goto("https://www.saucedemo.com")
        page.fill("#user-name", "standard_user")
        page.fill("#password", "secret_sauce")
        page.click("#login-button")
        
        assert page.url == "https://www.saucedemo.com/inventory.html"
        
        browser.close()

def test_locked_out_user():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        page.goto("https://www.saucedemo.com")
        page.fill("#user-name", "locked_out_user")
        page.fill("#password", "secret_sauce")
        page.click("#login-button")
        
        error = page.locator("[data-test='error']")
        assert error.is_visible()
        
        browser.close()

def test_wrong_password():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        page.goto("https://www.saucedemo.com")
        page.fill("#user-name", "standard_user")
        page.fill("#password", "wrongpassword")
        page.click("#login-button")
        
        error = page.locator("[data-test='error']")
        assert error.is_visible()
        
        browser.close()