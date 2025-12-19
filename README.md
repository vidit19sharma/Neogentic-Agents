# 🧠 Neogentic-Agents  
## *An Army of Intelligent AI Agents 🤖⚔️*

**Neogentic-Agents** is a collection of **AI agent systems** built using **Google Agent Development Kit (ADK)**.  
The project explores multiple **agent architecture patterns**, evolving from a **monolithic agent** to **advanced multi-agent systems** with coordination and parallelism.

---

## 📚 Table of Contents
- [Overview]
- [Table of Contents]
- [Agent Catalog]
- [Tech Stack]
- [Setup]
- [AI Model Agent]
- [Running the Agents]
- [Project Structure]
- [Future Improvements]
- [Contributions]
- [Contact]


---

## 📦 Agent Catalog

| S.No | **Agent ID** | **Agent Name** | **Description** |
|----|------------|--------------|----------------|
| 1 | `neo_agent_v1` | Monolithic Agent | Simple agent with Google Search access |
| 2 | `neo_agent_v2` | Research & Summarization System | Two specialized agents coordinated by AI |
| 3 | `neo_agent_v3` | Blog Post Creation Agent | Sequential multi-agent content pipeline |
| 4 | `neo_agent_v4` | Multi Research Team | Parallel research across Tech, Health & Finance |

---

## 📌 Agents Summary

## 🟢 1. Neo Agent v1 — **Monolithic Agent**
- **Agent Name:** `neo_agent_v1`

### ❌ Problem: The “Do-It-All” Agent
- Research, writing, editing, fact-checking in one agent  
- Long prompts, hard debugging, poor maintainability

### ✅ Solution: Multi-Agent Design
- Specialized agents with single responsibility  
- Easier debugging, scalability, and reliability

📘 [LLM Agents in ADK](https://google.github.io/adk-docs/agents/llm-agents/)

---

## 🟡 2. Neo Agent v2 — **Research & Summarization System**
- **Agent Name:** `neo_agent_v2`

### 🧩 System Architecture
- **Research Agent** – Google Search  
- **Summarizer Agent** – Condensed insights  
- **Coordinator Agent** – Workflow control

⚠️ LLM-based ordering can be unpredictable

---

## 🔵 3. Neo Agent v3 — **Blog Post Creation Agent**
- **Agent Name:** `neo_agent_v3`

### ✍️ Workflow
- **Outline Agent**
- **Writer Agent**
- **Editor Agent**

---

## 🔴 4. Neo Agent v4 — **Multi Research Team**
- **Agent Name:** `neo_agent_v4`

### 🔬 Agents
- Tech Researcher  
- Health Researcher  
- Finance Researcher  
- Aggregator Agent

---

## 🧰 Tech Stack
- Python
- Google Agent Development Kit (ADK)
- Gemini LLMs
- Google Search Tool
- OpenWeather API


## ⚙️ Setup & Configuration

### 🔐 Environment Variables
    1. create a .env file and paste the neccessary API keys in it
    2. for Gemini API Key put use variable : "GEMINI_API_KEY"
    3. for Weather API key use variable : OPEN_WEATHER_API_KEY for understanding and how it works refer to weather.py

### 🐍 Virtual Environment
A virtual environment is a tool used to isolate specific Python environments on a single machine, allowing you to work on multiple projects with different dependencies and packages without conflicts. This can be especially useful when working on projects that have conflicting package versions or packages that are not compatible with each other.

#### 1. Create a virtual environment
    
    python -m venv myenv

#### 2. Activate the virtual environment (Linux/macOS)
    
    source myenv/bin/activate

#### 3. Activate the virtual environment (Windows)

    myenv\Scripts\activate.bat

#### 4. Deactivate the virtual environment
    deactivate

### 📦 Dependencies ("requirements.txt")
In addition to creating and activating a virtual environment, it can be useful to create a requirements.txt file that lists the packages and their versions that your project depends on. This file can be used to easily install all the required packages in a new environment.

To create a requirements.txt file, you can use the pip freeze command, which outputs a list of installed packages and their versions. For example:
    
#### Output the list of installed packages and their versions to a file
    pip freeze > requirements.txt

#### Install the packages listed in the requirements.txt file

    pip install -r requirements.txt

---

## 🧠 AI Agent Model

### 🤔 What is an AI Agent?
You've probably used an LLM like Gemini before, where you give it a prompt and it gives you a text response.

    Prompt -> LLM -> Text

An AI Agent takes this one step further. An agent can think, take actions, and observe the results of those actions to give you a better answer.

    Prompt -> Agent -> Thought -> Action -> Observation -> Final Answer



### 🛠️ Creating an Agent

Run the adk create command to start a new agent project.
    
    adk create my_agent
or

    adk create sample-agent --model gemini-2.5-flash-lite --api_key $GOOGLE_API_KEY
---

### 📁 Agent Structure
The created agent project has the following structure, with the agent.py file containing the main control code for the agent.

```
my_agent/
├── agent.py            # main agent code
├── .env                # API keys or project IDs
└── __init__.py
```
---
### ⚙ Configure 

We'll configure an Agent by setting its key properties, which tell it what to do and how to operate.

To learn more, check out the documentation related to [agents in ADK](https://google.github.io/adk-docs/agents/).

These are the main properties we'll set:

**name and description:** A simple name and description to identify our agent.

**model:** The specific LLM that will power the agent's reasoning. We'll use "gemini-2.5-flash-lite".

**instruction:** The agent's guiding prompt. This tells the agent what its goal is and how to behave.

**tools:** A list of [tools](https://google.github.io/adk-docs/tools/) that the agent can use. To start, we'll give it the google_search tool, which lets it find up-to-date information online.

---

## ▶️ Running the Agents
### 1. Run with command-line interface
Run your agent using the adk run command-line tool.

    adk run neo_agent_v1

### 2. Run with web interface
The ADK framework provides web interface you can use to test and interact with your agent. You can start the web interface using the following command:

    adk web --port 8000

---

## 📂 Project Structure

```
Neogentic-Agents/
├── .gitignore
├── README.md
├── weather.py
├── neo_agent_v1/        # Version 1 – Simple Monolithic Agent
│   ├── <files for v1 agent>
│   └── …
├── neo_agent_v2/        # Version 2 – Research & Summarization System
│   ├── <files for v2 agents & coordinator>
│   └── …
├── neo_agent_v3/        # Version 3 – Blog Post Creation Multi-Agent
│   ├── <files for v3 agents>
│   └── …
└── neo_agent_v4/        # Version 4 – Multi Research Team Agents
    ├── <files for v4 agents>
    └── …
```
---

## 🔮 Future Improvements
- Agent memory and persistence
- Retry & failure handling
- Tool result validation
- Cost optimization strategies

---
## 🤝 Contributing

Pull requests are welcome. Please open an issue before major changes.

---

## 📬 Author
Vidit Sharma  
GitHub: [@vidit19sharma](https://github.com/vidit19sharma)

