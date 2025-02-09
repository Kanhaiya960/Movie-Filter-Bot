# handlers/start.py
from pyrogram import filters
from pyrogram.types import Message, ReplyKeyboardMarkup
from config import ADMIN_ID
from database.db import add_user

def start_handler(client, message: Message):
    user_id = message.from_user.id
    add_user(user_id)

    # Create a custom keyboard
    keyboard = ReplyKeyboardMarkup(
        [
            ["UPDATES", "FEATURES"],
            ["HELP", "ABOUT"],
            ["FREE PREMIUM", "BUY PREMIUM"]
        ],
        resize_keyboard=True  # Makes the keyboard smaller
    )

    # Send the welcome message with the custom keyboard
    message.reply_text(
        "OWNER : YOUR NAME\n\n"
        "GROUP : MOVIE GROUP\n\n"
        "MOVIE CHANNEL : MOVIE CHANNEL\n\n"
        "MAINTAINED BY - YOUR NAME\n\n"
        "ADD ME TO YOUR GROUP",
        reply_markup=keyboard
    )
