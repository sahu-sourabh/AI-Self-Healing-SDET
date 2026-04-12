# AI-Self-Healing-SDET: Event-Driven QE Engine 🩺

An enterprise-grade proof-of-concept for **Autonomous Quality Engineering**. This framework integrates AI-driven self-healing logic into a containerized CI/CD pipeline, targeting the elimination of test flakiness in modern E2E suites.

## 🏗️ Architecture
* **Modular Core**: Separated logic (`app/`) and test suites (`tests/`) for high scalability.
* **AI Orchestrator**: Leverages **Llama 3.3 (via Groq)** to perform real-time root-cause analysis on UI/API failures.
* **CI/CD Integrated**: Automated validation via **GitHub Actions** on every push.
* **Containerized**: **Dockerized** environment to ensure execution parity across Dev, Staging, and Production.

## 🛠️ Tech Stack
* **Language**: Python 3.12
* **Testing**: Pytest, Pytest-Asyncio
* **AI Framework**: Pydantic-AI
* **Infrastructure**: Docker, GitHub Actions
* **LLM**: Groq (Llama 3-70B)

## 🚀 Getting Started
1. Clone the repo.
2. Add your `GROQ_API_KEY` to a `.env` file.
3. Install dependencies: `pip install -r requirements.txt`
4. Run locally: `pytest tests/test_unified_flow.py`
5. Deploy: Push to `main` to trigger the automated CI/CD pipeline.