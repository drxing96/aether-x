import openai
from config import OPENAI_API_KEY
from utils.logger import get_logger

logger = get_logger(__name__)

# Set the API key globally
openai.api_key = OPENAI_API_KEY

def generate_tweet_draft(news_summary: str) -> str:
    """
    Takes a text summary of news and generates a tweet-friendly message.
    """

    if not OPENAI_API_KEY:
        logger.warning("OPENAI_API_KEY is not set. Returning an empty tweet draft.")
        return ""

    prompt = (
        "Based on the following news summary, craft a concise tweet (280 characters max). "
        "Make it engaging and factual:\n\n" + news_summary
    )

    try:
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            max_tokens=60,  # Enough for a concise tweet
            temperature=0.7
        )
        tweet_text = response["choices"][0]["text"].strip()
        logger.info("Generated tweet draft via OpenAI.")
        return tweet_text
    except Exception as e:
        logger.error(f"Error generating tweet with OpenAI: {e}")
        return "Could not generate tweet."