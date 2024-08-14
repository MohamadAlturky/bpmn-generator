from dotenv import load_dotenv
import os

load_dotenv()

class Settings:
    def __init__(self):
        self.environment = os.getenv("ENVIRONMENT", "DEVELOPMENT")
        self.llm_provider = os.getenv("LLM_PROVIDER", "GROQ")

    def __repr__(self):
        return f"Settings(environment={self.environment}, llm_provider={self.llm_provider})"

def get_settings():
    return Settings()