from ddgs import DDGS


def search_web(query, max_results=8):
    """
    Search the web using DDGS.

    Parameters:
        query: Research topic
        max_results: Maximum number of results

    Returns:
        List of search results
    """

    results = []

    try:

        with DDGS() as ddgs:

            search_results = ddgs.text(
                query,
                max_results=max_results
            )

            for result in search_results:

                results.append(
                    {
                        "title": result.get(
                            "title",
                            ""
                        ),

                        "url": result.get(
                            "href",
                            ""
                        ),

                        "snippet": result.get(
                            "body",
                            ""
                        )
                    }
                )

    except Exception as error:

        results.append(
            {
                "title": "Search Error",
                "url": "",
                "snippet": str(error)
            }
        )

    return results