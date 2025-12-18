# Neogentic-Agents
This is my Army of Agents

## Agents

### 1. Neo Agent v1 (Monolithic Agent)

    Agent Name = neo_agent_v1

**The Problem: The "Do-It-All" Agent**

Single agents can do a lot. But what happens when the task gets complex? A single "monolithic" agent that tries to do research, writing, editing, and fact-checking all at once becomes a problem. Its instruction prompt gets long and confusing. It's hard to debug (which part failed?), difficult to maintain, and often produces unreliable results.

**The Solution: A Team of Specialists**

Instead of one "do-it-all" agent, we can build a **multi-agent** system. This is a team of simple, specialized agents that collaborate, just like a real-world team. Each agent has one clear job (e.g., one agent only does research, another only writes). This makes them easier to build, easier to test, and much more powerful and reliable when working together.

To learn more, check out the documentation related to [LLM agents in ADK](https://google.github.io/adk-docs/agents/llm-agents/).

### Multi Agent Systems

### 2. Neo Agent v2 ( Research & Summarization System)

    Agent Name = neo_agent_v1

System with two specialized agents:

**Research Agent** - Searches for information using Google Search

**Summarizer Agent** - Creates concise summaries from research findings

A multi-agent system! You used a single **"coordinator"** agent to manage the workflow, which is a powerful and flexible pattern.

‼️ However, relying on an LLM's **instructions to control the order can sometimes be unpredictable.**

## Setup

### 1. Enviorment Variables
    1. create a .env file and paste the neccessary API keys in it
    2. for Gemini API Key put use variable : "GEMINI_API_KEY"
    3. for Weather API key use variable : OPEN_WEATHER_API_KEY for understanding and how it works refer to weather.py 

### 2. Virtual Enviorment
  A virtual environment is a tool used to isolate specific Python environments on a single machine, allowing you to work on multiple projects with different dependencies and packages without conflicts. This can be especially useful when working on projects that have conflicting package versions or packages that are not compatible with each other.

#### 1. Create a virtual environment
    
    python -m venv myenv

#### 2. Activate the virtual environment (Linux/macOS)
    
    source myenv/bin/activate

#### 3. Activate the virtual environment (Windows)

    myenv\Scripts\activate.bat

#### 4. Deactivate the virtual environment
    deactivate

### 3. Installation ("requirements.txt")
In addition to creating and activating a virtual environment, it can be useful to create a requirements.txt file that lists the packages and their versions that your project depends on. This file can be used to easily install all the required packages in a new environment.

To create a requirements.txt file, you can use the pip freeze command, which outputs a list of installed packages and their versions. For example:
    
#### Output the list of installed packages and their versions to a file
    pip freeze > requirements.txt

#### Install the packages listed in the requirements.txt file

    pip install -r requirements.txt


## Agent Model


🤔What is an AI Agent?
You've probably used an LLM like Gemini before, where you give it a prompt and it gives you a text response.

    Prompt -> LLM -> Text

An AI Agent takes this one step further. An agent can think, take actions, and observe the results of those actions to give you a better answer.

    Prompt -> Agent -> Thought -> Action -> Observation -> Final Answer

### Creating Agent
Run the adk create command to start a new agent project.
    
    adk create my_agent
or

    adk create sample-agent --model gemini-2.5-flash-lite --api_key $GOOGLE_API_KEY

    #### Agent created

The created agent project has the following structure, with the agent.py file containing the main control code for the agent.

    my_agent/

        agent.py      # main agent code
        .env          # API keys or project IDs
        __init__.py


### Configure

We'll configure an Agent by setting its key properties, which tell it what to do and how to operate.

To learn more, check out the documentation related to [agents in ADK](https://google.github.io/adk-docs/agents/).

These are the main properties we'll set:

**name and description:** A simple name and description to identify our agent.

**model:** The specific LLM that will power the agent's reasoning. We'll use "gemini-2.5-flash-lite".

**instruction:** The agent's guiding prompt. This tells the agent what its goal is and how to behave.

**tools:** A list of [tools](https://google.github.io/adk-docs/tools/) that the agent can use. To start, we'll give it the google_search tool, which lets it find up-to-date information online.


## Running Agent 

### 1. Run with command-line interface
Run your agent using the adk run command-line tool.

    adk run neo_agent_v1

### 2. Run with web interface
The ADK framework provides web interface you can use to test and interact with your agent. You can start the web interface using the following command:

    adk web --port 8000
