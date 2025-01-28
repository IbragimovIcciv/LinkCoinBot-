from aiogram import Router, F
from services.user import get_user
from aiogram.types import Message

router = Router()


@router.message(F.text == 'Balance')
async def cdm_balance(message: Message):
    user = await get_user(message.from_user.id)
    if user:
        await message.answer(f"{user.balance} 🌕")
    else:
        await message.answer("balance not found")