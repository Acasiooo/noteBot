from aiogram import Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import Dispatcher
from config import TOKEN
from data_base import db

storage = MemoryStorage()


CONN = db.create_connection()
db.create_table(CONN)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot, storage=storage)