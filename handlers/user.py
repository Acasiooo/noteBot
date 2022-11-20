from aiogram import types, Dispatcher
from create_bot import dp, bot
from data_base import db, sql_query
import create_bot


async def start_command(message: types.Message):
    text = (
            f'/show  показать заметку\n'
            f'/all  показать все заметки\n\n'
            f'/add  добавить заметку\n'
            f'/del  удалить заметку\n\n'
            f'/help  помощь'
    )

    await message.answer(text)


async def show_note(message: types.Message):
    pass


async def add_note(message: types.Message):
    pass
    

async def delite_note(message: types.Message):
    pass


async def all_notes(message: types.Message):
    data = db.select_from(conn=create_bot.CONN, sql_query=sql_query.SELECT_FROM, param=[message.from_user.id])

    text = ''
    for i in data:
        text += f'{i[0]} {i[1][:15]+"..." if len(i[1])>15 else i[1]}\n'

    await message.answer(text)


async def none(message: types.Message):
    pass


async def none(message: types.Message):
    pass


def register_message(dp: Dispatcher):
    dp.register_message_handler(start_command, commands=["start", "help"])
    dp.register_message_handler(show_note, commands=["show"])
    dp.register_message_handler(add_note, commands=["add", "add_note"])
    dp.register_message_handler(delite_note, commands=["del", "delite_note"])
    dp.register_message_handler(all_notes, commands=["all"])