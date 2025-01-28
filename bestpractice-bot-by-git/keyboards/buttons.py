from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

balance = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Balance"), KeyboardButton(text="Referral"),
     KeyboardButton(text="Send Coin")],
], resize_keyboard=True)
