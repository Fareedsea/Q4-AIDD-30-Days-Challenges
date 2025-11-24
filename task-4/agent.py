import os
from agents import Agent, OpenAIChatCompletionsModel
from openai import AsyncOpenAI
from tools import read_user_profile, update_user_profile

def create_agent():
    """Creates and configures the agent."""
    client = AsyncOpenAI(
        base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
        api_key=os.environ["GEMINI_API_KEY"],
    )

    model = OpenAIChatCompletionsModel(
        model="gemini-2.0-flash",
        openai_client=client,
    )

    agent = Agent(
        name="Personal Assistant",
        instructions="Greet users by name if known. Detect when users share personal info and save it using tools.",
        tools=[read_user_profile, update_user_profile],
        model=model,
    )
    return agent
