from google import genai

# Put your actual Gemini key here
API_KEY = "AQ.Ab8RN6JzRsIMZ4LZQg3EkDxL6qFAW5rRLk6yi4V0GkTqF2p06w"

client = genai.Client(api_key=API_KEY)

# Use Gemini 3.5 Flash-Lite (fastest response, rarely overloaded)
response = client.models.generate_content(
    model="gemini-3.5-flash-lite",
    contents="Explain artificial intelligence in simple terms."
)

print(response.text)

