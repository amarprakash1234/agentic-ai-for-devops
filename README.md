# Agentic AI for DevOps

An **Agentic AI for DevOps** project that combines **LLMs, LangChain, Ollama, Docker, and Model Context Protocol (MCP)** to create an AI-powered DevOps assistant.

The agent can interact with Docker through custom tools and help inspect running containers, list all containers, and retrieve container logs.

## 🚀 Features

* 🤖 AI-powered DevOps assistant
* 🐳 Docker container monitoring
* 📦 View currently running containers
* 📋 View all Docker containers
* 📜 Retrieve container logs
* 🔧 Custom tools using LangChain
* 🧠 Local LLM integration using Ollama
* 🔌 MCP server implementation using FastMCP
* 🌐 MCP client integration with LangChain
* 💻 Interactive command-line interface

## 🏗️ Project Structure

```text
agentic-ai-for-devops/
│
├── agent.py
├── agent_with_mcp.py
├── mcp_server.py
├── my_first_generative_ai.py
├── requirements.txt
└── .gitignore
```

## 📄 Project Components

### 1. `agent.py`

This file contains the main AI-powered Docker assistant.

The agent uses:

* `ChatOllama` for connecting with a local LLM
* LangChain tools
* LangChain agent framework
* Python `subprocess` module to execute Docker commands

The agent provides the following Docker tools:

#### Show Running Containers

```bash
docker ps
```

#### Show All Containers

```bash
docker ps -a
```

#### Show Container Logs

The agent can retrieve recent logs from a specific Docker container.

Example:

```text
Show me the logs of my-nginx-container
```

---

### 2. `mcp_server.py`

This file creates a **Docker MCP Server** using FastMCP.

The Docker operations are exposed as MCP tools:

* `show_running_containers`
* `show_containers_logs_by_name`
* `show_all_containers`

This allows external AI agents to discover and use Docker-related tools through the **Model Context Protocol**.

---

### 3. `agent_with_mcp.py`

This file demonstrates how an AI agent can connect to the Docker MCP server.

The project uses:

```text
MultiServerMCPClient
```

to connect with the MCP server through the `stdio` transport.

The available MCP tools are then provided to the LangChain agent.

---

## 🛠️ Tech Stack

| Technology                   | Purpose                                  |
| ---------------------------- | ---------------------------------------- |
| Python                       | Core programming language                |
| LangChain                    | AI agent and tool integration            |
| Ollama                       | Running local LLMs                       |
| LangGraph                    | Agent workflow infrastructure            |
| Docker                       | Container management                     |
| FastMCP                      | Creating MCP servers                     |
| Model Context Protocol (MCP) | Connecting AI agents with external tools |

## ⚙️ Prerequisites

Before running this project, make sure you have the following installed:

* Python 3.10+
* Docker
* Ollama
* A supported Ollama model

You can verify Docker installation with:

```bash
docker --version
```

Check whether Docker is running:

```bash
docker ps
```

You should also have Ollama installed and running locally.

## 📦 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/amarprakash1234/agentic-ai-for-devops.git
```

### 2. Move Into the Project Directory

```bash
cd agentic-ai-for-devops
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

Activate it.

#### macOS/Linux

```bash
source venv/bin/activate
```

#### Windows

```bash
venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

The project dependencies include:

```text
langchain-ollama
langchain-core
langchain
ollama
langgraph
fastmcp
langchain-mcp-adapters
```

## 🧠 Configure the Ollama Model

The current project configuration uses:

```python
model="gemma4"
```

Make sure the configured model is available in your local Ollama installation.

If you want to use another model, update the model name inside:

```text
agent.py
agent_with_mcp.py
```

## ▶️ Running the Local Docker Agent

Run:

```bash
python agent.py
```

You will see:

```text
Enter your message:
```

You can then ask questions related to Docker.

Example:

```text
How many containers are running?
```

```text
Show all my Docker containers
```

```text
Show logs for nginx-container
```

To exit:

```text
exit
```

## 🔌 Running the MCP-Based Agent

The MCP server is started automatically by the MCP client configuration using the following command:

```python
"command": "python",
"args": ["mcp_server.py"]
```

Run the MCP-based agent with:

```bash
python agent_with_mcp.py
```

The flow is:

```text
User
  │
  ▼
AI Agent
  │
  ▼
LangChain
  │
  ▼
MCP Client
  │
  ▼
Docker MCP Server
  │
  ▼
Docker Commands
```

## 🐳 Available Docker Tools

### `show_running_containers`

Displays all currently running Docker containers.

Equivalent Docker command:

```bash
docker ps
```

### `show_all_containers`

Displays all Docker containers, including stopped containers.

Equivalent Docker command:

```bash
docker ps -a
```

### `show_containers_logs_by_name`

Retrieves recent logs for a specific container.

Equivalent command:

```bash
docker logs --tail 10 <container_name>
```

## 🧩 How It Works

The project demonstrates two approaches for building an AI-powered DevOps agent.

### Approach 1: Local LangChain Tools

```text
User
   ↓
LangChain Agent
   ↓
Custom Python Tools
   ↓
subprocess
   ↓
Docker CLI
```

In this approach, the Docker tools are directly defined inside the Python application.

### Approach 2: MCP-Based Tools

```text
User
   ↓
LangChain Agent
   ↓
MCP Client
   ↓
FastMCP Server
   ↓
Docker Tools
   ↓
Docker CLI
```

This approach separates the tools from the AI agent using the Model Context Protocol.

## 🎯 Learning Objectives

This project is useful for understanding:

* How AI agents use tools
* Building custom tools with LangChain
* Connecting local LLMs using Ollama
* Executing system commands with Python
* Building an MCP server
* Connecting an MCP client to an AI agent
* Using AI for DevOps automation
* Creating Docker-aware AI assistants

## 👨‍💻 Author

**Amar Prakash**

GitHub: [amarprakash1234](https://github.com/amarprakash1234?utm_source=chatgpt.com)


