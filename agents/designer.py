from agents import create_agent

designer_chain = create_agent(
    role="UX/UI Designer",
    description="You focus on user interface, usability, and visual appeal based on the product manager’s idea."
)

def designer(pm_output):
    return designer_chain.run(pm_output)
