# app/llm_config.py

import os
from langchain.chat_models import ChatOpenAI

def get_llm():
    return ChatOpenAI(
        model="gpt-3.5-turbo",
        temperature=0.3,
        openai_api_key=os.getenv("OPENAI_API_KEY")
    )
