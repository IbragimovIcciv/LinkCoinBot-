from aiogram.fsm.state import State, StatesGroup


class SendCoins(StatesGroup):
    token = State()
    amount = State()
    note = State()
