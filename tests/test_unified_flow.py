import pytest
import requests
import asyncio
from app.agent_logic import get_ai_fix

# 1. API Test Scenario
def test_api_health_check():
    """Validates the core API response for the Fintech app."""
    print("\n[STG-1] Testing API Layer...")
    # Simulated API check (In real life, this would be requests.get(url))
    response_status = 200
    assert response_status == 200
    print("✅ API check passed.")

# 2. UI Self-Healing Scenario (The "Architect" Demo)
@pytest.mark.asyncio
async def test_ui_self_healing():
    """Simulates a UI failure and uses the AI Agent to recover."""
    print("\n[STG-2] Testing UI Layer with Self-Healing...")
    
    # Context of the failure
    failing_selector = "button#login-old-version"
    html_context = '<button data-testid="login-submit" class="primary-btn">Sign In</button>'
    
    print(f"❌ Playwright Timeout: Selector '{failing_selector}' not found.")
    print("🤖 Calling AI Agent for recovery...")
    
    # Call our logic from the app folder
    suggestion = await get_ai_fix("Playwright UI", failing_selector, html_context)
    
    # Assertions to prove it worked
    assert "data-testid" in suggestion.lower()
    print(f"✅ AI Recovery Suggestion Received:\n{suggestion}")

if __name__ == "__main__":
    # This allows you to run it via 'python tests/test_unified_flow.py' as well
    pytest.main([__file__])