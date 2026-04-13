import telebot
from telebot import types

# Tokeningizni tekshiring, u qo'shtirnoq ichida bo'lishi shart
token = '7742131379:AAHAnY-T_Ld5A_wY8UOfvP77Lz-vN9yGogU'
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_hack = types.KeyboardButton('🔑 Insta Hack')
    btn_stats = types.KeyboardButton('📊 Statistika')
    btn_help = types.KeyboardButton('❓ Yordam')
    btn_settings = types.KeyboardButton('⚙️ Sozlamalar')
    
    markup.add(btn_hack)
    markup.add(btn_stats, btn_help, btn_settings)
    
    user_name = message.from_user.first_name
    bot.send_message(message.chat.id, f"Salom {user_name}! Kerakli bo'limni tanlang:", reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def handle_messages(message):
    if message.text == '🔑 Insta Hack':
        bot.send_message(message.chat.id, "Target (qurbon) nikini kiriting:")
    elif message.text == '📊 Statistika':
        bot.send_message(message.chat.id, "📈 Bot holati: Online\n👥 Foydalanuvchilar: 1,254 ta\n✅ Muvaffaqiyatli tahlillar: 842 ta")
    elif message.text == '❓ Yordam':
        bot.send_message(message.chat.id, "🆘 Muammo yuzaga kelsa, adminga murojaat qiling:\n\n👨‍💻 Admin: @saidjon_mc1")
    elif message.text == '⚙️ Sozlamalar':
        bot.send_message(message.chat.id, "⚙️ Sozlamalar bo'limi hozircha tahrirlash jarayonida.")
    else:
        bot.send_message(message.chat.id, f"🔍 {message.text} tahlil qilinmoqda...\n⌛ Iltimos, 1-2 daqiqa kuting...")

# Buni o'zgartirmang
if __name__ == "__main__":
    bot.polling(none_stop=True)
