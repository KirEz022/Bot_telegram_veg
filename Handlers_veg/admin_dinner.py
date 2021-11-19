from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher
from create_veganbot import dp, bot
from aiogram.dispatcher.filters import Text
from data_base_veg import sqlite_dinner
from keyboards_veg import veg_admin_keyboards
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

ID = None
class FSMAdmin(StatesGroup):
    photo = State()
    title = State()
    ingredients = State()
    recipe = State()



# @dp.message_handler(commands=['Модератор'],is_chat_admin= True)
async def make_changes_command2(message: types.Message):
    global ID
    ID = message.from_user.id
    await bot.send_message(message.from_user.id,'Бот к Вашим услугам', reply_markup=veg_admin_keyboards.button_l2)
    await message.delete()



#@dp.message_handler(commands='Загрузить',State=None)
async def cm_start2(message: types.Message):
    await FSMAdmin.photo.set()
    await message.reply('Загрузите фото')

#Ловим первый ответ от пользователя и пишем в словарь
# @dp.message_handler(content_types=['photo'], state=FSMAdmin.photo)
async def load_photo2(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[0].file_id
    if message.from_user.id == ID:
        await FSMAdmin.next()
        await message.reply("Введите название")

#Ловим второй ответ
#@dp.message_handler(state=FSMAdmin.name)
async def load_title2(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['title'] = message.text
    if message.from_user.id == ID:
        await FSMAdmin.next()
        await message.reply('Введите ингредиенты ')

#Ловим третий ответ
#@dp.message_handler(state=FSMAdmin.description)
async def load_ingredients2(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data[' ingredients '] = message.text
    if message.from_user.id == ID:
        await FSMAdmin.next()
        await message.reply('Введите рецепт')

#Получаем последние ответ и используем полученные данные
#@dp.message_handler(state=FSMAdmin.price)
async def load_recipe2(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['recipe'] = message.text
        await sqlite_dinner.sql_add_command2(state)
        await state.finish()

#выход из состояний
#@dp.message_handler(state="*", commands='Отмена')
#@dp.message_handler(Text(equals='Отмена', ignore_case=True), state="*")
async def cancel_handler2(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.reply('OK')

@dp.callback_query_handler(lambda x: x.data and x.data.startswith('del '))
async def del_callback_run(callback_query: types.CallbackQuery):
    await sqlite_dinner.sql_delete_command(callback_query.data.replace('del ', ''))
    await callback_query.answer(text=f'{callback_query.data.replace("del ", "")} удалена.', show_alert=True)

@dp.message_handler(commands='Удалить')
async def delete_item(message: types.Message):
    if message.from_user.id == ID:
        read = await sqlite_dinner.sql_read2()
        for ret in read:
            await bot.send_photo(message.from_user.id, ret [0], f'{ret[1]}\nИнгредиенты: {ret[2]}\nРецепт {ret[-1]}')
            await bot.send_message(message.from_user.id, text='^^^', reply_markup=InlineKeyboardMarkup().\
            add(InlineKeyboardButton(f'Удалить {ret[1]}', callback_data=f'del {ret[1]}')))

#Регистрируем хенделеры
def register_handlers_admin2(dp: Dispatcher):
    dp.register_message_handler(cm_start2, commands=['Загрузить в обеды'], state=None)
    dp.register_message_handler(load_photo2, content_types=['photo'], state=FSMAdmin.photo)
    dp.register_message_handler(load_title2, state=FSMAdmin.title)
    dp.register_message_handler(load_ingredients2, state=FSMAdmin.ingredients)
    dp.register_message_handler(load_recipe2, state=FSMAdmin.recipe)
    dp.register_message_handler(cancel_handler2, state="*", commands='Отмена')
    dp.register_message_handler(cancel_handler2, Text(equals='Отмена', ignore_case=True), state="*")
    dp.register_message_handler(make_changes_command2, commands=['Модератор2'], is_chat_admin=True)
