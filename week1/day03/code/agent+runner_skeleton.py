from agents import Agent

billing_agent = Agent(
    name="Billing Agent",
    instructions="You take care of the billing operations for the user"
)

def transfer_to_billing():
    """Call this function when the task involves billing to pass to the billing agent"""
    # Learned that docstring is read by the agent to know the intent/use-case of the tool(fucntion) and not just to decsribe the function to another dev
    return billing_agent

triage_agent = Agent(
    name="Triage Agent",
    instructions="You get alll the necessary info from the user and pass to the agent fit for the next task",
    tools=[transfer_to_billing]
)
