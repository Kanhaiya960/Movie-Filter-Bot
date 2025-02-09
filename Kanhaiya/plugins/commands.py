from pyrogram.types import Message

async def start_command(message: Message):
    await message.reply_text("🎬 Welcome to Movie Filter Bot! Use /help to see available commands.")

async def help_command(message: Message):
    await message.reply_text("""
📚 **Available Commands:**
- /start - Start the bot
- /help - Show this help message
- /search <movie_name> - Search for a movie
    """)

async def search_command(message: Message):
    query = " ".join(message.command[1:])
    if not query:
        await message.reply_text("Please provide a movie name to search.")
        return
    # Add movie search logic here
    await message.reply_text(f"🔍 Searching for: {query}")
