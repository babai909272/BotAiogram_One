from aiogram import Bot, types
from aiogram.utils import executor
from aiogram.dispatcher import Dispatcher
from config import API_TOKEN


bot = Bot(API_TOKEN, parse_mode="HTML")
dp = Dispatcher(bot)


executor.start_polling(dp, skip_updates=True)
