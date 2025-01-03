# news_fetcher.py

import requests
from config import NEWS_API_KEY
from utils.logger import get_logger

logger = get_logger(__name__)

def fetch_latest_crypto_news():
    """
    Fetches the latest crypto-related news from CryptoCompare.
    Returns a list of article dictionaries, each containing keys like 'title', 'url', 'source', etc.
    """

    if not NEWS_API_KEY:
        logger.warning("NEWS_API_KEY is not set. Returning empty list.")
        return []

    # CryptoCompare News endpoint
    url = "https://min-api.cryptocompare.com/data/v2/news/"
    params = {
        "lang": "EN",  # Only English news
        # You can add more parameters if needed, see CryptoCompare docs
    }
    headers = {
        "authorization": f"Apikey {NEWS_API_KEY}",
    }

    try:
        response = requests.get(url, params=params, headers=headers, timeout=10)
        response.raise_for_status()
        data = response.json()

        # The news articles are usually in the "Data" field
        articles = data.get("Data", [])
        logger.info(f"Fetched {len(articles)} articles from CryptoCompare.")
        return articles
    except Exception as e:
        logger.error(f"Error while fetching crypto news from CryptoCompare: {e}")
        return []