import openai
from config import OPENAI_API_KEY
from utils.logger import get_logger

logger = get_logger(__name__)

# Set the API key globally
openai.api_key = OPENAI_API_KEY

def generate_tweet_draft(news_summary: str) -> str:
    if not OPENAI_API_KEY:
        logger.warning("OPENAI_API_KEY is not set. Returning an empty tweet draft.")
        return ""

    # Use your real news_summary directly in the prompt
    prompt = (
        "Craft a concise tweet (280 characters max) based on the following news summary. "
        "Keep it factual and engaging. Use relevant crypto hashtags if needed:\n\n"
        f"{news_summary}"
    )

    try:
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            max_tokens=60,      # Enough for a short tweet
            temperature=0.7
        )
        tweet_text = response["choices"][0]["text"].strip()
        logger.info("Generated tweet draft via OpenAI.")
        return tweet_text
    except Exception as e:
        logger.error(f"Error generating tweet with OpenAI: {e}")
        return "Could not generate tweet."