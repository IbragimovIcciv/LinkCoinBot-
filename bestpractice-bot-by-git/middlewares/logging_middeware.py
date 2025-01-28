from aiogram import BaseMiddleware


class CustomLoggingMiddleware(BaseMiddleware):
    async def __call__(self, handler, event, data):
        print(f"Logging event: {event}")
        return await handler(event, data)
