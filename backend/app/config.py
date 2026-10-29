import os
from dotenv import load_dotenv

load_dotenv()


class Settings:

    PROJECT_NAME = "TITAN AI Trading Bot"

    DATABASE_URL = os.getenv(
        "DATABASE_URL",
        "postgresql://postgres:postgres@localhost/titan"
    )

    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

    GROK_API_KEY = os.getenv("GROK_API_KEY")

    CLAUDE_API_KEY = os.getenv("CLAUDE_API_KEY")

    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

    DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")


settings = Settings()
