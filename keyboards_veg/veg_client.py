from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

b1 = KeyboardButton('/Завтрак')
b2 = KeyboardButton('/Обед')
b3 = KeyboardButton('/Ужин')
b4 = KeyboardButton('/Что-то к чаю')

kb_client_veg = ReplyKeyboardMarkup(resize_keyboard=True)

kb_client_veg.row(b1, b2, b3, b4)