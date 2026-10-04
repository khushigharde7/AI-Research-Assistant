🔎 AI-Research-Assistant
 
An AI-powered multi-agent research application that allows users to enter a research topic, search the web for relevant information, summarize the findings, and generate a structured research report.

The application uses three specialized AI agents working together with OpenAI, DDGS web search, and Streamlit.

## Technologies

* Python
* OpenAI API
* DDGS
* Streamlit
* python-dotenv

## Features

* Multi-agent AI research system
* Web search
* Automatic research collection
* AI-powered summarization
* Structured research report generation
* Source citations
* OpenAI API integration
* Streamlit interface

## Setup

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```env
OPENAI_API_KEY=your_api_key
```

Run the application:

```bash
streamlit run app.py
```

## Example

Enter a research topic such as:

```text
Impact of Generative AI on Software Development
```

The application will:

1. Search the web for relevant information.
2. Collect search results.
3. Summarize the findings.
4. Generate a structured research report.
5. Display source URLs.

Other example topics:

```text
Future of Agentic AI
```

```text
Applications of Artificial Intelligence in Healthcare
```

```text
Impact of AI on Cybersecurity                                                               