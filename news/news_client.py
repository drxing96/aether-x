import requests
from config import NEWS_API_KEY
from utils.logger import get_logger

logger = get_logger(__name__)

def fetch_latest_news():
    """
    Fetches the latest news headlines using NewsAPI.
    Returns a list of articles (each article is a dict).
    """

    if not NEWS_API_KEY:
        logger.warning("NEWS_API_KEY is not set. Returning empty list.")
        return []

    url = "https://newsapi.org/v2/top-headlines"
    params = {
        "country": "us",
        "apiKey": NEWS_API_KEY,
        "pageSize": 5  # Limit to 5 top headlines
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        articles = data.get("articles", [])
        logger.info(f"Fetched {len(articles)} articles from NewsAPI.")
        return articles
    except Exception as e:
        logger.error(f"Error while fetching news: {e}")
        return []