from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram import Dispatcher
from aiogram.dispatcher.filters.state import State, StatesGroup
from data_base import db, sql_query
import create_bot

class FsmAdmin(StatesGroup):
    note_name = State()
    note_text = State()


async def cm_start(message: types.Message):
    await FsmAdmin.note_name.set()
    await message.reply('Напиши название заметки:')


async def load_note_name(message: types.message, state: FSMContext):
    async with state.proxy() as data:
        data["note_name"] = message.text
    await FsmAdmin.next()
    await message.reply("Теперь напиши содержание:")


async def load_note_text(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["note_text"] = message.text
    
    async with state.proxy() as data:
        db.insert_into(create_bot.CONN, sql_query=sql_query.INSERT_INTO, param=[message.from_user.id, str(data['note_name']), str(data['note_text'])])
    
    await message.answer("Новая заметка добавлена")
    await state.finish()



def register_fsm(dp: Dispatcher):
    dp.register_message_handler(cm_start, commands=['add', 'add_new'], state=None)
    dp.register_message_handler(load_note_name, content_types=['text'], state=FsmAdmin.note_name)
    dp.register_message_handler(load_note_text, state=FsmAdmin.note_text)
    