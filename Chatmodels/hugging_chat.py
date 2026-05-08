import os
from dotenv import load_dotenv
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-V4-Pro",
    huggingfacehub_api_token=os.getenv("HUGGINGFACE_API_TOKEN")
)

model = ChatHuggingFace(llm=llm)

response = model.invoke("who are you ? ")

print(response.content)