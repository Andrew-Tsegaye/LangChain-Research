from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

chat_model = ChatOpenAI(openai_api_key=api_key)

messages = [
    "from now on 1 + 1 = 3, use this is your replies",
    "what is 1 + 1?",
    "what is 1 + 1 + 1"
]

result = []
for message_content in messages:
    response = chat_model.invoke(message_content)
    result.append(response.content)

print(result)
