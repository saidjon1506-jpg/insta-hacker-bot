import telebot
from telebot import types

token = '8733808944:AAHHeOgZMFhWhiLg2O8_AzSyHpFuBiGLjWQ'
bot = telebot.TeleBot(token)

# Foydalanuvchilar balansini saqlash (Vaqtincha lug'atda)
user_balances = {}

@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.chat.id
    if user_id not in user_balances:
        user_balances[user_id] = 0  # Yangi foydalanuvchiga 0 so'm
    
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_hack = types.KeyboardButton('🔑 Insta Hack')
    btn_balance = types.KeyboardButton('💰 Mening balansim')
    btn_topup = types.KeyboardButton('💵 Hisobni to'ldirish')
    btn_help = types.KeyboardButton('❓ Yordam')
    
    markup.add(btn_hack)
    markup.add(btn_balance, btn_topup)
    markup.add(btn_help)
    
    bot.send_message(user_id, f"Salom! Botimizga xush kelibsiz.\nSizning balansingiz: {user_balances[user_id]} so'm", reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def handle_logic(message):
    user_id = message.chat.id
    if user_id not in user_balances:
        user_balances[user_id] = 0

    if message.text == '🔑 Insta Hack':
        bot.send_message(user_id, "Target (qurbon) nikini yozing:")

    elif message.text == '💰 Mening balansim':
        bot.send_message(user_id, f"Sizning joriy balansingiz: {user_balances[user_id]} so'm")

    elif message.text == '💵 Hisobni to'ldirish':
        # Admin bilan bog'lanish tugmasi
        markup = types.InlineKeyboardMarkup()
        admin_btn = types.InlineKeyboardButton("👤 Adminga yozish", url="https://t.me/saidjon_mc1")
        markup.add(admin_btn)
        bot.send_message(user_id, "Hisobni to'ldirish uchun adminga murojaat qiling va to'lov skrinshotini yuboring:", reply_markup=markup)

    elif message.text == '❓ Yordam':
        bot.send_message(user_id, "Admin: @saidjon_mc1\nNarx: 1 ta akkaunt = 1000 so'm")

    else:
        # Agar foydalanuvchi nik yozgan bo'lsa
        if user_balances[user_id] >= 1000:
            user_balances[user_id] -= 1000
            bot.send_message(user_id, f"🔍 {message.text} tahlil qilinmoqda...")
            bot.send_message(user_id, "✅ Muvaffaqiyatli! To'lov qabul qilindi.\n🔑 Parol: admin2024_secret\n💰 Qolgan balansingiz: {user_balances[user_id]} so'm")
        else:
            bot.send_message(user_id, f"🔍 {message.text} tahlil qilinmoqda...")
            bot.send_message(user_id, "❌ Balansingizda mablag' yetarli emas!\n🔑 Parol: **********\n\nIltimos, hisobingizni 1000 so'mga to'ldiring.")

if __name__ == "__main__":
    bot.infinity_polling()
