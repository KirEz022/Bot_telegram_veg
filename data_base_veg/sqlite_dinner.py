import sqlite3 as sq
from create_veganbot import bot

def sql_start2():
    global base, cur
    base = sq.connect('cooking_veg.db')
    cur = base.cursor()
    base.execute('CREATE TABLE IF NOT EXISTS dinner(img_d TEXT, name_d TEXT PRIMARY KEY,description_d TEXT, price_d TEXT)')
    base.commit()


async def sql_add_command2(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO dinner VALUES(?,?,?,?)', tuple(data.values()))
        base.commit()

async def sql_read_veg2(message):
    for rets in cur.execute('SELECT * FROM dinner').fetchall():
        await bot.send_photo(message.from_user.id, rets[0], f'{rets[1]}\nИнгредиенты: {rets[2]}\nРецепт {rets[-1]}')

async def sql_read02():
    return cur.execute('SELECT * FROM dinner').fetchall()

async def sql_delete_command2(data):
    cur.execute('DELETE FROM  dinner WHERE name == ?', (data,))
    base.commit()