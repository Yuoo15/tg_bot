from aiogram import Dispatcher, F, Bot
import asyncio
from heandrles import commands_bot, message_user
from data.modules import async_main

async def main():
    await async_main()
    dp = Dispatcher()
    bot = Bot("8357458684:AAEEDpBONTQnUjJ3ZtWkVgzOV5jzJW1rYBU")
    dp.include_routers(
        commands_bot.router,
        message_user.router
    )
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('exit')