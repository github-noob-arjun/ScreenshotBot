from pyrogram import Client

from .config import Config


ScreenShotBot = Client(
    session_name=Config.SESSION_NAME,
    bot_token = Config.BOT_TOKEN,
    api_id = Config.API_ID,
    api_hash = Config.API_HASH,
    workers = 20,
    root="bot/plugins"
)
        
