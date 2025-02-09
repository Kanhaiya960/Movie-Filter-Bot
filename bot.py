# bot.py
from pyrogram import Client, filters
from pyrogram.types import Message
from handlers.start import start_handler
from handlers.search import search_handler
from handlers.admin import admin_handler

app = Client("movie_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# Add handlers
app.on_message(filters.command("start"))(start_handler)
app.on_message(filters.command("search"))(search_handler)
app.on_message(filters.command("addmovie"))(admin_handler)

# Handle button clicks
@app.on_message(filters.text)
def handle_buttons(client, message: Message):
    text = message.text
    if text == "UPDATES":
        message.reply_text("Latest updates for the bot will be shown here.")
    elif text == "FEATURES":
        message.reply_text("Here are the features of the bot:\n- Search movies\n- Get download links\n- Admin panel")
    elif text == "HELP":
        message.reply_text("How to use the bot:\n- Use /search <movie_name> to find movies.\n- Contact support for more help.")
    elif text == "ABOUT":
        message.reply_text("This bot is maintained by YOUR NAME. It provides movie and series download links.")
    elif text == "FREE PREMIUM":
        message.reply_text("Get free premium access by sharing the bot with 5 groups.")
    elif text == "BUY PREMIUM":
        message.reply_text("To buy premium, contact @your_username.")

print("Bot is running...")
app.run()
