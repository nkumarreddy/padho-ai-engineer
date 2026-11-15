import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("API key not found")

client = Groq(api_key=my_api_key)
model = "openai/gpt-oss-120b"
role="user"
prompt="Suggest a name for my clothing company to open in India, suggest 5 names"
message_system={
    "role":"system",
    "content":"you are a brand manager who suggests name for my clothing company , name should be in one word "
}
message={
    "role":role,
    "content":prompt
}

messages=[message_system,message]
# Temprerature by default is 0 meaning safe, 1 meaning medium creativity , 2 means extreme creativity
response=client.chat.completions.create(model=model,messages=messages,temperature=1)
#print(response)

print("###################################")

answer=response.choices[0].message.content
print(answer)