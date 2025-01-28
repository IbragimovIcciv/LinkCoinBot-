from config import BOT_TOKEN
from aiogram import Bot

bot = Bot(token=BOT_TOKEN)


async def send_notification(user_id: int, img_url: str, message_text: str):
    return await bot.send_photo(chat_id=user_id, photo=img_url, caption=message_text)