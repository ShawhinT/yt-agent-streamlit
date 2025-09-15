from agents import Agent, function_tool, Runner
from openai.types.responses import ResponseTextDeltaEvent
from dotenv import load_dotenv
import asyncio
import os
from functions import fetch_video_transcript, fetch_intstructions

# try to import OPENAI_API_KEY from .env file, if not found, take user input
if not os.getenv("OPENAI_API_KEY"):
    OPENAI_API_KEY = input("Enter your OpenAI API key: ")
    with open(".env", "w") as f:
        f.write(f"OPENAI_API_KEY={OPENAI_API_KEY}")
else:
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# load system instructions
with open("prompts/system_instructions.md", "r") as f:
    system_instructions = f.read()
    
# create agent
agent = Agent(
    name="YouTube Agent",
    model="gpt-5",
    system_instructions=system_instructions,
    tools=[fetch_video_transcript, fetch_intstructions],
)

async def main():
    pass

if __name__ == "__main__":
    asyncio.run(main())
