# ui/streamlit_app.py

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
from app.summarizer import summarize_text

st.title("📝 LangChain Text Summarizer")

with st.expander("Enter text to summarize"):
    input_text = st.text_area("Paste your text here")

if st.button("Summarize"):
    if input_text:
        summary = summarize_text(input_text)
        st.success(summary)
    else:
        st.warning("Please enter some text to summarize.")
