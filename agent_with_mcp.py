from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain.agents import create_agent
from langchain_ollama import ChatOllama
import asyncio

async def main():
    # this brings all the tools from mcp server
    client = MultiServerMCPClient(
        {
            "docker-mcp" : {
                "transport": "stdio",
                "command": "python",
                "args": ["mcp_server.py"]
            }
        }
    )
    tools = await client.get_tools() # ye local tools nhi h, ye mcp tools hai jo "docker-mcp" me rkhe hue hai.
    llm = ChatOllama(
        model="gemma4",
        temperature="0.8", 
    )

    # agent with MCP tools
    agent = create_agent(
        llm,
        tools
    )
    while True:
        user_input = input("Enter your message :\n")
        if user_input == "exit":
            break
        response = agent.ainvoke(
            {"messages": [{"role": "user", "content": "how many containers are running"}]}
        )
        print(response['message'][-1].content)

if __name__ == "__main__":
    asyncio.run(main())


