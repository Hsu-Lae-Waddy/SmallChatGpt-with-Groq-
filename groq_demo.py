import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

# 1. Load environment variables
load_dotenv()

# 2. Initialize Groq Chat
groq_chat = ChatGroq(
    model_name="llama3-70b-8192",  # Meta's latest Llama 3 70B
    api_key=os.getenv("GROQ_API_KEY")
)

# 3. User input ကိုရယူပါ
user_question = input("Ask me one Question? : ")

# 4. Model ကို query လုပ်ပါ
response = groq_chat.invoke(user_question)

# 5. အဖြေကိုပြပါ
print("\nGroq AI answer:")
print(response.content)