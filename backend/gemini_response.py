import os
from groq import Groq

client = Groq(

    api_key=os.getenv("GROQ_API_KEY")
)

def generate_response(

    user_query,

    legal_context
):

    prompt = f"""
You are a legal AI assistant.

Answer in simple and easy English.

IMPORTANT RULES:
- Give answers in proper structured format
- Use headings
- Use bullet points
- Keep explanations short and clear
- Avoid very long paragraphs
- Make answers easy for students to understand

User Question:
{user_query}

Legal Context:
{legal_context}

Generate a clean and structured legal explanation.
"""

    chat_completion = client.chat.completions.create(

        messages=[

            {
                "role": "user",

                "content": prompt
            }
        ],

        model="llama-3.1-8b-instant"
    )

    return chat_completion.choices[0].message.content