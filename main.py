import asyncio
import os
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv

from logger import logger
from command_handler import command_router

load_dotenv()

async def main():
    bot_token = os.getenv("BOT_TOKEN")
    bot = Bot(token=bot_token)
    dp = Dispatcher()
    dp.include_routers(command_router)
    logger.info("Starting bot ...")
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
