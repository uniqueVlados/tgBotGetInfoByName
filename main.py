from database import User1, User2
from database import engine
from sqlalchemy import select
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

TOKEN = "5238823708:AAE5zOMs8rxMkzn2H4CGsf-9azVlVO04evg"

BUTTON_INPUT = KeyboardButton('ВВЕСТИ ФИО')
BUTTON_EXIT = KeyboardButton('ВЫХОД')
KB = ReplyKeyboardMarkup(resize_keyboard=True)
STATES = {"start": True, "input": False}


def get_id(msg):
    conn = engine.connect()
    id = select([User1.id]). \
        where(
        User1.name == msg,
    )
    return conn.execute(id).fetchall()


def get_info1(msg):
    conn = engine.connect()
    a = []
    for i in get_id(msg):
        info1 = select([User1]). \
            where(
            User1.id == i[0]
        )
        a.append(conn.execute(info1).fetchall())
    c = []
    for i in a:
        c.extend(i)
    return c


def get_info2(msg):
    conn = engine.connect()
    a = []
    for i in get_id(msg):
        info2 = select([User2]). \
            where(
            User2.id == i[0]
        )
        a.append(conn.execute(info2).fetchall())
    c = []
    for i in a:
        c.extend(i)
    return c


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

KB.add(BUTTON_INPUT)
KB.add(BUTTON_EXIT)


def is_correct_name(name):
    name_list = name.split()
    if len(name_list) == 3:
        for i in range(3):
            if not name_list[i].capitalize():
                return False
        return True
    return False


@dp.message_handler(commands=['start'])
async def start_(message: types.Message):
    await message.reply("Приветсвую!\nЗдесь Вы можешь получить данные о добавленных пользователях.", reply_markup=KB)


@dp.message_handler()
async def info(message: types.Message):
    if message.text == "ВЫХОД":
        await message.reply("Ждём снова.\nДля начала работы введите команду /start")
    elif message.text == "ВВЕСТИ ФИО":
        STATES["input"] = True
        await message.reply("Жду данные!")
    elif is_correct_name(message.text) and STATES["input"]:
        STATES[input] = False
        user_info1 = get_info1(message.text)
        user_info2 = get_info2(message.text)
        t1 = [".", "ФИО", "Телнфон", "Почта"]
        t2 = [".", "Программа обучения", "Номер потока", "Начало", "Конец", "Статус"]
        for i in range(1, len(user_info1[0])):
            await message.reply(f"{t1[i]} - {user_info1[0][i]}")
        for i in range(1, len(user_info2[0])):
            await message.reply(f"{t2[i]} - {user_info2[0][i]}")


if __name__ == '__main__':
    executor.start_polling(dp)
