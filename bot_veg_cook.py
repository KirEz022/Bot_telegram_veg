from aiogram.utils import executor
from create_veganbot import dp
from data_base_veg import sqlite_breakfast
from data_base_veg import sqlite_dinner
from data_base_veg import sqlite_supper
from data_base_veg import sqlite_dessert




async def on_startup(_):
    print('Бот вышел в онлайн')
    sqlite_breakfast.sql_start()
    sqlite_dinner.sql_start2()
    sqlite_supper.sql_start3()
    sqlite_dessert.sql_start4()


from Handlers_veg import client_veg, admin_breakfast, admin_dinner, admin_supper,admin_dessert

client_veg.register_handlers_client(dp)
admin_breakfast.register_handlers_admin(dp)
admin_dinner.register_handlers_admin2(dp)
admin_supper.register_handlers_admin(dp)
admin_dessert.register_handlers_admin(dp)

executor.start_polling(dp, skip_updates=True, on_startup=on_startup)