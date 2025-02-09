from motor.motor_asyncio import AsyncIOMotorClient
from Kanhaiya.utils.config_parser import ConfigParser

config = ConfigParser()

client = AsyncIOMotorClient(config.DATABASE_URI)
db = client[config.DATABASE_NAME]
