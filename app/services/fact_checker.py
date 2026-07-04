import requests
from urllib.parse import quote
from app.config import FACT_CHECK_API


def fact_check(query: str) -> str:
    try:
        url = f"{FACT_CHECK_API}/{quote(query.replace(' ', '_'))}"

        headers = {
            "User-Agent": "PersonalizedNetworkingAssistant/1.0 (student-project)"
        }

        response = requests.get(
            url,
            headers=headers,
            timeout=10
        )

        print("URL:", url)
        print("Status:", response.status_code)

        if response.status_code != 200:
            return response.text

        data = response.json()
        return data.get("extract", "No summary found.")

    except Exception as e:
        return str(e) 