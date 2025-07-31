from agents import create_agent

developer_chain = create_agent(
    role="Software Developer",
    description="You're responsible for designing the system architecture and technical implementation details based on the product manager's vision."
)

def developer(pm_output):
    return developer_chain.run(pm_output)
