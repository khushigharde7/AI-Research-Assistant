import streamlit as st

from research_agent import ResearchAgent
from summary_agent import SummaryAgent
from report_agent import ReportAgent


# ============================================
# PAGE CONFIGURATION
# ============================================

st.set_page_config(
    page_title="AI Research Assistant",
    page_icon="🔎",
    layout="wide"
)


# ============================================
# CREATE AGENTS
# ============================================

research_agent = ResearchAgent()

summary_agent = SummaryAgent()

report_agent = ReportAgent()


# ============================================
# PAGE HEADER
# ============================================

st.title("🔎 AI Research Assistant")

st.subheader(
    "Multi-Agent AI Research System"
)

st.write(
    """
This application uses three specialized AI agents:

🕵️ **Research Agent**  
Searches the web for relevant information.

📝 **Summary Agent**  
Analyzes and summarizes the research findings.

📊 **Report Agent**  
Generates a structured research report.
"""
)


# ============================================
# SIDEBAR
# ============================================

with st.sidebar:

    st.header("⚙️ Configuration")

    st.write(
        "AI Research Assistant"
    )

    st.markdown(
        """
### Agents

1. 🕵️ Research Agent
2. 📝 Summary Agent
3. 📊 Report Agent
"""
    )


# ============================================
# USER INPUT
# ============================================

topic = st.text_area(
    "Enter Research Topic",

    placeholder=(
        "Example: "
        "Impact of Generative AI on Software Development"
    ),

    height=120
)


# ============================================
# START RESEARCH BUTTON
# ============================================

start_button = st.button(
    "🚀 Start Research",
    type="primary"
)


# ============================================
# MAIN WORKFLOW
# ============================================

if start_button:

    if not topic.strip():

        st.warning(
            "⚠️ Please enter a research topic."
        )

    else:

        try:

            # ==================================
            # AGENT 1
            # ==================================

            with st.status(
                "🕵️ Research Agent is searching the web...",
                expanded=True
            ):

                search_results = research_agent.run(
                    topic
                )

                st.write(
                    f"Found {len(search_results)} sources."
                )


            # ==================================
            # DISPLAY WEB RESULTS
            # ==================================

            st.header(
                "🌐 Web Research Results"
            )

            for index, result in enumerate(
                search_results,
                start=1
            ):

                title = result.get(
                    "title",
                    "No title"
                )

                snippet = result.get(
                    "snippet",
                    "No description"
                )

                url = result.get(
                    "url",
                    ""
                )

                with st.expander(
                    f"{index}. {title}"
                ):

                    st.write(snippet)

                    if url:

                        st.markdown(
                            f"[🔗 Open Source]({url})"
                        )


            # ==================================
            # AGENT 2
            # ==================================

            with st.status(
                "📝 Summary Agent is analyzing findings...",
                expanded=True
            ):

                summary = summary_agent.run(
                    topic,
                    search_results
                )


            # ==================================
            # DISPLAY SUMMARY
            # ==================================

            st.header(
                "📝 Research Summary"
            )

            st.markdown(summary)


            # ==================================
            # AGENT 3
            # ==================================

            with st.status(
                "📊 Report Agent is generating the final report...",
                expanded=True
            ):

                report = report_agent.run(
                    topic,
                    summary,
                    search_results
                )


            # ==================================
            # DISPLAY FINAL REPORT
            # ==================================

            st.header(
                "📊 Final Research Report"
            )

            st.markdown(report)


            # ==================================
            # DOWNLOAD REPORT
            # ==================================

            st.download_button(
                label="📥 Download Research Report",

                data=report,

                file_name="research_report.md",

                mime="text/markdown"
            )


            st.success(
                "✅ Research completed successfully!"
            )


        except Exception as error:

            st.error(
                f"❌ An error occurred: {error}"
            )