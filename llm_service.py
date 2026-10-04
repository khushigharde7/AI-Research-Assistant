from openai import OpenAI

from config import OPENAI_API_KEY, MODEL_NAME


# Create OpenAI client
client = OpenAI(
    api_key=OPENAI_API_KEY
)


def ask_llm(prompt):
    """
    Send a prompt to the OpenAI model
    and return the generated response.
    """

    response = client.chat.completions.create(

        model=MODEL_NAME,

        messages=[
            {
                "role": "system",
                "content": (
                    "You are an intelligent AI research assistant. "
                    "Provide accurate, clear, structured, "
                    "and evidence-based responses. "
                    "Do not intentionally invent facts."
                )
            },
            {
                "role": "user",
                "content": prompt
            }
        ],

        temperature=0.3
    )

    return response.choices[0].message.content