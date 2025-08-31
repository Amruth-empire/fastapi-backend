import os
from dotenv import load_dotenv

# Load variables from .env
load_dotenv()

class Settings:
    MONGO_URI: str = os.getenv("MONGO_URI", "mongodb://localhost:27017")
    MONGO_DB: str = os.getenv("MONGO_DB", "fastapi_db")

# Create a settings instance
settings = Settings()
