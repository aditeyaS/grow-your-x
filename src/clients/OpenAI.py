from ..errors.ApiKeyError import ApiKeyError
import os
from openai import OpenAI as ChatGPT

class OpenAI:
    def __init__(self):
        API_KEY = os.getenv("OPENAI_API_KEY")
        if not API_KEY:
            raise ApiKeyError("Missing OPENAI_API_KEY")
        ORGANIZATION_ID = os.getenv("OPENAI_ORGANIZATION_ID")
        PROJECT_ID = os.getenv("OPENAI_PROJECT_ID")
        self.client = ChatGPT(
            api_key=API_KEY,
            organization=ORGANIZATION_ID,
            project=PROJECT_ID
        )

    def generate_tweet(self, topic):
        chat_completion = self.client.chat.completions.create(
            model= "gpt-3.5-turbo",
            messages = [
                {"role": "system", "content": "You have an insane sense of humor and make creative viral tweets. Write 1 unique tweet about the following topic. Ensure each tweet is under 280 characters. Use only 2 hashtags."},
                {"role": "user", "content": topic}
            ],
            max_tokens=75,
            n=1,
            temperature=0.5
        )
        generated_tweet = chat_completion.choices[0].message.content
        # removing \" from start and end
        generated_tweet = generated_tweet.strip("\"")
        return generated_tweet