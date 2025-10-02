# 🧠 InnerVoice AI – Decision Clarity Through AI Debate

InnerVoice AI is a **Minimal Viable Product (MVP)** that helps users overcome decision paralysis by simulating structured internal debates between role-based autonomous agents.

This project was built for the **48-Hour Build Challenge** by Claude Builder Club @ UCSD.

---

## 🧩 Overview

InnerVoice AI allows users to input a difficult decision and receive reasoned responses from four simulated inner voices:

- 🟢 **Optimist** – champions the upside and best-case outcomes  
- 🔴 **Pessimist** – warns about risks and worst-case scenarios  
- ⚖️ **Ethicist** – considers personal values and moral impact  
- 🧘 **Mediator** – synthesizes all perspectives into a confident final recommendation  

The system uses [CrewAI](https://github.com/joaomdmoura/crewai) to coordinate reasoning across multiple agents and return a unified response, accessible via a clean Streamlit UI.

---

## 🚀 Features

- ✅ Multi-agent inner voice simulation using CrewAI  
- ✅ Real-time response with LLMs (OpenAI, Anthropic, etc.)  
- ✅ Fully customizable agent roles via YAML  
- ✅ Clean and interactive Streamlit interface  
- ✅ Secure API key management via `.env`  
- ✅ Ready for deployment (Streamlit Cloud, HuggingFace Spaces)

---

## 🛠️ Tech Stack

| Tool        | Purpose                                |
|-------------|----------------------------------------|
| 🧠 CrewAI    | Multi-agent orchestration              |
| 💬 Claude    | Language model API (for reasoning)     |
| 🎛️ Streamlit | Interactive UI                         |
| 📝 YAML      | Configuration of agents and tasks      |
| 🔐 Python-dotenv | Secure local environment variables |

---

## 🧪 Example Use Case

> _“Should I buy a car or a bike while staying environmentally responsible?”_

👂 You'll hear from:
- The **Optimist** – “Cars are great for family and adventure!”
- The **Pessimist** – “Cars can be costly and polluting.”
- The **Ethicist** – “Balance sustainability with long-term needs.”
- The **Mediator** – “A hybrid solution might work best...”

---

## 📥 Installation

```bash
# Clone the repo
git clone https://github.com/SarathL754/48-Hour-Build-Challenge-Claude-Builder-Club-UCSD.git
cd 48-Hour-Build-Challenge-Claude-Builder-Club-UCSD

# Install dependencies
pip install -r requirements.txt
