# handlers/admin.py
from pyrogram import filters
from pyrogram.types import Message
from config import ADMIN_ID
from database.db import add_movie

def admin_handler(client, message: Message):
    user_id = message.from_user.id
    if user_id != ADMIN_ID:
        message.reply_text("You are not authorized to use this command.")
        return

    if len(message.command) < 3:
        message.reply_text("Usage: /addmovie <title> <download_link>")
        return

    title = message.command[1]
    download_link = message.command[2]
    add_movie(title, download_link)
    message.reply_text(f"Movie '{title}' added successfully!")
