
import argparse
from app.summarizer import summarize_text

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Summarize text via LangChain.")
    parser.add_argument("text", type=str, help="Text to summarize")
    args = parser.parse_args()

    print("Summary:\n")
    print(summarize_text(args.text))
