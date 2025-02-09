# handlers/search.py
from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from database.db import search_movies

def search_handler(client, message: Message):
    query = " ".join(message.command[1:])
    if not query:
        message.reply_text("Please provide a movie name. Example: /search Inception")
        return

    movies = search_movies(query)
    if not movies:
        message.reply_text("No movies found.")
        return

    for movie in movies:
        keyboard = InlineKeyboardMarkup(
            [[InlineKeyboardButton("Download", url=movie["download_link"])]]
        )
        message.reply_text(
            f"**Title:** {movie['title']}\n"
            f"**Download Link:** [Click Here]({movie['download_link']})",
            reply_markup=keyboard
        )
