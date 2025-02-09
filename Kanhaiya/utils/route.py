from pyrogram import filters
from pyrogram.types import Message
from Kanhaiya.plugins.commands import start_command, help_command, search_command

def setup_routes(app):
    @app.on_message(filters.command("start"))
    async def start_handler(_, message: Message):
        await start_command(message)

    @app.on_message(filters.command("help"))
    async def help_handler(_, message: Message):
        await help_command(message)

    @app.on_message(filters.command("search"))
    async def search_handler(_, message: Message):
        await search_command(message)
