from dotenv import load_dotenv
import os
from openai import OpenAI, AuthenticationError

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    print("OPENAI_API_KEY not found in environment. Please set it in a .env file.")
    client = None
else:
    client = OpenAI(api_key=api_key)

def qualify_lead(lead):
    if not client:
        return "LOW"  # Default if no API key

    prompt = f"""
    Classify this lead as HIGH, MEDIUM, or LOW:

    Name: {lead['name']}
    Job: {lead['job']}
    Company: {lead['company']}
    """

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content.strip()
    except AuthenticationError:
        print("Invalid OpenAI API key. Please check your OPENAI_API_KEY.")
        return "LOW"