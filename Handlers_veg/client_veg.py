from aiogram import types, Dispatcher
from create_veganbot import dp, bot
from keyboards_veg import kb_client_veg
from data_base_veg import sqlite_breakfast
from data_base_veg import sqlite_dinner
from data_base_veg import sqlite_supper
from data_base_veg import sqlite_dessert


#@dp.message_handler(commands=['start',])
async def command_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Выберете нужный пункт в меню 👇', reply_markup=kb_client_veg)
        await message.delete()
    except:
        await message.reply('Общение с ботом через Лс, напише ему:\nhttps://t.me./Vegan_Cooking_bot')

#@dp.message_handler(commands=['Завтрак'])
async def veg_breakfast_command(message: types.Message):
    await sqlite_breakfast.sql_read_veg(message)


#@dp.message_handler(commands=['Обед'])
async def veg_dinner_command(message: types.Message):
    await sqlite_dinner.sql_read_veg2(message)


#@dp.message_handler(commands='Ужин')
async def veg_supper_command(message: types.Message):
    await sqlite_supper.sql_read_veg3(message)


#@dp.message_handler(commands='Что-то к чаю')
async def veg_dessert_command(message: types.Message):
    await sqlite_dessert.sql_read_veg4(message)




def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start'])
    dp.register_message_handler(veg_breakfast_command, commands=['Завтрак'])
    dp.register_message_handler(veg_dinner_command, commands=['Обед'])
    dp.register_message_handler(veg_supper_command,commands=['Ужин'])
    dp.register_message_handler(veg_dessert_command, commands=['Что-то к чаю'])