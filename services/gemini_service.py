import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

MODEL_NAME = os.getenv(
    "GEMINI_MODEL",
    "gemini-3.1-flash-lite"
)


def generate_summary(text):

    prompt = f"""
You are an AI Research Assistant.

Summarize the following research paper.

Research Paper:
{text}

Provide:

1. Overview

2. Methodology

3. Results

4. Conclusion
"""

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt
    )

    return response.text


def extract_key_contributions(text):

    prompt = f"""
You are an expert AI Research Assistant.

Read the following research paper carefully.

Extract ONLY the top 5 research contributions.

Rules:
- Return exactly 5 bullet points.
- Do NOT use Markdown.
- Do NOT use **bold**.
- Do NOT use numbering.
- Each bullet should be one concise sentence.
- Maximum 35 words per bullet.

Research Paper:

{text}
"""

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt
    )

    return response.text

def answer_question(text, question, history):
    conversation = ""

    recent_history = history[-10:]   # Keep only the last 10 messages

    for message in recent_history:
        role = "User" if message["role"] == "user" else "Assistant"
        conversation += f"{role}: {message['content']}\n"

    prompt = f"""
You are an expert AI Research Assistant.

Your job is to answer questions ONLY from the uploaded research paper.

Guidelines:
- Use ONLY information from the uploaded paper.
- Use the previous conversation only to understand follow-up questions.
- Never invent facts.
- If the answer is missing, reply exactly:
"The uploaded paper does not contain this information."
- Use headings and bullet points whenever appropriate.
- Keep answers concise, accurate, and easy to understand.

Previous Conversation:
{conversation}

Research Paper:
{text}

Current Question:
{question}
"""

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt
    )

    return response.text

def basic_summary(text):

    prompt = f"""
Summarize the following research paper.

{text}
"""

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt
    )

    return response.text

def advanced_summary(text):

    prompt = f"""
You are an expert AI Research Assistant.

Read the research paper carefully.

Generate a structured summary.

Include:

1. Overview
2. Methodology
3. Results
4. Key Contributions
5. Future Scope

Keep it concise.
Do not use unnecessary introductions.

Research Paper:

{text}
"""

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt
    )

    return response.text