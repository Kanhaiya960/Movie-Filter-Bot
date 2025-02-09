from pyrogram import Client, filters
from pyrogram.types import Message
from Kanhaiya.utils.config_parser import ConfigParser
from Kanhaiya.utils.clients import initialize_clients
from Kanhaiya.route import setup_routes
import logging

# Load configuration
config = ConfigParser()

# Initialize logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize the bot
app = Client(
    "MovieFilterBot",
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    bot_token=config.BOT_TOKEN
)

# Initialize clients (if any)
clients = initialize_clients(config)

# Setup routes (handlers)
setup_routes(app)

# Start the bot
if __name__ == "__main__":
    logger.info("Starting Movie Filter Bot...")
    app.run()
