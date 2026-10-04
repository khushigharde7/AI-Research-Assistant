from web_search import search_web


class ResearchAgent:

    def __init__(self):

        self.name = "Research Agent"


    def run(self, topic):

        """
        Search the web for the research topic.
        """

        results = search_web(
            query=topic,
            max_results=8
        )

        return results