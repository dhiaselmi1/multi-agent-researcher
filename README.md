# 🤖 Multi-Agent Researcher

A modular, AI-driven research pipeline that uses multiple agents and a local LLM (LLaMA2 via Ollama) to simulate in-depth research. Each agent has a specialized task—searching, summarizing, checking for hallucinations, and reporting—collaborating like a real research team.

---

## 🚀 Features

- 🔍 Simulated or real API-based topic search
- 🧠 Summary generation using LLaMA2 (via local API)
- 🧐 Fact-checking for bias and hallucination
- 📄 Final report generation
- 🧩 Modular multi-agent design, easy to extend or customize

---

---

## 🧪 How It Works

The `orchestrator.py` ties together four agents:

1. **Search Agent** (`search_agent.py`): Simulates search results (you can plug in a real API like Serper or Brave Search).
2. **Summarizer Agent**: Converts findings into concise bullet points.
3. **Checker Agent**: Analyzes for hallucinations or bias.
4. **Report Agent**: Combines it all into a professional report.

> ✏️ **Want real search results?**
> Replace the dummy `run_search()` function in `search_agent.py` with an actual API call like Serper.dev, Brave Search, or Bing Web API.

---

## 💼 Real-World Use Case

**Horizon Insights**, a competitive intelligence firm, often needs rapid, reliable research on companies, markets, and emerging technologies. Instead of relying on a single AI model for everything, they use this *multi-agent system* to break down tasks:

- One agent gathers the facts.
- Another condenses the findings.
- A third validates the content.
- A final agent writes the report.

This mirrors how actual analysts work—resulting in faster, more trustworthy intelligence.

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/multi-agent-researcher.git
cd multi-agent-researcher
```
2.  **Install Python Dependencies:**
    It's recommended to create a virtual environment first:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: `venv\Scripts\activate`
    ```
    Then, install the required libraries:
    ```bash
    pip install streamlit    requests
    ```
    *(For a production setup, you might want to create separate `requirements.txt` files for `backend` and `frontend`.)*

 ## ▶️ Running the Application

1.  **Start the Frontend Application:**
    Open a *new* terminal, navigate to the `frontend` directory:
    ```bash
    streamlit run app.py
    ```
    This will open the Streamlit application in your web browser (typically at `http://localhost:8501`).


