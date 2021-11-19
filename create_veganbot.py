from aiogram import Bot, Dispatcher
from Token_Veg import token_veg
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()

bot = Bot(token_veg, parse_mode="HTML")
dp = Dispatcher(bot, storage=storage)