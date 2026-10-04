from llm_service import ask_llm


class SummaryAgent:

    def __init__(self):

        self.name = "Summary Agent"


    def run(self, topic, search_results):

        """
        Analyze the web research results
        and create a research summary.
        """

        formatted_results = ""

        for index, result in enumerate(
            search_results,
            start=1
        ):

            formatted_results += f"""
SOURCE {index}

Title:
{result.get("title", "")}

URL:
{result.get("url", "")}

Content:
{result.get("snippet", "")}

--------------------------------
"""


        prompt = f"""
You are the Summary Agent in a
multi-agent AI research system.

Research Topic:
{topic}

The Research Agent collected
the following web results:

{formatted_results}

Analyze the research.

Requirements:

1. Identify the most relevant information.
2. Remove duplicate information.
3. Extract important facts.
4. Identify major themes.
5. Identify important statistics if available.
6. Identify challenges.
7. Identify conflicting information.
8. Do not invent facts.
9. Preserve source URLs.
10. Clearly distinguish facts from interpretation.

Create this structure:

# Research Summary

## Key Findings

Explain the most important findings.

## Important Facts

List important facts.

## Major Themes

Explain the major themes.

## Important Statistics

Include statistics only when supported
by the provided sources.

## Challenges and Conflicting Information

Explain limitations or disagreements.

## Sources

List relevant source URLs.
"""


        summary = ask_llm(prompt)

        return summary