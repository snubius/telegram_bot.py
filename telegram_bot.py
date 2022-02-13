import telebot
from decouple import config
from telebot import types

bot = telebot.TeleBot(
    token=config('TOKEN_BOT')
)

@bot.message_handler(commands=["start","привет","Привет","hi","HI", "HELLO", "hello"])
def answer_start(message):
    text = f"чтож кем ты хочeшь стать?   {message.from_user.first_name} "\
           f" Выбери свой путь"
    keyboard_in = types.InlineKeyboardMarkup()
    bot.send_message(message.chat.id, text)
    btn_1 = types.InlineKeyboardButton(text='стать самураем', callback_data="стать самураем")
    btn_2 = types.InlineKeyboardButton(text='торговцем', callback_data="торговцем")

    keyboard_in.add(btn_1, btn_2)
    bot.send_message(message.chat.id, text, reply_markup=keyboard_in)


@bot.callback_query_handler(func=lambda call:True)
def send_course(call):
    if call.data == 'стать самураем':
        murkup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn_1 = types.KeyboardButton('клан токугава')
        btn_2 = types.KeyboardButton('клан ода' )
        btn_3 = types.KeyboardButton('клан мори')
        murkup_reply.add(btn_1, btn_2, btn_3)
        text = f"У самурая нет цели только путь! Вперед!"
        bot.send_message(call.message.chat.id, text,
                         reply_markup=murkup_reply
                         )
    elif call.data == 'торговцем':
        murkup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btv_1 = types.KeyboardButton("оми")
        btv_2 = types.KeyboardButton("кавати")
        btv_3 = types.KeyboardButton("ямасита")
        btv_4 = types.KeyboardButton("микава")
        murkup_reply.add(btv_1, btv_2, btv_3,btv_4)
        text = f"ты стал торговцем,выбери провинцию "
        bot.send_message(call.message.chat.id, text,
                         reply_markup=murkup_reply
                         )


@bot.message_handler(content_types=['text'])
def send_good_message(message):
    if message.text == 'клан токугава':
        bot.send_message(message.chat.id, f"ты стал самураем клана токугава" )
    elif message.text == 'клан ода':
        bot.send_message(message.chat.id, f"ты стал стал самураем клана ода" )
    if message.text == 'клан мори':
        bot.send_message(message.chat.id, f"ты стал стал самураем клана мори" )




bot.polling()
