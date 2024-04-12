import random
import sqlite3

from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext


from config import TG_TOKEN
import keyboards as kb
import data as data
import afisha
import datetime
# Объект бота
bot = Bot(TG_TOKEN)
# Диспетчер для бота
dp = Dispatcher(bot,storage=MemoryStorage())

current_time = datetime.datetime.now()
month, day = current_time.month, current_time.day
films,links,descript = afisha.getFilmsByDate(str(month), day)
# ------------------------------------------------------------------------------------------------------------------------------
# обработка команды /start
@dp.message_handler(commands=['start'])
async def process_command_start(message: types.Message):
    await message.answer(data.greeting_text, parse_mode="html", reply_markup=kb.return_kb)
    await message.answer("Выбери интересующий пункт:", reply_markup=kb.main_kb)
# ------------------------------------------------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------------------------------------------------
# отлавливаем по встроенному фильтру нажатие на кнопку первой клавиатуры, используя фильтр
@dp.callback_query_handler(kb.cb.filter(kb="main_kb"))
async def process_main_kb(call: types.CallbackQuery, callback_data: dict, state: FSMContext):
    await call.answer(cache_time=60)
    
    btn_name = callback_data.get("btn_name")
    await state.update_data(kb=callback_data.get("kb"))

    # нажата кнопка Категории
    if btn_name == kb.main_kb_cb[0]:
        await call.message.edit_reply_markup(reply_markup = kb.categories_kb)

    # нажата кнопка Обратная связь
    elif btn_name == kb.main_kb_cb[1]:
        await call.message.answer(data.feedback_text, parse_mode="html")

    # ошибка
    else:
        await call.message.answer("Неизвестная команда. Попробуйте еще раз.")
        await call.message.answer("Выбери интересующий пункт:", reply_markup=kb.main_kb)   
# ------------------------------------------------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------------------------------------------------
# отлавливаем по встроенному фильтру нажатие на кнопку клавиатуры Категориии, используя фильтр
@dp.callback_query_handler(kb.cb.filter(kb="categories_kb"))
async def process_main_kb(call: types.CallbackQuery, callback_data: dict, state: FSMContext):
    await call.answer(cache_time=60)
    btn_name = callback_data.get("btn_name")
    await state.update_data(kb=callback_data.get("kb"))

    # нажата кнопка Новые места
    if btn_name == kb.categories_kb_cb[0]:
        
        await bot.send_photo(chat_id=call.message.chat.id, photo=data.meteor_photo)
        await call.message.answer(data.meteor_text, parse_mode="html")

        await bot.send_photo(chat_id=call.message.chat.id, photo=data.a_sad_photo)
        await call.message.answer(data.a_sad_text, parse_mode="html")

        await bot.send_photo(chat_id=call.message.chat.id, photo=data.fabula_photo)
        await call.message.answer(data.fabula_text, parse_mode="html")

        await bot.send_photo(chat_id=call.message.chat.id, photo=data.laboratory_photo)
        await call.message.answer(data.laboratory_text, parse_mode="html")

        await bot.send_photo(chat_id=call.message.chat.id, photo=data.pasters_photo)
        await call.message.answer(data.pasters_text, parse_mode="html")

    # нажата кнопка Поработать с ноутбуком
    elif btn_name == kb.categories_kb_cb[1]:
        
        await bot.send_photo(chat_id=call.message.chat.id, photo=data.vysota_photo)
        await call.message.answer(data.vysota_text, parse_mode="html")

        await bot.send_photo(chat_id=call.message.chat.id, photo=data.record_photo)
        await call.message.answer(data.record_text, parse_mode="html")

        await bot.send_photo(chat_id=call.message.chat.id, photo=data.dom_archi_photo)
        await call.message.answer(data.dom_archi_text, parse_mode="html")

        await bot.send_photo(chat_id=call.message.chat.id, photo=data.young_photo)
        await call.message.answer(data.young_text, parse_mode="html")

        await bot.send_photo(chat_id=call.message.chat.id, photo=data.planetarium1_photo)
        await call.message.answer(data.planetarium1_text, parse_mode="html")
        
        await bot.send_photo(chat_id=call.message.chat.id, photo=data.garage_photo)
        await call.message.answer(data.garage_text, parse_mode="html")

    # нажата кнопка Устроить свидание
    elif btn_name == kb.categories_kb_cb[2]:
        
        await bot.send_photo(chat_id=call.message.chat.id, photo=data.tramway_photo)
        await call.message.answer(data.tramway_text, parse_mode="html")

        await bot.send_photo(chat_id=call.message.chat.id, photo=data.river_walks_photo)
        await call.message.answer(data.river_walks_text, parse_mode="html")

        await bot.send_photo(chat_id=call.message.chat.id, photo=data.planetarium_photo)
        await call.message.answer(data.planetarium_text, parse_mode="html")

        await bot.send_photo(chat_id=call.message.chat.id, photo=data.roof_photo)
        await call.message.answer(data.roof_text, parse_mode="html")

        await bot.send_photo(chat_id=call.message.chat.id, photo=data.sea_photo)
        await call.message.answer(data.sea_text, parse_mode="html")
        
        await bot.send_photo(chat_id=call.message.chat.id, photo=data.igloo_photo)
        await call.message.answer(data.igloo_text, parse_mode="html")


    # нажата кнопка Навести красоту
    elif btn_name == kb.categories_kb_cb[3]:

        await bot.send_photo(chat_id=call.message.chat.id, photo=data.legrand_photo)
        await call.message.answer(data.legrand_text, parse_mode="html")

        await bot.send_photo(chat_id=call.message.chat.id, photo=data.lelu_photo)
        await call.message.answer(data.lelu_text, parse_mode="html")

        await bot.send_photo(chat_id=call.message.chat.id, photo=data.blackq_photo)
        await call.message.answer(data.blackq_text, parse_mode="html")

        await bot.send_photo(chat_id=call.message.chat.id, photo=data.slivki_photo)
        await call.message.answer(data.slivki_text, parse_mode="html")

        await bot.send_photo(chat_id=call.message.chat.id, photo=data.versal_photo)
        await call.message.answer(data.versal_text, parse_mode="html")
        
        await bot.send_photo(chat_id=call.message.chat.id, photo=data.greenspa_photo)
        await call.message.answer(data.greenspa_text, parse_mode="html")
 

    # нажата кнопка Поехать загород
    elif btn_name == kb.categories_kb_cb[4]:

        await bot.send_photo(chat_id=call.message.chat.id, photo=data.mys_photo)
        await call.message.answer(data.mys_text, parse_mode="html")

        await bot.send_photo(chat_id=call.message.chat.id, photo=data.gore_more_photo)
        await call.message.answer(data.gore_more_text, parse_mode="html")

        await bot.send_photo(chat_id=call.message.chat.id, photo=data.chan_photo)
        await call.message.answer(data.chan_text, parse_mode="html")

        await bot.send_photo(chat_id=call.message.chat.id, photo=data.aframe_photo)
        await call.message.answer(data.aframe_text, parse_mode="html")

        await bot.send_photo(chat_id=call.message.chat.id, photo=data.beach_photo)
        await call.message.answer(data.beach_text, parse_mode="html")
        
        await bot.send_photo(chat_id=call.message.chat.id, photo=data.filingrif_photo)
        await call.message.answer(data.filingrif_text, parse_mode="html")

        await bot.send_photo(chat_id=call.message.chat.id, photo=data.extream_photo)
        await call.message.answer(data.extream_text, parse_mode="html")
 

    # нажата кнопка Провести время с друзьями
    elif btn_name == kb.categories_kb_cb[5]:

        await bot.send_photo(chat_id=call.message.chat.id, photo=data.palitra_photo)
        await call.message.answer(data.palitra_text, parse_mode="html")

        await bot.send_photo(chat_id=call.message.chat.id, photo=data.qzar_photo)
        await call.message.answer(data.qzar_text, parse_mode="html")

        await bot.send_photo(chat_id=call.message.chat.id, photo=data.kvest_photo)
        await call.message.answer(data.kvest_text, parse_mode="html")

        await bot.send_photo(chat_id=call.message.chat.id, photo=data.omega_photo)
        await call.message.answer(data.omega_text, parse_mode="html")

        await bot.send_photo(chat_id=call.message.chat.id, photo=data.olymp_photo)
        await call.message.answer(data.olymp_text, parse_mode="html")
        
        await bot.send_photo(chat_id=call.message.chat.id, photo=data.capitalclub_photo)
        await call.message.answer(data.capitalclub_text, parse_mode="html")

    # нажата кнопка фильмы сегодня
    elif btn_name == kb.categories_kb_cb[6]:

        for i in range(0,5):
            rand_idx = random.randrange(len(films))
            await call.message.answer(f"<b>{films[rand_idx]}</b> \n {descript[rand_idx]} \n\n Ссылка на покупку: https://www.afisha.ru{links[rand_idx]}", parse_mode="html")

    # нажата кнопка поесть
    elif btn_name == kb.categories_kb_cb[7]:
        connection = sqlite3.connect('my_database.db')
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM Rests')

        rests = cursor.fetchall()
        rests_list = []
        for rest in rests:
            user_dict = {
                'name': rest[0],
                'phone': rest[1],
                'address': rest[2]

            }
            rests_list.append(user_dict)
        print(rests_list)
        for i in range(0,5):
            rand_idx = random.randrange(len(rests_list))
            #print(f"<b>{rests_list[rand_idx]['name']}</b> \n {rests_list[rand_idx]['phone']} \n\n {rests_list[rand_idx]['address']}")
            await call.message.answer(f"<b>{rests_list[rand_idx]['name']}</b> \n {rests_list[rand_idx]['phone']} \n\n {rests_list[rand_idx]['address']}", parse_mode="html")
        connection.close()
    # ошибка
    else:
        await call.message.answer("Неизвестная команда. Попробуйте еще раз.")
        await call.message.answer("Выбери интересующий пункт:", reply_markup=kb.main_kb)   
# ------------------------------------------------------------------------------------------------------------------------------


# ------------------------------------------------------------------------------------------------------------------------------
# обработка нажатия кнопок "Назад", "Вернуться в начало" или другого текста
@dp.message_handler()
async def process_message(message: types.Message, state: FSMContext):
    # кнопка "Вернуться в начало"
    if (message.text == kb.goto_beg_button.text):
        await message.answer("Выберите интересующий Вас пункт:", reply_markup=kb.main_kb)
        await state.finish()

    # кнопка "Назад"
    elif (message.text == kb.step_back_button.text):
        async with state.proxy() as current_state:
            try:
                current_kb = current_state['kb']

                if current_kb == "categories_kb":
                    await message.answer("Выбери интересующий пункт:", reply_markup=kb.categories_kb)
                    await state.finish()

                if current_kb == "main_kb":
                    await message.answer("Выбери интересующий пункт:", reply_markup=kb.main_kb)
                    await state.finish()
            except:
                await message.answer("Выбери интересующий пункт:", reply_markup=kb.main_kb)

    # обработка текста от пользователя
    else:
        await message.reply("Неизвестная команда.")
# ------------------------------------------------------------------------------------------------------------------------------


if __name__ == "__main__":
    # Запуск бота
    executor.start_polling(dp, skip_updates=True)

