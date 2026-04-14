# AI-Self-Healing-SDET: Event-Driven QE Engine 🩺

[![AI-QE-Pipeline](https://github.com/sahu-sourabh/AI-Self-Healing-SDET/actions/workflows/main.yml/badge.svg)](https://github.com/sahu-sourabh/AI-Self-Healing-SDET/actions/workflows/main.yml) 

An enterprise-grade proof-of-concept for **Autonomous Quality Engineering**. This framework integrates AI-driven self-healing logic into a stable CI/CD pipeline, effectively eliminating flakiness caused by shifting DOM elements.

## 🏗️ Project Status: MVP Reached 🚀
The framework has successfully demonstrated **Autonomous Recovery** by detecting failing locators and using LLM diagnostics to heal tests in real-time.

### 🏗️ Architecture & Roadmap
- [x] **CI/CD Integrated:** Automated validation via GitHub Actions is LIVE.
- [x] **Threaded Bridge:** Implemented a sync-async bridge for 100% stability on Windows and Linux runners.
- [x] **AI Orchestrator:** Integrated **Pydantic-AI** and **Llama 3.3** for DOM analysis and "Brackets Protocol" healing.
- [x] **Secure Secrets:** Environment-agnostic configuration using `.env` and GitHub Secrets.
- [ ] **Smart Filtering (Next):** Implementing DOM Minification to optimize token usage and latency.

## 🛠️ Tech Stack
- **Language:** Python 3.12
- **Testing:** Pytest, Playwright (Sync API)
- **AI Framework:** Pydantic-AI
- **LLM:** Llama 3.3-70b (via Groq API)
- **Infrastructure:** GitHub Actions

## 🚀 Getting Started
1. **Clone the repo:** `git clone ...`
2. **Setup Secrets:** Create a `.env` file with `GROQ_API_KEY`, `SAUCE_USERNAME`, and `SAUCE_PASSWORD`.
3. **Install dependencies:** `pip install -r requirements.txt`
4. **Playwright Setup:** `playwright install`
5. **Run Self-Healing Test:** `pytest tests/test_ai_playwright.py --headed -s`

---
*Serving Notice Period | Last Working Day: June 2nd, 2026*