import os
from dotenv import load_dotenv
from pydantic_ai import Agent

load_dotenv()

# We define the agent here, but we don't 'run' it in the global scope
test_doctor = Agent(
    'groq:llama-3.3-70b-versatile',
    system_prompt=(
        "You are a Senior SDET AI. You specialize in Playwright and API testing. "
        "Analyze the failure and return a concise fix in a code block."
    )
)

async def get_ai_fix(context_type, failing_item, html_or_schema):
    prompt = f"Type: {context_type}. Failed on: {failing_item}. Context: {html_or_schema}"
    result = await test_doctor.run(prompt)
    return result.output