# app/summarizer.py

from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from app.llm_config import get_llm

def summarize_text(text: str) -> str:
    template = PromptTemplate(
        input_variables=["text"],
        template="Summarize the following text:\n\n{text}"
    )
    chain = LLMChain(llm=get_llm(), prompt=template)
    return chain.run(text)
