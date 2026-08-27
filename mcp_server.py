from fastmcp import FastMCP
import subprocess

mcp = FastMCP("Docker MCP Server") # instance

# Tool 1 : Show Running Containers 
@mcp.tool
def show_running_containers():
    result = subprocess.run(["docker", "ps"], capture_output=True, text=True)
    return result.stdout

# Tool 2 : Show Container Logs 
@mcp.tool
def show_containers_logs_by_name(container_name):
    result = subprocess(["docker", "logs", "--tail", "10",container_name], capture_output=True, text=True)
    return result.stdout

# Tool 3 : Show all Containers
@mcp.tool
def show_all_containers():
    result = subprocess.run(["docker", "ps", "-a"], capture_output=True, text=True)
    return result.stdout


if __name__ == "__main__":
    mcp.run()

