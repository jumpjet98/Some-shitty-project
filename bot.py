import telebot
import config
from config import *
import dbworker
import random
from telebot import types

bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=['start'])
def cmd_start(message):#Заменен текстовый блок на текстовую переменную
    keyboard = types.ReplyKeyboardMarkup(row_width=2)
    keyboard.add(*[types.KeyboardButton(i) for i in ['Вода', 'Газ', 'Свет', 'Другое']])
    msg = bot.send_message(message.chat.id, greetings_message,#замена
                                            reply_markup=keyboard, parse_mode='Markdown')
    bot.register_next_step_handler(msg, name)
    # print(message)


def name(message):
    if message.text == 'Вода':
        dbworker.set_state(message.chat.id, config.States.WATER.value)
    elif message.text == 'Газ':
        dbworker.set_state(message.chat.id, config.States.GAS.value)
    elif message.text == 'Свет':
        dbworker.set_state(message.chat.id, config.States.ELECTR.value)
    elif message.text == 'Другое':
        dbworker.set_state(message.chat.id, config.States.OTHER.value)
    # print(message)


# Algorithm for WATER STARTs


@bot.message_handler(func=lambda message: dbworker.get_current_state(message.chat.id) == config.States.WATER.value)
def water_choice(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*[types.KeyboardButton(i) for i in ['Оплата', 'Тарифы', 'Проблемы']])
    msg = bot.send_message(message.chat.id, "Пожалуйста, выберите разделы водоснабжения", reply_markup=keyboard)
    bot.register_next_step_handler(msg, water_options)


def water_options(message):
    if message.text == 'Оплата':
        dbworker.set_state(message.chat.id, config.States.PAY.value)

    elif message.text == 'Тарифы':
        delete = types.ReplyKeyboardRemove()
        bot.send_message(message.chat.id, text='Действующие тарифы на водоснабжение:', reply_markup=delete)
        bot.send_photo(message.chat.id, photo=open('cost_w.jpg', 'rb'))## Картинка с ценниками по ВОДЕ и прочей шляпе
        bot.send_message(message.chat.id, text='Для перехода в меню, введите _/start_', parse_mode='Markdown')
        dbworker.set_state(message.chat.id, config.States.MENU.value)

    elif message.text == 'Проблемы':
        dbworker.set_state(message.chat.id, config.States.PROBLEM_W.value)


@bot.message_handler(func=lambda message: dbworker.get_current_state(message.chat.id) == config.States.PROBLEM_W.value)
def water_problems(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    keyboard.add(*[types.KeyboardButton(i) for i in ['Трубу прорвало', 'Нет воды',
                                                     'Нет горячей воды', 'Другое']])
    msg = bot.send_message(message.chat.id, "Пожалуйста, выберите Вашу проблему", reply_markup=keyboard)
    bot.register_next_step_handler(msg, water_problems_options)


def water_problems_options(message):#По вопросам ВОДЫ Здесь заменены 2 блока текста на текстовые переменные чтобы было легче подгонять под необходимые районы 
    delete = types.ReplyKeyboardRemove()
    if message.text == 'Трубу прорвало' or message.text == 'Нет воды':
        bot.send_message(message.chat.id, water_problems_settings0, reply_markup=delete,#замена
                         parse_mode='Markdown')

    elif message.text == 'Нет горячей воды' or message.text == 'Другое':
        bot.send_message(message.chat.id, water_problems_settings1, reply_markup=delete,#замена
                         parse_mode='Markdown')
    dbworker.set_state(message.chat.id, config.States.MENU.value)


# Algorithm for WATER ENDs


# Algorithm for LIGHT STARTs
@bot.message_handler(func=lambda message: dbworker.get_current_state(message.chat.id) == config.States.ELECTR.value)
def light_choice(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*[types.KeyboardButton(i) for i in ['Оплата', 'Тарифы', 'Проблемы']])
    msg = bot.send_message(message.chat.id, "Пожалуйста, выберите разделы электроснабжения", reply_markup=keyboard)
    bot.register_next_step_handler(msg, water_options)


def light_options(message):
    if message.text == 'Оплата':
        dbworker.set_state(message.chat.id, config.States.PAY.value)
    elif message.text == 'Тарифы':
        delete = types.ReplyKeyboardRemove(selective=False)
        bot.send_message(message.chat.id, "Действующие тарифы на электроснабжение:")
        bot.send_photo(message.chat.id, photo=open('cost_e.jpg', 'rb'))# Картинка с ценниками по свету и прочей шляпе
        bot.send_message(message.chat.id, "Для возврата в главное меню введите _/start_", reply_markup=delete,
                         parse_mode='Markdown')
        dbworker.set_state(message.chat.id, config.States.MENU.value)
    elif message.text == 'Проблемы':
        dbworker.set_state(message.chat.id, config.States.PROBLEM_E.value)


@bot.message_handler(func=lambda message: dbworker.get_current_state(message.chat.id) == config.States.PROBLEM_E.value)
def light_problems(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    keyboard.add(*[types.KeyboardButton(i) for i in ['Нет света', 'Повреждена проводка', 'Другое']])
    msg = bot.send_message(message.chat.id, "Пожалуйста, выберите Вашу проблему", reply_markup=keyboard)
    bot.register_next_step_handler(msg, light_problems_options)


def light_problems_options(message):#По вопросам СВЕТА Здесь заменены 2 блока текста на текстовые переменные чтобы было легче подгонять под необходимые районы 
    if message.text == 'Нет света' or message.text == 'Другое':
        delete = types.ReplyKeyboardRemove(selective=False)
        bot.send_message(message.chat.id, light_problems_setting0,#замена
                         reply_markup=delete, parse_mode='Markdown')
        # dbworker.set_state(message.chat.id, config.States.MENU.value)
    elif message.text == 'Повреждена проводка':
        delete = types.ReplyKeyboardRemove(selective=False)
        bot.send_message(message.chat.id, light_problems_setting1,#замена
                         reply_markup=delete, parse_mode='Markdown')
    dbworker.set_state(message.chat.id, config.States.MENU.value)


# Algorithm for LIGHT ENDs


@bot.message_handler(func=lambda message: dbworker.get_current_state(message.chat.id) == config.States.GAS.value)
def gas_options(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    keyboard.add(*[types.KeyboardButton(i) for i in ['Оплата', 'Тарифы', 'Проблема']])
    msg = bot.send_message(message.chat.id, "Выберите услуги Газоснабжения", reply_markup=keyboard)
    bot.register_next_step_handler(msg, gas)


def gas(message):
    if message.text == 'Оплата':
        dbworker.set_state(message.chat.id, config.States.PAY.value)
    elif message.text == 'Тарифы':
        dbworker.set_state(message.chat.id, config.States.COST_G.value)
    elif message.text == 'Проблема':
        dbworker.set_state(message.chat.id, config.States.PROBLEM_G.value)


@bot.message_handler(func=lambda message: dbworker.get_current_state(message.chat.id) == config.States.PROBLEM_G.value)
def pr_gas(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    keyboard.add(*[types.KeyboardButton(i) for i in ['Утечка газа', 'Отключили газ',
                                                     'Повреждение линии теплопередач', 'Другое']])
    msg = bot.send_message(message.chat.id, "Какая у Вас проблема?", reply_markup=keyboard)
    bot.register_next_step_handler(msg, problem_gas)


def problem_gas(message):#По вопросам ГАЗА Здесь заменены 2 блока текста на текстовые переменные чтобы было легче подгонять под необходимые районы 
    if message.text == 'Утечка газа' or message.text == 'Отключили газ':
        delete = types.ReplyKeyboardRemove(selective=False)
        bot.send_message(message.chat.id,gas_problems_setting0,#замена
                         reply_markup=delete,
                         parse_mode='Markdown')
        # dbworker.set_state(message.chat.id, config.States.MENU.value)

    elif message.text == 'Нарушение линии теплопередач' or message.text == 'Другое':
        delete = types.ReplyKeyboardRemove(selective=False)
        bot.send_message(message.chat.id, gas_problems_setting1,#замена
                         reply_markup=delete,#
                         parse_mode='Markdown')
    dbworker.set_state(message.chat.id, config.States.MENU.value)


@bot.message_handler(func=lambda message: dbworker.get_current_state(message.chat.id) == config.States.PAY.value)
def payment(message):#сайт оплаты услуг или что в этом роде заменена одна ссылка на переменную содержащую ссылку
    delete = types.ReplyKeyboardRemove(selective=False)
    bot.send_message(message.chat.id, "Вы можете оплатить счета "
                                      "[ЗДЕСЬ]"+payment_adress+"\n"#замена
                                      "Для возврата в главное меню введите _/start_",
                     reply_markup=delete, parse_mode='Markdown')
    dbworker.set_state(message.chat.id, config.States.MENU.value)


@bot.message_handler(func=lambda message: dbworker.get_current_state(message.chat.id) == config.States.COST_G.value)
def cost_gas(message):
    delete = types.ReplyKeyboardRemove(selective=False)
    bot.send_message(message.chat.id, "Вот тарифы на Газ:")
    bot.send_photo(message.chat.id, photo=open('cost_g.jpg', 'rb'))# Картинка с ценниками по газу и прочей шляпе
    bot.send_message(message.chat.id, "Для возврата в главное меню введите _/start_", reply_markup=delete,
                     parse_mode='Markdown')
    dbworker.set_state(message.chat.id, config.States.MENU.value)


# Другое

#Бля ну Я хз что с этим делать подкинь идей
@bot.message_handler(func=lambda message: dbworker.get_current_state(message.chat.id) == config.States.OTHER.value)
def other(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    keyboard.add(*[types.KeyboardButton(i) for i in ['Шутки-прибаутки', 'Оценить приложение']])
    msg = bot.send_message(message.chat.id, "Почитайте анекдоты или оцените приложение", reply_markup=keyboard)
    bot.register_next_step_handler(msg, other_opt)


def other_opt(message):
    delete = types.ReplyKeyboardRemove(selective=False)
    if message.text == 'Шутки-прибаутки':
        rand_joke = random.choice(config.jokes)
        bot.send_message(message.chat.id, rand_joke,
                         reply_markup=delete, parse_mode='Markdown')
        bot.send_message(message.chat.id, 'Пошутили и хватит. Для возврата в меню введите _/start_',
                         parse_mode='Markdown')
    elif message.text == 'Оценить приложение':
        keyboard = types.ReplyKeyboardMarkup(row_width=5, resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(i) for i in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']])
        msg = bot.send_message(message.chat.id, "Оцените приложение по шкале от 1 до 10", reply_markup=keyboard)
        bot.register_next_step_handler(msg, thanks)
    dbworker.set_state(message.chat.id, config.States.MENU.value)


def thanks(message):
    delete = types.ReplyKeyboardRemove(selective=False)
    bot.send_message(message.chat.id, "Спасибо, Ваш ответ записан. Для выхода в главное меню, введите _/start_",
                     reply_markup=delete, parse_mode='Markdown')

if __name__ == '__main__':
    bot.polling(none_stop=True)
