import urllib.parse
import requests

def wiki(text: str) -> str:
    encoded = urllib.parse.quote(text)
    url = f"https://ru.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext&format=json&titles={encoded}"

    response = requests.get(url)
    data = response.json()

    # Извлекаем текст
    page = next(iter(data["query"]["pages"].values()))
    if "extract" in page:
        clean_text = page["extract"]
        return clean_text
    else:
        return "Информация не найдена."