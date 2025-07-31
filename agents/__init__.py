from langchain_community.llms import Ollama
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory
from langchain.prompts import PromptTemplate

llm = Ollama(model="llama3")

def create_agent(role: str, description: str) -> LLMChain:
    prompt = PromptTemplate(
        input_variables=["input", "history"],
        template=(
            "You are a highly skilled {role}.\n"
            "{description}\n"
            "Conversation history:\n{history}\n"
            "Current task: {input}\n"
            "Your response:"
        )
    )
    memory = ConversationBufferMemory(memory_key="history")
    return LLMChain(llm=llm, prompt=prompt, memory=memory)
