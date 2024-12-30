import streamlit as st
import openai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Set the OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

def summarize_text(text, model="gpt-3.5-turbo", max_tokens=150):
    """
    Summarizes the input text using OpenAI API.
    """
    try:
        response = openai.ChatCompletion.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are a helpful assistant that summarizes text."},
                {"role": "user", "content": f"Summarize the following text:\n{text}"}
            ],
            max_tokens=max_tokens,
            temperature=0.7,
        )
        return response["choices"][0]["message"]["content"].strip()
    except Exception as e:
        return f"Error: {e}"

# Streamlit App
st.title("Summarization Chatbot")

# User Input
st.write("Enter your text below, and the chatbot will summarize it for you.")
user_input = st.text_area("Input Text", placeholder="Type or paste your text here...")

if st.button("Summarize"):
    if user_input.strip():
        with st.spinner("Summarizing..."):
            summary = summarize_text(user_input)
        st.write("### Summary:")
        st.write(summary)
    else:
        st.warning("Please enter some text to summarize.")
