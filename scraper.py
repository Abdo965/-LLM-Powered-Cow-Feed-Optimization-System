import requests
from bs4 import BeautifulSoup
#
# from App import scraper


class Scraper:
    def __init__(self, tags=None, max_length=2000):
        self.tags = tags if tags else ['p', 'li']
        self.max_length = max_length

    def fetch(self, url):
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')
            elements = soup.find_all(self.tags)
            text = "\n".join(el.get_text(strip=True) for el in elements if el.get_text(strip=True))
            return {
                'url': url,
                'content': text[:self.max_length]
            }
        except Exception as e:
            return {
                'url': url,
                'content': f"Error: {e}"
            }

