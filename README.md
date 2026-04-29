# 📧 Multi-Agent Sales Email Generator

Generate high-quality cold emails using multiple AI agents with different writing styles — in parallel.

---

## 🚀 Overview

This project uses **multiple LLM agents** to generate cold sales emails for the same use case, each with a distinct tone:

- Professional
- Humorous & engaging
- Concise & direct

All agents run **concurrently using asyncio**, allowing you to compare outputs instantly.

---

## ⚙️ How It Works

- Three agents are defined with different instructions
- Each agent receives the **same input prompt**
- `asyncio.gather()` runs them in parallel
- Outputs are printed together for easy comparison

---

## 🧠 Agents

### 1. Professional Sales Agent

- Tone: Formal, serious
- Focus: Clarity and credibility

### 2. Engaging Sales Agent

- Tone: Witty, conversational
- Focus: Attention & response rate

### 3. Busy Sales Agent

- Tone: Short, direct
- Focus: Efficiency

---

## 🔁 Execution Flow

```python
asyncio.gather(
  Runner.run(agent1, input=...),
  Runner.run(agent2, input=...),
  Runner.run(agent3, input=...)
)
```

Each agent runs independently and returns:

```python
res.final_output
```

---

## 📦 Installation

```bash
git clone https://github.com/your-username/multi-agent-email-generator.git
cd multi-agent-email-generator
pip install -r requirements.txt
```

---

## 🔑 Setup

Create a `.env` file:

```
OPENAI_API_KEY=your_api_key_here
SENDGRID_API_KEY=your_sendgrid_key_here
```

---

## ▶️ Run

```bash
python app.py
```

---

## 💡 Example Use Case

Input:

> Generate a cold email to a CTO about SOC2 compliance

Output:

- Email 1 → Professional version
- Email 2 → Engaging version
- Email 3 → Concise version

---

---

## 🛠️ Tech Stack

- Python
- OpenAI Agents SDK (`Agent`, `Runner`)
- Asyncio (parallel execution)
- SendGrid (optional email sending)

---

---

## 📄 License

MIT License
