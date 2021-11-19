import sqlite3 as sq
from create_veganbot import bot

def sql_start4():
    global base, cur
    base = sq.connect('cooking_veg.db')
    cur = base.cursor()
    if base:
        print('Data base connected OK!')
    base.execute('CREATE TABLE IF NOT EXISTS dessert(img TEXT, name TEXT PRIMARY KEY,description TEXT, price TEXT)')
    base.commit()


async def sql_add_command(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO dessert VALUES(?,?,?,?)', tuple(data.values()))
        base.commit()

async def sql_read_veg4(message):
    for ret in cur.execute('SELECT * FROM dessert').fetchall():
        await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\nИнгредиенты: {ret[2]}\nРецепт {ret[-1]}')

async def sql_read2():
    return cur.execute('SELECT * FROM dessert').fetchall()

async def sql_delete_command(data):
    cur.execute('DELETE FROM  dessert WHERE name == ?', (data,))
    base.commit()