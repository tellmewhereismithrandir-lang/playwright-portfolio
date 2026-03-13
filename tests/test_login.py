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
        print("Login successful!")
        page.wait_for_timeout(3000)  # waits 3 seconds before closing
        
        browser.close()