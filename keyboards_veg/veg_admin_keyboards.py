from aiogram.types import KeyboardButton, ReplyKeyboardMarkup



button_load1 = KeyboardButton('/Загрузить в завтраки ')
button_load2 = KeyboardButton('/Загрузить в обеды ')
button_load3 = KeyboardButton('/Загрузить в ужины ')
button_load4 = KeyboardButton('/Загрузить в к чаю ')
button_delete = KeyboardButton('/Удалить')
button_l = ReplyKeyboardMarkup(resize_keyboard=True)
button_l2 = ReplyKeyboardMarkup(resize_keyboard=True)
button_l3 = ReplyKeyboardMarkup(resize_keyboard=True)
button_l4 = ReplyKeyboardMarkup(resize_keyboard=True)

button_l.row(button_load1).add(button_delete)
button_l2.row(button_load2).add(button_delete)
button_l3.row(button_load3).add(button_delete)
button_l4.row(button_load4).add(button_delete)
#button_case_admin = ReplyKeyboardMarkup(resize_keyboard=True).add(button_load)\
    #.add(button_delete)
