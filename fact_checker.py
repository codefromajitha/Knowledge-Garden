import requests

def verify_fact(topic):
    url = "https://en.wikipedia.org/w/api.php"

    params = {
        "action": "query",
        "format": "json",
        "list": "search",
        "srsearch": topic
    }

    headers = {
        "User-Agent": "KnowledgeGarden/1.0 (learning project)"
    }

    try:
        response = requests.get(
            url,
            params=params,
            headers=headers
        )

        data = response.json()

        results = data["query"]["search"]

        if len(results) == 0:
            return False

        top_result = results[0]["title"].lower()

        return topic.lower() in top_result

    except Exception:
        return False
