# inference.py
#We are importing the necessary libraries and loading the environment variables.
# We are also loading the dataset from a JSONL file and creating a system prompt with few-shot examples.
# Finally, we are using the Google Generative AI API to generate a response based on the user input.
import google.generativeai as genai
import json
from dotenv import load_dotenv

load_dotenv()
# Load examples from dataset.jsonl
examples = []
with open("dataset.jsonl", "r", encoding="utf-8") as f:
    for line in f:
        data = json.loads(line.strip())
        prompt = data['prompt']
        completion = data['completion']
        examples.append(f"{prompt.strip()} {completion.strip()}")

# Build system prompt dynamically
few_shot_examples = "\n\n".join(examples)
system_prompt = f"""You are a friendly Hinglish-speaking AI assistant. Respond casually mixing Hindi and English naturally.

Here are some examples:
{few_shot_examples}

(Answer all future questions in this same Hinglish style.)
"""

# User query
user_prompt = input("User: ")

# Load model
model = genai.GenerativeModel('gemini-1.5-flash')

# Generate response
response = model.generate_content([
    {"role": "user", "parts": [system_prompt]},
    {"role": "user", "parts": [user_prompt]}
])

print("Assistant:", response.text)
