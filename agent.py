# Langchain
from langchain_ollama import ChatOllama
from langchain_core.tools import tool
from langchain.agents import create_agent

#System Package
import subprocess # package that can run your commands on your terminal

# model = ChatOllama(
#     model="gemma4",
#     temperature="0.8", # controls randomness,jitna temperature high hoga utna edher udher chize nhi krega.

# )

SYSTEM_PROMPT = """
You are a docker expert. You can explain things in 1-2 line max.
You don't overthink, hallucinate or keep reasoning in a loop.
You Reason and Act according to user prompt.

these are the thnings you do:
1/ You tell errors (What went wrong, etc)
2/ You tell about the root cause (What was the cause likely)
3/ You tell about fix or solution in short
"""

# Tool 1 : Show Running Containers 
# And this tool is running on local so it is not MCP Server
@tool
def show_running_containers():
    result = subprocess.run(["docker", "ps"], capture_output=True, text=True)
    return result.stdout

# Tool 2 : Show Container Logs 
@tool
def show_containers_logs_by_name(container_name):
    result = subprocess(["docker", "logs", "--tail", "10",container_name], capture_output=True, text=True)
    return result.stdout

# Tool 3 : Show all Containers
@tool
def show_all_containers():
    result = subprocess.run(["docker", "ps", "-a"], capture_output=True, text=True)
    return result.stdout

llm = ChatOllama(
    model="gemma4",
    temperature="0.8", # controls randomness,jitna temperature high hoga utna edher udher chize nhi krega.
    system = SYSTEM_PROMPT,
) # LLM

tools = [show_running_containers, show_containers_logs_by_name, show_all_containers] # Tools

agent = create_agent(llm, tools)

while True:
    user_input = input("Enter your message :\n")
    if user_input == "exit":
        break
    response = agent.invoke({"messages":[{
        "role":"user", 
        "content":user_input
    }]})

    print(response['messages'][-1].content) 


