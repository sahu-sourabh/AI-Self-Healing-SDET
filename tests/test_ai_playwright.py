import pytest
import asyncio
import re
import os
from concurrent.futures import ThreadPoolExecutor
from playwright.sync_api import Page
from pages.login_page_sync import LoginPageSync
from app.agent_logic import get_ai_fix
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

def test_login_with_ai_fallback(page: Page):
    """
    Architect Strategy:
    1. Environment Agnostic: Pulls credentials from .env via os.getenv.
    2. Resilience: Uses AI to heal the login flow if locators fail.
    3. Thread Isolation: Bypasses Windows asyncio conflicts.
    """
    # Pull credentials from environment
    user = os.getenv("SAUCE_USERNAME")
    pw = os.getenv("SAUCE_PASSWORD")
    
    login_page = LoginPageSync(page)
    
    print("\n🚀 Starting UI Test (Environment-Aware)...")
    login_page.navigate()

    try:
        print(f"🔍 Attempting initial login for user: {user}")
        # Attempt login with credentials from .env
        login_page.login(user, pw)
        
        # Verify if we reached the inventory page
        page.wait_for_url("**/inventory.html", timeout=5000)
        
    except Exception as e:
        print(f"❌ UI Action Failed: Locator not found or timeout.")
        print("🤖 Triggering AI Self-Healing via Threaded Bridge...")
        
        # 1. Capture the DOM state (3000 chars for context)
        html_snippet = page.content()
        
        # 2. Execute AI logic in an isolated thread
        with ThreadPoolExecutor() as executor:
            future = executor.submit(
                lambda: asyncio.run(get_ai_fix("Playwright UI", "#wrong-button", html_snippet[:3000]))
            )
            suggestion = future.result()

        print(f"📝 AI Raw Suggestion: {suggestion}")

        # 3. EXTRACTION: Find the healed locator in double brackets [[ ]]
        matches = re.findall(r'\[\[(.*?)\]\]', suggestion)
        
        if matches and matches[-1] != "NONE":
            new_selector = matches[-1]
            print(f"🛠️ Self-Healing in progress... Attempting recovery with: {new_selector}")
            
            # 4. RECOVERY: Re-perform the login using the suggested locator
            try:
                page.fill("#user-name", user)
                page.fill("#password", pw)
                page.click(new_selector)
                
                # Final check after recovery
                page.wait_for_url("**/inventory.html", timeout=5000)
                print("⚡ Recovery action performed successfully.")
            except Exception as retry_error:
                pytest.fail(f"Self-healing failed to apply the fix: {retry_error}")
        else:
            pytest.fail("AI was unable to provide a valid recovery locator.")
    
    # 5. FINAL ASSERTION
    assert "inventory.html" in page.url
    print("✅ Test Passed via Self-Healing!")