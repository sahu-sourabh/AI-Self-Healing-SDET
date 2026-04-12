# AI-Driven Self-Healing Test Agent 🩺

A proof-of-concept AI agent built to eliminate test flakiness in E2E pipelines. This tool uses **Llama 3.3 (via Groq)** and **Pydantic-AI** to analyze failing Playwright/Cypress selectors and suggest robust alternatives in real-time.

### 🚀 Key Features:
- **Contextual Awareness**: Analyzes HTML snippets to understand DOM changes.
- **Selector Optimization**: Prioritizes `data-testid` and ARIA roles over brittle CSS paths.
- **LLM Integration**: Leverages high-speed inference for near-instant test recovery suggestions.

### 🛠️ Tech Stack:
- **Language**: Python 3.12
- **Framework**: Pydantic-AI
- **LLM**: Groq (Llama 3.3-70B)
- **Testing Context**: Playwright / Cypress