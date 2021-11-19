import sqlite3 as sq
from create_veganbot import bot

def sql_start3():
    global base, cur
    base = sq.connect('cooking_veg.db')
    cur = base.cursor()
    if base:
        print('Data base connected OK!')
    base.execute('CREATE TABLE IF NOT EXISTS supper(img TEXT, name TEXT PRIMARY KEY,description TEXT, price TEXT)')
    base.commit()


async def sql_add_command(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO supper VALUES(?,?,?,?)', tuple(data.values()))
        base.commit()

async def sql_read_veg3(message):
    for ret in cur.execute('SELECT * FROM supper').fetchall():
        await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\nИнгредиенты: {ret[2]}\nРецепт {ret[-1]}')

async def sql_read2():
    return cur.execute('SELECT * FROM supper').fetchall()

async def sql_delete_command(data):
    cur.execute('DELETE FROM  supper WHERE name == ?', (data,))
    base.commit()