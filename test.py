from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
import pprint

# Create server parameters for stdio connection
server_params = StdioServerParameters(
    command="uv",
    args=["--directory",
          ".",
          "run",
          "json-error-demo"], 
)

async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            # Initialize the connection
            await session.initialize()

            # The example server only supports prompt primitives:
        
            # List available prompts
            tools = await session.list_tools()
            print(f"Tools: {pprint.pformat(tools.model_dump())}\n")

            # Call a tool
            print("Calling tool\n")
            result = await session.call_tool("search", {"query": "test"})
            print(f"Result: {result}")

if __name__ == "__main__":
    import asyncio
    asyncio.run(run())