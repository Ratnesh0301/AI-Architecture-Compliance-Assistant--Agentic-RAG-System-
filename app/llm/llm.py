from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def get_llm_response(prompt):
    response = client.chat.completions.create(
        model = "qwen/qwen3-32b",
        messages=[{"role":"user","content":prompt}],
        temperature=0.3
        )
    return response.choices[0].message.content