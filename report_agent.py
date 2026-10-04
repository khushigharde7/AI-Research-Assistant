from llm_service import ask_llm


class ReportAgent:

    def __init__(self):

        self.name = "Report Agent"


    def run(
        self,
        topic,
        summary,
        search_results
    ):

        """
        Generate the final structured
        research report.
        """

        sources = ""

        for index, result in enumerate(
            search_results,
            start=1
        ):

            sources += f"""
{index}. {result.get("title", "")}
URL: {result.get("url", "")}
"""


        prompt = f"""
You are the Report Agent in a
multi-agent AI research system.

Research Topic:
{topic}

The Summary Agent produced:

{summary}

Original research sources:

{sources}

Create a professional research report.

Use exactly this structure:

# Research Report

## 1. Executive Summary

Provide a concise overview.

## 2. Introduction

Explain the topic and why it matters.

## 3. Key Findings

Present the most important findings.

## 4. Detailed Analysis

Explain the findings in detail.

## 5. Benefits and Opportunities

Discuss benefits, applications,
and opportunities.

## 6. Challenges and Limitations

Discuss limitations, risks,
and challenges.

## 7. Future Outlook

Discuss possible future developments.

## 8. Conclusion

Provide a concise conclusion.

## 9. Sources

List the sources and URLs.

Important rules:

- Do not invent facts.
- Do not create fake statistics.
- Use information supported by the research.
- Keep the report professional.
- Preserve source URLs.
- Clearly distinguish facts from interpretation.
"""


        report = ask_llm(prompt)

        return report