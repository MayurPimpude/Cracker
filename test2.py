# Install the library (if you haven't already)
# !pip install google-generativeai
import os
import google.generativeai as genai
from dotenv import load_dotenv
# Replace with your Gemini API key

load_dotenv()

# Configure Google generative AI
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Define your question
question = "What is the capital of France?"

# Choose the Gemini model (text generation)
model = genai.GenerativeModel("gemini-1.0-pro")

# Generate the answer
response = model.generate_content(question)

# Print the answer
print(f"Answer: {response.text}")
