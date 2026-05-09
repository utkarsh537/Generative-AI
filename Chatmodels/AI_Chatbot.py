from dotenv import load_dotenv
load_dotenv()
from langchain.core_messages import AIMessages, SystemMessages, HumanMessages
from langchain_mistralai import ChatMistralAI
model = ChatMistralAI(model="mistral-small-2506", temperature=0.9)
messages = [
    SystemMessages(content="you are the funny and helpful assistant")
]
print("------Welcome to the AI Chatbot! Type 'exit' to end the conversation.------")
while True:
    prompt = input("You: ")
    messages.append(HumanMessages(content=prompt))
    if prompt.lower() == "exit":
        print("AI: Goodbye!")
        break
    response = model.invoke(messages)
    messages.append(AIMessages(content=response.content))
    print(f"AI: {response.content}")
print(messages)
    