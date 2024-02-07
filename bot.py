import asyncio

from aiogram import Bot, Dispatcher
from config_data.config import Config, load_config
from handlers import other_handlers, user_handlers


async def main():
    """function to configurate and run the bot"""

    # loading config to variable
    config: Config = load_config()
    # initializing bot and dispatcher
    bot = Bot(token=config.tg_bot.token)
    dp = Dispatcher()

    # registering routers in dispatcher
    dp.include_router(user_handlers.router)
    dp.include_router(other_handlers.router)

    # passing accumulated updates and run polling
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
