from agents import create_agent

marketer_chain = create_agent(
    role="Marketing Strategist",
    description="You create a go-to-market strategy, messaging, and channels to acquire users based on the product manager’s plan."
)

def marketer(pm_output):
    return marketer_chain.run(pm_output)
