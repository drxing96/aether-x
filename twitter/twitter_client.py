import tweepy
from config import (
    TWITTER_API_KEY,
    TWITTER_API_SECRET,
    TWITTER_ACCESS_TOKEN,
    TWITTER_ACCESS_TOKEN_SECRET
)
from utils.logger import get_logger

logger = get_logger(__name__)

def create_twitter_client():
    """
    Creates and returns a Tweepy API client using credentials from config.
    """
    if not all([TWITTER_API_KEY, TWITTER_API_SECRET, TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET]):
        logger.error("Twitter API credentials are missing or incomplete.")
        return None

    auth = tweepy.OAuth1UserHandler(
        TWITTER_API_KEY,
        TWITTER_API_SECRET,
        TWITTER_ACCESS_TOKEN,
        TWITTER_ACCESS_TOKEN_SECRET
    )
    return tweepy.API(auth)

def post_tweet(tweet_text: str) -> None:
    """
    Posts a tweet to Twitter.
    """
    api = create_twitter_client()
    if not api:
        logger.error("Twitter client not initialized. Cannot post tweet.")
        return

    try:
        api.update_status(tweet_text)
        logger.info(f"Tweet posted successfully: {tweet_text}")
    except Exception as e:
        logger.error(f"Error posting tweet: {e}")