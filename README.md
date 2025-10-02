InnerVoice AI – Decision Clarity Through AI Debate

InnerVoice AI is an MVP that helps users overcome decision paralysis by simulating their internal reasoning process using role-based autonomous agents. Powered by CrewAI , it enables structured inner dialogue between four distinct agents:

Optimist – champions the upside and best-case outcomes

Pessimist – warns about risks and worst-case scenarios

Ethicist – considers values, ethics, and long-term integrity

Mediator – weighs all perspectives and provides a final, confident recommendation

This project is a Minimum Viable Product (MVP), built as part of the 48-Hour Build Challenge by Claude Builder Club @ UCSD.

✅ Multi-agent reasoning using CrewAI

✅ Real-time inner voice simulation

✅ Simple and clean Streamlit UI

✅ Fully configurable via YAML

✅ Secure API key management using .env

✅ Ready to deploy, customize, and scale

Installation

Clone the repo git clone https://github.com/SarathL754/48-Hour-Build-Challenge-Claude-Builder-Club-UCSD.git cd 48-Hour-Build-Challenge-Claude-Builder-Club-UCSD

Install dependencies

We recommend using uv or pip.

pip install -r requirements.txt

Add your .env file
Create a .env file in the project root:

touch .env

Paste your keys:

OPENAI_API_KEY=your-openai-api-key AGENTOPS_API_KEY=your-optional-agentops-api-key AGENTOPS_DISABLED=true # Recommended for local testing

✅ .env is excluded from version control via .gitignore.

Running the InnerVoice Crew (CLI or UI) Option 1: Streamlit Interface (Recommended) streamlit run src/innervoiceai/main.py

This launches a web UI where users can:

Input a decision they’re stuck on

Provide their values

See a complete debate and final recommendation

Option 2: Run from CLI crewai run

Make sure pyproject.toml is configured with:

[tool.crewai] entry_point = "src.innervoiceai.crew.Innervoiceai"

Configuration Agents

Defined in: src/innervoiceai/config/agents.yaml

Each agent has:

role: What they do

goal: Their purpose in the crew

backstory: Why they think the way they do

Tasks

Defined in: src/innervoiceai/config/tasks.yaml

Each task has:

description: What the agent must do

expected_output: What the agent must return

output_variable_name: Used to pass output to later tasks

📁 Project Structure innervoiceai/ ├── .env # ⚠️ Your secrets (ignored from git) ├── .gitignore ├── README.md # ✅ This file ├── requirements.txt # Project dependencies ├── pyproject.toml # For crewAI CLI └── src/ └── innervoiceai/ ├── config/ │ ├── agents.yaml │ └── tasks.yaml ├── crew.py ├── main.py # 💡 Streamlit interface └── tools/ # Optional: Custom tools for agents

Deployment Options

You can deploy this app to:

Streamlit Cloud (add API keys under "Secrets")

Hugging Face Spaces

Render

Vercel (via FastAPI wrapper)

Need help with deployment? Just ask!

📖 Learn More

🧠 CrewAI Docs

💬 CrewAI Discord

🔧 CrewAI GitHub

🤖 LangChain Tools

👩‍💻 Credits

Built by SarathL754 and contributors during the Claude Builder Club @ UCSD Hackathon.

Powered by:

CrewAI

OpenAI

Streamlit

📌 Disclaimer

This is an experimental MVP, not intended for real-world ethical or psychological advice. Use responsibly.
