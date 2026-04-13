import telebot
from telebot import types

token = '7742131379:AAHAnY-T_Ld5A_wY8UOfvP77Lz-vN9yGogU'
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(types.KeyboardButton('🔑 Insta Hack'))
    markup.add(types.KeyboardButton('📊 Statistika'), types.KeyboardButton('❓ Yordam'))
    bot.send_message(message.chat.id, f"Salom! Bo'limni tanlang:", reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def handle(message):
    if message.text == '🔑 Insta Hack':
        bot.send_message(message.chat.id, "Target nikini kiriting:")
    elif message.text == '❓ Yordam':
        bot.send_message(message.chat.id, "Admin: @saidjon_mc1")
    else:
        bot.send_message(message.chat.id, f"🔍 {message.text} tahlil qilinmoqda...")

if __name__ == "__main__":
    bot.polling(none_stop=True)
