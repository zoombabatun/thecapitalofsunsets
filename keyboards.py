from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData


cb = CallbackData("show_kb", "kb", "btn_name")


# -- Главная клавиатура --------------------------------------------------------------------------------------------------------
main_kb = InlineKeyboardMarkup(row_width = 1)

main_kb_captions = ['Категории', 'Обратная связь']
main_kb_cb = ['categories', 'feedback']

for i in range(len(main_kb_captions)):
    main_kb_buttons = InlineKeyboardButton(main_kb_captions[i], callback_data=cb.new(kb="main_kb", btn_name = main_kb_cb[i]))
    main_kb.insert(main_kb_buttons)
# ------------------------------------------------------------------------------------------------------------------------------

# -- Категории --------------------------------------------------------------------------------------------------------------
categories_kb = InlineKeyboardMarkup(row_width = 1)

categories_kb_captions = ['Новые места', 'Поработать с ноутбуком', 'Устроить свидание', 'Навести красоту', 'Поехать загород', 'Провести время с друзьями', 'Фильмы сегодня', 'Поесть']
categories_kb_cb = ['new', 'work_laptop', 'date', 'beautiful', 'countryside', 'friends', 'films today', 'food']

for i in range(len(categories_kb_captions)):
    categories_kb_buttons = InlineKeyboardButton(categories_kb_captions[i], callback_data=cb.new(kb="categories_kb", btn_name = categories_kb_cb[i]))
    categories_kb.insert(categories_kb_buttons)
# ------------------------------------------------------------------------------------------------------------------------------



# -- Кнопки для возврата -------------------------------------------------------------------------------------------------------
return_kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width = 2)

step_back_button = KeyboardButton("Назад")
goto_beg_button = KeyboardButton("Вернуться в начало")

return_kb.insert(step_back_button).insert(goto_beg_button)
# ------------------------------------------------------------------------------------------------------------------------------



