import os
import logging
from dotenv import load_dotenv
from pydantic_ai import Agent

# 1. Setup Professional Logging
# This ensures that both local and CI/CD logs are readable and timestamped
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

load_dotenv()

# 2. Define the Senior SDET AI Agent
test_doctor = Agent(
    'groq:llama-3.3-70b-versatile',
    system_prompt=(
        "You are a Senior SDET AI. Analyze the provided HTML and the failing locator. "
        "Find the real element in the HTML that matches the user's intent. "
        "STRICT RULES: "
        "1. Do NOT provide examples. "
        "2. Do NOT provide multiple options. "
        "3. Your response must ONLY contain the correct CSS selector inside double brackets, "
        "e.g., [[#login-button]]. "
        "4. If you cannot find a fix, return [[NONE]]."
    )
)

async def get_ai_fix(context_type, failing_item, html_or_schema):
    """
    Orchestrates the AI call to recover from a test failure.
    """
    logger.info(f"🚀 Initializing Self-Healing for {context_type}")
    logger.info(f"❌ Failed Item: {failing_item}")
    
    prompt = (
        f"Context: {context_type}. "
        f"Failed Element: {failing_item}. "
        f"Available DOM/Schema: {html_or_schema}"
    )

    try:
        logger.info("🤖 Requesting diagnostic fix from Llama 3.3...")
        result = await test_doctor.run(prompt)
        
        logger.info("✅ AI Recovery Suggestion generated successfully.")
        return result.output

    except Exception as e:
        logger.error(f"⚠️ AI Agent failed to provide a fix: {str(e)}")
        return "Manual intervention required: AI Diagnostic failed."