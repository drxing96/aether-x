import time
from news.news_client import fetch_latest_crypto_news
# from openai.openai_client import generate_tweet_draft
# from twitter.twitter_client import post_tweet
from utils.logger import get_logger

logger = get_logger(__name__)

def summarize_articles(articles):
    """
    Creates a simple text summary of the articles for the GPT prompt.
    You could make this more sophisticated.
    """
    summary = ""
    for article in articles:
        title = article.get("title", "No title")
        source = article.get("source_info", {}).get("name", "Unknown source")
        summary += f"- {title} ({source})\n"
    return summary

def main():
    logger.info("Starting daily news tweet workflow...")

    # 1. Fetch the latest news
    articles = fetch_latest_crypto_news()
    if not articles:
        logger.warning("No articles fetched. Exiting...")
        return

    # 2. Summarize the news
    news_summary = summarize_articles(articles)
    logger.debug(f"News Summary:\n{news_summary}")

    # # 3. Generate a tweet draft using OpenAI
    # tweet_text = generate_tweet_draft(news_summary)
    # logger.debug(f"Draft tweet: {tweet_text}")

    # # 4. Post the tweet to Twitter
    # post_tweet(tweet_text)

    # logger.info("Completed daily news tweet workflow.")

if __name__ == "__main__":
    main()