# LangChain Text Summarization


The main purpose of this project is to demonstrate how LangChain can be integrated with a language model. It serves as a simple starting point for working with LangChain.
This project is a text summarization tool built using **LangChain**, **OpenAI**, and **Streamlit**. It allows users to input any text and receive a concise summary, accessible via both a web interface and the command line.


---

<details>
<summary><strong>Features</strong></summary>

- LangChain integration for clean prompt chaining
- Streamlit web UI for interactive usage
- CLI mode via `main.py`
- .env support for API key management
- Modular code structure (LLM config, summarizer, UI)
</details>

---

<details>
<summary><strong>Quickstart</strong></summary>

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/text-summarization.git
cd text-summarization
```

### 2. Create a virtual env and activate it

```bash
conda create --name txtsum python=3.11
conda activate txtsum
```

### 3. install the requirments

```bash
pip install -r requirements.txt

```

### 4. Run the pipeline using streamlit

```bash
streamlit run ui/streamlit_app.py
```
