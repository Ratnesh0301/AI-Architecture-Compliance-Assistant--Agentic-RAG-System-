from groq import Groq
import os

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def get_llm_response(prompt):
    response = client.chat.completions.create(
        model = "llama3-8b-8192",
        messages=[{"role":"user","content":prompt}],
        temperature=0.3
        )
    return response.choices[0].message.content