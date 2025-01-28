
from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command
from models.user import User
from keyboards.buttons import balance
from services.user import add_user
from config import BOT_USERNAME

router = Router()


@router.message(Command('start'))
async def cmd_start(message: Message):
    referred_by_code = message.text.split(" ")[1] if len(message.text.split()) > 1 else None
    user = await User.get_or_none(tg_id=message.from_user.id)
    if not user:
        await add_user(tg_id=message.from_user.id, full_name=message.from_user.full_name,
                       username=message.from_user.username, referred_by_code=referred_by_code)
        await message.answer(f"{message.from_user.full_name} Welcome! You have been successfully registered.")

    else:
        await message.answer("You are already registered.", reply_markup=balance)


@router.message(F.text == "Referral")
async def my_referrals(message: Message):
    user = await User.get(tg_id=message.from_user.id)
    print(user)
    if not user:
        await message.answer("You are not registered. Please start the bot using /start.")
    else:
        referral_link = f"https://t.me/{BOT_USERNAME}?start={user.referral_code}"
        if user.referral_count > 0:
            await message.answer(
                f"Your referral link: {referral_link}\n"
                f"Number of people referred: {user.referral_count}"
            )
        else:
            await message.answer(
                f"Your referral link: {referral_link}\n"
                f"No one has used your referral link yet."
            )
