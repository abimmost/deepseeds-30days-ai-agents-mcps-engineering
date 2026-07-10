# CUSTOMER AGENT BOT

from config import openai_key, openai_url

from openai import AsyncOpenAI
from agents import Agent, Runner, function_tool, set_tracing_disabled
from agents.models.openai_chatcompletions import OpenAIChatCompletionsModel

set_tracing_disabled(True)

state = {
    "active_agent": None
}

gemini_client = AsyncOpenAI(
    api_key=openai_key,
    base_url=openai_url
)

gemini_model = OpenAIChatCompletionsModel(
    model="gemini-2.5-flash",
    openai_client=gemini_client
)

# Define handoff tools/functions

@function_tool
def transfer_to_triage():
    """Call this when the user needs general help or you want to know some general info"""
    print("\n[System] Handoff: Transferring to Triage Agent...")
    state["active_agent"]=triage_agent
    return triage_agent

@function_tool
def transfer_to_txsupport():
    """Call this tool when the user needs technical support"""
    print("\n[System] Handoff: Transferring you to Technical Support agent...")
    state["active_agent"]=txsupport_agent
    return txsupport_agent

@function_tool
def transfer_to_billing():
    """Call this tool when you want to handle billing operations for the user"""
    print("\n[System] Handoff: Transferring to Billing agent...")
    state["active_agent"]=billing_agent
    return billing_agent

triage_agent = Agent(
    name="Triage Agent",
    instructions="You are the gatekeeper for customer support. Listen to the user's issues and determine the kind of help they need, then switch to the technical or billing assistants where needed. Don't try to solve technical issues yourself.",
    model=gemini_model,
    tools=[transfer_to_billing, transfer_to_txsupport]
)

txsupport_agent = Agent(
    name="Technical Support Agent",
    instructions="You are a senior technical support engineer. Help users with technical issues. Transer them to the triage or billing bots where necessary.",
    model=gemini_model,
    tools=[transfer_to_triage, transfer_to_billing]
)

billing_agent = Agent(
    name="Billing Agent",
    instructions="You are an expert assistant at billing and invoicing. Help the user with billing questions and issues. Transfer them to the triage or technical support agents where necessary.",
    model=gemini_model,
    tools=[transfer_to_triage, transfer_to_txsupport]
)


def run_support_chat():
    print("Multi-Agent Customer Support is active!")
    print("Type 'exit' to end session.\n")

    state["active_agent"] = triage_agent
    messages = []

    while True:
        user_input = input("User: ")

        if user_input.lower() == "exit":
            break

        messages.append({"role": "user", "content": user_input})

        turn_result = Runner.run_sync(state["active_agent"], messages)

        print(f"{state['active_agent'].name}: {turn_result.final_output}")

        messages.append(f"{state['active_agent'].name}: {turn_result.final_output}")

        # print(f"{messages}\n")


# Main Function

run_support_chat()