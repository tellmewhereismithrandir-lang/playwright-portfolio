import pytest
from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage

def test_valid_login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        login_page = LoginPage(page)
        login_page.goto()
        login_page.login("standard_user", "secret_sauce")
        
        assert page.url == "https://www.saucedemo.com/inventory.html"
        
        browser.close()

def test_locked_out_user():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        login_page = LoginPage(page)
        login_page.goto()
        login_page.login("locked_out_user", "secret_sauce")
        
        assert login_page.get_error().is_visible()

        browser.close()

def test_wrong_password():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        login_page = LoginPage(page)
        login_page.goto()
        login_page.login("standard_user", "wrongpassword")
        
        assert login_page.get_error().is_visible()
        
        browser.close()