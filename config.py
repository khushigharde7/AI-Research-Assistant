import os

from dotenv import load_dotenv


# Load variables from .env
load_dotenv()


# Get OpenAI API key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


# Model used by the agents
MODEL_NAME = "gpt-4o-mini"


# Check whether API key exists
if not OPENAI_API_KEY:
    raise ValueError(
        "OPENAI_API_KEY is missing. "
        "Please add your API key to the .env file."
    )