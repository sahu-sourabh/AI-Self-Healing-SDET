import os
import asyncio
from dotenv import load_dotenv
from pydantic_ai import Agent

# 1. Load your Groq Key from the .env in THIS folder
load_dotenv()

# 2. Define the Agent's "Job Description"
# This system prompt is your "SDET Architect" persona
test_doctor = Agent(
    'groq:llama-3.3-70b-versatile',
    system_prompt=(
        "You are a Senior SDET AI Agent. Your expertise is fixing brittle test selectors. "
        "Analyze the provided failing selector and HTML context to suggest a robust, "
        "maintainable Playwright selector. Prioritize data-testid and accessible roles."
    )
)

async def main():
    print("--- 🩺 AI-Self-Healing-SDET: Diagnosing... ---")
    
    # Example scenario for your portfolio
    failing_selector = "button#login-01"
    html_context = """
    <div class="auth-form">
        <button data-testid="login-submit" class="btn-primary-new" aria-label="Submit Login">
            Enter Dashboard
        </button>
    </div>
    """
    
    prompt = f"""
    The test failed on: '{failing_selector}'.
    Current HTML: {html_context}
    
    Provide the best Playwright selector and a brief 'Senior Engineer' explanation.
    """

    try:
        # result.output is the standard text attribute for 2026
        result = await test_doctor.run(prompt)
        print(f"\n✅ AI PROPOSAL:\n{result.output}")
    except Exception as e:
        print(f"Connection Error: {e}")

if __name__ == '__main__':
    asyncio.run(main())