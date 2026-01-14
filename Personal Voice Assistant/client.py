from google import genai
from google.genai import types

# 1. Initialize the Client
# (The SDK automatically finds your key if set as GEMINI_API_KEY environment variable)
client = genai.Client(api_key="AIzaSyC_vt94zn12zTsEoteabG8cETWpkQJxsFs")

# 2. Generate content using the new structure
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="What is coding?",
    config=types.GenerateContentConfig(
        system_instruction="You are a virtual assistant named Jarvis skilled in general tasks like google and alexa"
    )
)

print(response.text)
