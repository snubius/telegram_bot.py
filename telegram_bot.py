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
                     "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот созданный чтобы быть подопытным котиком.".format(
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
        else:
            bot.send_message(message.chat.id, 'Я не знаю что ответить 😢')

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
