import os
from dotenv import load_dotenv
from playwright.sync_api import Page

# Load the variables from .env
load_dotenv()

class LoginPageSync:
    def __init__(self, page: Page):
        self.page = page
        # Get the URL from .env, fallback to a default if missing
        self.url = os.getenv("BASE_URL", "https://www.saucedemo.com/")
        
        # Locators
        self.username_field = page.locator("#user-name")
        self.password_field = page.locator("#password")
        # Keep this as "#wrong-button" for now to test the AI healing!
        self.login_button = page.locator("#wrong-button") 

    def navigate(self):
        self.page.goto(self.url)

    def login(self, username, password):
        self.username_field.fill(username)
        self.password_field.fill(password)
        self.login_button.click()