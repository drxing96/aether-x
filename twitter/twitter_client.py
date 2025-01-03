# twitter_client.py

from twython import Twython
from config import (
    TWITTER_CONSUMER_KEY,
    TWITTER_CONSUMER_SECRET,
    TWITTER_ACCESS_TOKEN,
    TWITTER_ACCESS_TOKEN_SECRET
)
from utils.logger import get_logger

logger = get_logger(__name__)

def create_twitter_client():
    """
    Creates and returns a Twython client using credentials from config.
    """
    if not all([
        TWITTER_CONSUMER_KEY,
        TWITTER_CONSUMER_SECRET,
        TWITTER_ACCESS_TOKEN,
        TWITTER_ACCESS_TOKEN_SECRET
    ]):
        logger.error("Twitter API credentials are missing or incomplete.")
        return None

    # Initialize Twython client with your consumer keys/tokens
    return Twython(
        TWITTER_CONSUMER_KEY,
        TWITTER_CONSUMER_SECRET,
        TWITTER_ACCESS_TOKEN,
        TWITTER_ACCESS_TOKEN_SECRET
    )

def post_tweet(tweet_text: str) -> None:
    """
    Posts a tweet to Twitter via Twython.
    """
    client = create_twitter_client()
    if not client:
        logger.error("Twitter client not initialized. Cannot post tweet.")
        return

    try:
        client.update_status(status=tweet_text)
        logger.info(f"Tweet posted successfully: {tweet_text}")
    except Exception as e:
        logger.error(f"Error posting tweet: {e}")