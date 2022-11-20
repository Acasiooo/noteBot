from aiogram.utils import executor
from create_bot import dp
from handlers import user
from handlers import admin

admin.register_fsm(dp)
user.register_message(dp)

if __name__ == '__main__':
    executor.start_polling(dp)