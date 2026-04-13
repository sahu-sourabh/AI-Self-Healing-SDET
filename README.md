# AI-Self-Healing-SDET: Event-Driven QE Engine 🩺

![Build Status](https://github.com/sahu-sourabh/AI-Self-Healing-SDET/actions/workflows/main.yml/badge.gif) 

An enterprise-grade proof-of-concept for **Autonomous Quality Engineering**. This framework integrates AI-driven self-healing logic into a containerized CI/CD pipeline, targeting the elimination of test flakiness.

## 🏗️ Project Status: Active Development (Foundation Phase)
I am currently transitioning the framework's core to **Playwright + Python 3.12** to leverage superior async performance and modern web standards.

### 🏗️ Architecture & Roadmap
- [x] **CI/CD Integrated:** Automated validation via GitHub Actions is LIVE.
- [x] **Modular Core:** Logic (app/) and test suites (tests/) are separated for scalability.
- [/] **Core Foundation (Current Sprint):** Implementing robust Playwright Page Objects.
- [ ] **AI Orchestrator:** Integrating **Pydantic-AI** and **Llama 3.3** for real-time root-cause analysis and DOM healing.

## 🛠️ Tech Stack
- **Language:** Python 3.12
- **Testing:** Pytest, Playwright
- **AI Framework:** Pydantic-AI
- **LLM:** Llama 3.3 (via Groq)
- **Infrastructure:** Docker, GitHub Actions

## 🚀 Getting Started (Experimental)
1. **Clone the repo:** `git clone ...`
2. **Install dependencies:** `pip install -r requirements.txt`
3. **Playwright Setup:** `playwright install`
4. **Run Sample:** `pytest tests/test_foundation.py`

---
*Serving Notice Period | Last Working Day: June 2nd, 2026*