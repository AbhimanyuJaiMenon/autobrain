from agents import create_agent

product_manager_chain = create_agent(
    role="Product Manager",
    description="Your job is to turn ideas into a concrete product vision, understand the target market, and define the core features."
)

def product_manager(user_input):
    return product_manager_chain.run(user_input)
