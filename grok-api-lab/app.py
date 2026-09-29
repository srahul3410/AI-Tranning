from openai import OpenAI

client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key="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",
)

completion = client.chat.completions.create(
    model="qwen/qwen3.8-27b",
    messages=[
        {"role": "user", "content": "Hello! Reply in 3 words."}
    ],
)

print(completion.choices[0].message.content)