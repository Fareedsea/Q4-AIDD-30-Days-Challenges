import chainlit as cl
from agents import Runner
from agent import create_agent

@cl.on_chat_start
async def on_chat_start():
    agent = create_agent()
    cl.user_session.set("agent", agent)
    await cl.Message(content="Hello, how can I assist you today?").send()

@cl.on_message
async def on_message(message: cl.Message):
    agent = cl.user_session.get("agent")
    runner = Runner(agent=agent)
    result = await runner.run(message.content)

    if result.tool_calls:
        for tool_call in result.tool_calls:
            await cl.Message(content=f"Tool call: {tool_call.tool_name} with args {tool_call.tool_args}").send()

    if result.final_output:
        await cl.Message(content=result.final_output).send()
