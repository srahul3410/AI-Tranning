import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=os.getenv("GROQ_API_KEY"),
)

completion = client.chat.completions.create(
    model="qwen/qwen3.8-27b",
    messages=[
        {"role": "user", "content": "Hello! Reply in 3 words."}
    ],
)

print(completion.choices[0].message.content)