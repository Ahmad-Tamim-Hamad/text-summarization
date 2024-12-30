import openai

from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Print the loaded API key
api_key = os.getenv("OPENAI_API_KEY")


def summarize_text(text, model="gpt-3.5-turbo", max_tokens=150):
    """
    Summarizes the input text using OpenAI API.

    Parameters:
    - text (str): The text to summarize.
    - model (str): The OpenAI model to use (default: gpt-3.5-turbo).
    - max_tokens (int): Maximum number of tokens for the summary.

    Returns:
    - str: The summarized text.
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
        summary = response['choices'][0]['message']['content'].strip()
        return summary
    except Exception as e:
        return f"Error: {e}"

# Example Input
input_text = """
Artificial intelligence (AI) is intelligence demonstrated by machines, in contrast to the natural intelligence displayed by humans and animals. Leading AI textbooks define the field as the study of intelligent agents, which refers to any system that perceives its environment and takes actions that maximize its chance of achieving its goals. Some popular accounts use the term artificial intelligence to describe machines that mimic cognitive functions that humans associate with the human mind, such as learning and problem-solving.
"""

# Summarize the Text
summary = summarize_text(input_text)
print("Original Text:")
print(input_text)
print("\nSummary:")
print(summary)
