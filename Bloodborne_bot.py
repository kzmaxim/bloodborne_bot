from aiogram import types, Dispatcher, Bot, executor
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

TOKEN_API = "TOKEN"
bot = Bot(TOKEN_API)
dp = Dispatcher(bot)
HELP_COMMAND = '''
<b>/help</b> - <em>список всех комманд</em>
<b>/start</b> - <em>старт бота</em>
<b>/link</b> - <em>ссылка на вики или на форум по ББ</em>
<b>/builds_opinion</b> - <em>проголосовать за лучший билд</em>
'''
blood_description = '''
Билд через Оттенок Крови:

Начальный класс: благородный
Оружие: Чикаге(основное оружие), Кровопускатель, для левой руки - Эвелина
Ловкость - 25, Здоровье - 30-50, Стамина - 30, остальное в оттенок
'''
arcane_description = '''
Билд через Тайну:

Начальный класс: жестокая судьба
Оружие: Меч священного лунного света, Клинок Людвига(со вставленными самоцветами на стихию),
Тонитрус
Здоровье - 30-50, Стамина - 40, Сила - 16, Ловкость - 10, остальное в Тайну
'''
strength_description = '''
Билд через Силу:

Начальный класс: жестокое прошлое
Оружие: Клинок Людвига, Секира Охотника, Молот-меч, Пила-вертушка
Здоровье - 30-50, Стамина - 40, Ловкость - 15, остальное в Силу
'''
weapons = '''
1.Меч Священного Лунного Света
2.Меч Людвига
3.Чикаге
4.Пила-вертушка
5.Тонитрус
'''
bosses = '''
1.Сирота Коса
2.Первый Викарий Лоренс
3.Людвиг
4.Ибраитас
5.Викарий Амелия
'''

start_kb = ReplyKeyboardMarkup(resize_keyboard=True)
start_b1 = KeyboardButton('/best_builds')
start_b2 = KeyboardButton('/best_weapons')
start_b3 = KeyboardButton('/difficult_bosses')
start_b4 = KeyboardButton('/builds_opinion')
start_b5 = KeyboardButton('/link')
start_kb.add(start_b1, start_b2, start_b3).add(start_b4, start_b5)


async def on_startup(_):
    print('Старт бота...')


@dp.message_handler(commands=['start']) # Запуск бота, также запускается клавиатура
async def start_command(message: types.Message):
    await bot.send_message(
        chat_id=message.from_user.id,
        text='Бот запустился!',
        reply_markup=start_kb
    )


@dp.message_handler(commands=['help'])  # Список всех комманд бота
async def help_command(message: types.Message):
    await bot.send_message(
        chat_id=message.from_user.id,
        text=HELP_COMMAND,
        reply_markup=ReplyKeyboardRemove(),
        parse_mode='HTML'
    )


@dp.message_handler(commands=['link'])  # Получить ссылку на фандом и вики по Бладборну с inline-клавиатуры 
async def link_command(message: types.Message):
    link_ikb = InlineKeyboardMarkup(row_width=2)
    link_ib1 = InlineKeyboardButton(
        'stratege.ru',
        url='https://www.stratege.ru/forums/forumdisplay.php?f=157'
    )
    link_ib2 = InlineKeyboardButton(
        'Bloodborne Wiki',
        url='https://bloodborne.fandom.com/ru/wiki/Bloodborne_%D0%B2%D0%B8%D0%BA%D0%B8'
    )
    link_ikb.add(link_ib1, link_ib2)
    await bot.send_photo(
        chat_id=message.from_user.id,
        photo='https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse4.mm.bing.net%2Fth%3Fid%3DOIP._MJInPD2WPL0lYj7SkSphgHaEK%26pid%3DApi&f=1&ipt=b8d0ed5862b6ef8dfb8e5ccafba69fc137275025ff96bfaba3feda5a9f6ab67f&ipo=images',
        reply_markup=link_ikb
    )


@dp.message_handler(commands=['builds_opinion'])    # Голосование за лучший билд
async def opinion_command(message: types.Message):
    opinion_ikb = InlineKeyboardMarkup(row_width=2)
    opinion_ib1 = InlineKeyboardButton(
        'Кровавый',
        callback_data='кровавый'
    )
    opinion_ib2 = InlineKeyboardButton(
        'Тайный',
        callback_data='тайный'
    )
    opinion_ib3 = InlineKeyboardButton(
        'Силовой',
        callback_data='силовой'
    )
    opinion_ib4 = InlineKeyboardButton(
        'Ловкий',
        callback_data='ловкий'
    )
    opinion_ikb.add(opinion_ib1, opinion_ib2).add(opinion_ib3, opinion_ib4)
    await bot.send_photo(
        chat_id=message.from_user.id,
        photo='https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse3.mm.bing.net%2Fth%3Fid%3DOIP.R7WhTVw3BqiuhQQPa-CxnQHaDt%26pid%3DApi&f=1&ipt=98af4e80a2ff30c0ab4d2c170c8c02e26b344e7296e273efe261080dc5e05a4a&ipo=images',
        caption='Какой билд тебе больше всего нравится?',
        reply_markup=opinion_ikb
    )


@dp.callback_query_handler()
async def opinion_callback(callback: types.CallbackQuery):
    if callback.data == 'кровавый':
        await callback.answer('Вы выбрали Кровавый')
    elif callback.data == 'тайный':
        await callback.answer('Вы выбрали Тайный')
    elif callback.data == 'силовой':
        await callback.answer('Вы выбрали Силовой')
    elif callback.data == 'ловкий':
        await callback.answer('Вы выбрали Ловкий')


@dp.message_handler(commands=['best_builds'])   # Список лучших билдов, запускается клавиатура со список билдов
async def bb_command(message: types.Message):
    bb_kb = ReplyKeyboardMarkup(resize_keyboard=True)
    bb_b1 = KeyboardButton('/blood')
    bb_b2 = KeyboardButton('/arcane')
    bb_b3 = KeyboardButton('/strength')
    bb_kb.add(bb_b1, bb_b2, bb_b3)

    await bot.send_message(
        chat_id=message.from_user.id,
        text='''
        Лучшие билды:
        Кровавый(blood), Тайный(arcane) и Силовой(strength)
        ''',
        reply_markup=bb_kb
    )


@dp.message_handler(commands=['blood']) # Описание билда через кровь
async def blood_command(message: types.Message):
    await bot.send_photo(
        chat_id=message.from_user.id,
        photo='https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse4.mm.bing.net%2Fth%3Fid%3DOIP.HFWBTNjeRHvRU_B1bTf55AHaEK%26pid%3DApi&f=1&ipt=9a4120c50aae86fc120ded722e4cebf178618cfc612c0d45781bc41c7525852c&ipo=images',
        caption=blood_description,
        reply_markup=ReplyKeyboardRemove()
    )


@dp.message_handler(commands=['arcane']) # Описание билда через тайну
async def arcane_command(message: types.Message):
    await bot.send_photo(
        chat_id=message.from_user.id,
        photo='https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse1.mm.bing.net%2Fth%3Fid%3DOIP.kYn_2ZF5mjX5A_Y4VnABpQHaEK%26pid%3DApi&f=1&ipt=6ee8195766f8835b2d8c1c1c78657cc42dbe6e82da64971363b01ae4f727ef1e&ipo=images',
        caption=arcane_description,
        reply_markup=ReplyKeyboardRemove()
    )


@dp.message_handler(commands=['strength']) # Описание билда через силу
async def strength_command(message: types.Message):
    await bot.send_photo(
        chat_id=message.from_user.id,
        photo='https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse4.mm.bing.net%2Fth%3Fid%3DOIP.cmMg4roZ5wae_EPEJANbTgHaEK%26pid%3DApi&f=1&ipt=fca49ee39df77eb9c587a7501363e36b166ad4d52862608517a8fb62bcacdbe0&ipo=images',
        caption=strength_description,
        reply_markup=ReplyKeyboardRemove()
    )


@dp.message_handler(commands=['best_weapons'])  # список лучшего оружия
async def weapon_command(message: types.Message):
    await bot.send_message(
        chat_id=message.from_user.id,
        text=weapons
    )


@dp.message_handler(commands=['difficult_bosses'])  # список сложнейших боссов
async def bosses_command(message: types.Message):
    await bot.send_message(
        chat_id=message.from_user.id,
        text=bosses
    )





if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup,skip_updates=True)

