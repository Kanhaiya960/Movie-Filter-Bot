import os

class ConfigParser:
    def __init__(self):
        self.API_ID = int(os.getenv("API_ID", 12345))
        self.API_HASH = os.getenv("API_HASH", "your_api_hash")
        self.BOT_TOKEN = os.getenv("BOT_TOKEN", "your_bot_token")
        self.DATABASE_URI = os.getenv("DATABASE_URI", "mongodb://localhost:27017")
        self.DATABASE_NAME = os.getenv("DATABASE_NAME", "MovieFilterBot")
