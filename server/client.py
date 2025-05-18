import asyncio
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from mcp_use import MCPAgent, MCPClient

async def run_memory_chat():
    """Run a memory chat with the weather MCP server"""
    load_dotenv()
    os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
    
    # Config file path - change this to your config file
    config_file = "server/weather.json"
    
    print("--- Initializing MCP Client ---")
    
    # Create MCP client and agent with memory enabled
    mcp_client = MCPClient.from_config_file(config_file)
    llm = ChatGroq(model="qwen-qwq-32b")
    
    # create agent with memory_enabled = True
    agent = MCPAgent(
        llm=llm, 
        client=mcp_client, 
        max_steps=15,
        memory_enabled=True)
    
    print("\n===== Interactive MCP Chat =====")
    print("Type 'exit' or 'quit' to end the conversation")
    print("Type 'clear' to clear conversation history")
    print("==================================\n")
    
    try:
        # Main Chat loop 
        while True:
            user_input = input("\nYou: ")
            if user_input.lower() in ["exit", "quit"]:
                print("\n===== Conversation Ended =====")
                print("Thank you for using the MCP Chat!")
                print("==================================\n")
                break
            elif user_input.lower() == "clear":
                agent.clear_conversation_history()
                print("\nConversation history cleared.")
                continue
            
            # Get response from agent
            print("\nAssistant: ", end="", flush=True)
            
            try:
                # Get response from agent
                response = await agent.run(user_input)
                print(f"\nMCP Agent: {response}")
            except Exception as e:
                print(f"Error: {e}")
    finally:
        print("\n===== Conversation Ended =====")
        print("Thank you for using the MCP Chat!")
        print("==================================\n")
        if mcp_client and mcp_client.sessions:
            await mcp_client.close_all_sessions()
        
if __name__ == "__main__":
    asyncio.run(run_memory_chat())