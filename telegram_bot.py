import telebot
from decouple import config
from time import sleep
from decouple import config
import random
from telebot import types

bot = telebot.TeleBot(
    token=config('TOKEN_BOT')
)
#commands
#@bot.message_handler(commands=['hi'])
#def start(message):
 #   bot.send_message(message.chat.id, 'привет я кот, теперь я твой хозяин')
#buttons
#@bot.message_handler(commands=['hi', 'hello', 'start', 'привет'])
#def button(message):
  # markup = types.InlineKeyboardMarkup(row_width=2)
  #  btn1= types.InlineKeyboardButton('Как дела?', callback_data='question_1')
  #  btn2 = types.InlineKeyboardButton('Пока', callback_data='goodbye')
  #  markup.add(btn1,btn2)
  #  bot.send_message(message.chat.id, 'Привет!', reply_markup=markup)
@bot.message_handler(commands=['hi'])
def welcome(message):
    # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("🎲 Рандомное число")
    item2 = types.KeyboardButton("😊 Как дела?")
    item3 = types.KeyboardButton("🔭 гороскоп")

    markup.add(item1, item2, item3)

    bot.send_message(message.chat.id,
                     "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот созданный чтобы быть подопытным кроликом.".format(
                         message.from_user, bot.get_me()),
                     parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def dududu(message):
    if message.chat.type == 'private':
        if message.text == '🎲 Рандомное число':
            bot.send_message(message.chat.id, str(random.randint(0, 10)))
        elif message.text == '😊 Как дела?':

            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("Хорошо", callback_data='good')
            item2 = types.InlineKeyboardButton("Не очень", callback_data='bad')

            markup.add(item1, item2)
            bot.send_message(message.chat.id, 'Отлично, сам как?', reply_markup=markup)

        elif message.text == '🔭 гороскоп':
            markup = types.InlineKeyboardMarkup(row_width=13)
            item1 = types.InlineKeyboardButton("♈ Овен", callback_data='♈ Овен')
            item2 = types.InlineKeyboardButton("♉ Телец", callback_data='♉ Телец')
            item3 = types.InlineKeyboardButton("♊ Близнецы", callback_data='♊ Близнецы')
            item4 = types.InlineKeyboardButton("♋ Рак", callback_data='♋ Рак')
            item5 = types.InlineKeyboardButton("♌ Лев", callback_data='♌ Лев')
            item6 = types.InlineKeyboardButton("♍ Дева", callback_data='♍ Дева')
            item7 = types.InlineKeyboardButton("♎ Весы", callback_data='♎ Весы')
            item8 = types.InlineKeyboardButton("♏ Скорпион", callback_data='♏ Скорпион')
            item9 = types.InlineKeyboardButton("⛎ Змееносец", callback_data='⛎ Змееносец')
            item10 = types.InlineKeyboardButton("♐ Стрелец", callback_data='♐ Стрелец')
            item11 = types.InlineKeyboardButton( '♑ Козерог', callback_data=' ♑ Козерог')
            item12= types.InlineKeyboardButton("♒ Водолей", callback_data='♒ Водолей')
            item13 = types.InlineKeyboardButton("♓ Рыбы", callback_data='♓ Рыбы')

            markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11, item12, item13)

            bot.send_message(message.chat.id, 'выбери свой знак зодиака?', reply_markup=markup)



@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'good':
                bot.send_message(call.message.chat.id, 'Вот и отличненько 😊')
            elif call.data == 'bad':
                bot.send_message(call.message.chat.id, 'Бывает 😢')
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="😊 Как дела?",
                                  reply_markup=None)
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                text="ЭТО ТЕСТОВОЕ УВЕДОМЛЕНИЕ!!11")

    except Exception as e:
        print(repr(e))
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == '♈ Овен':
                bot.send_message(call.message.chat.id, 'Вот и отличненько 😊')
            elif call.data == '♉ Телец':
                bot.send_message(call.message.chat.id, 'Бывает 😢')
            elif call.data == '♊ Близнецы':
                bot.send_message(call.message.chat.id, 'Вот и отличненько 😊')
            elif call.data == '♋ Рак':
                bot.send_message(call.message.chat.id, 'Бывает 😢')
            elif call.data == '♌ Лев':
                bot.send_message(call.message.chat.id, 'Вот и отличненько 😊')
            elif call.data == '♍ Дева':
                bot.send_message(call.message.chat.id, 'Бывает 😢')
            elif call.data == '♎ Весы':
                    bot.send_message(call.message.chat.id, 'Вот и отличненько 😊')
            elif call.data == '♏ Скорпион':
                    bot.send_message(call.message.chat.id, 'Бывает 😢')
            elif call.data == '⛎ Змееносец':
                bot.send_message(call.message.chat.id, 'Бывает 😢')
            elif call.data == '♐ Стрелец':
                bot.send_message(call.message.chat.id, 'Вот и отличненько 😊')
            elif call.data == '♑ Козерог':
                bot.send_message(call.message.chat.id, 'Бывает 😢')
            elif call.data == '♒ Водолей':
                bot.send_message(call.message.chat.id, 'Вот и отличненько 😊')
            elif call.data == '♓ Рыбы':
                bot.send_message(call.message.chat.id, 'Бывает 😢')
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="😊 Как дела?",
                                  reply_markup=None)
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                text="ЭТО ТЕСТОВОЕ УВЕДОМЛЕНИЕ!!11")


    except Exception as e:\
                print(repr(e))




@bot.message_handler (commands= ["random_num"])
def random_num(message):
    num = random.randint(1, 10)
    bot.send_message(message.chat.id, str(num))

#textbot.py
@bot.message_handler(content_types=['text'])
def text(message):
    if message.text.lower() == 'привет':
     bot.send_message(message.chat.id, "привет, привет")




bot.polling()
