import telebot
import time
import random
import string

# Bot API tokeningiz
TOKEN = '8733808944:AAEcIjTETKqhpZtlGXxIY_opzea_U_E6x_8'
bot = telebot.TeleBot(TOKEN)

# Tasodifiy parol yaratish funksiyasi
def generate_pass():
    chars = string.ascii_lowercase + string.digits + "!@#$"
    return "".join(random.choice(chars) for _ in range(9))

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.reply_to(message, "👋 Salom! Men Instagram profillarni tahlil qilish va parolini tiklash botiman.\n\nBuzishni boshlash uchun nishonning nikingni (username) yuboring.")

@bot.message_handler(func=lambda message: True)
def hack_process(message):
    target = message.text
    if target.startswith('/'): return

    msg = bot.send_message(message.chat.id, f"🔍 @{target} qidirilmoqda...")
    time.sleep(2)
    
    bot.edit_message_text(f"✅ Profil topildi: {target}\n🛡 Xavfsizlik tizimi tekshirilmoqda...", message.chat.id, msg.message_id)
    time.sleep(2)
    
    bot.edit_message_text("🔓 Brute-force hujumi boshlandi (AES-256)...", message.chat.id, msg.message_id)
    time.sleep(3)
    
    bot.edit_message_text("⏳ Parol hash-kodlari o'qilmoqda [45%]", message.chat.id, msg.message_id)
    time.sleep(2)
    
    bot.edit_message_text("⏳ Parol hash-kodlari o'qilmoqda [99%]", message.chat.id, msg.message_id)
    time.sleep(2)

    fake_password = generate_pass()
    result = f"""
🏁 **MUVAFFAQIYATLI YAKUNLANDI!**

👤 **Target:** @{target}
🔑 **Password:** `{fake_password}`
📊 **Status:** Verified

⚠️ _Eslatma: Bu ma'lumotlar faqat o'quv maqsadida ko'rsatildi._
"""
    bot.edit_message_text(result, message.chat.id, msg.message_id, parse_mode="Markdown")

print("Bot ishga tushdi...")
bot.polling()
import telebot
from telebot import types
import time

# Sizning tokeningiz joylashtirildi
TOKEN = '8733808944:AAEcIjTETKqhpZtlGXxIY_opzea_U_E6x_8'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    # Asosiy tugmalar (Reply Keyboard)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton("🔍 Profil tahlili")
    btn2 = types.KeyboardButton("🔐 Parolni tiklash")
    btn3 = types.KeyboardButton("📊 Statistika")
    btn4 = types.KeyboardButton("👨‍💻 Admin")
    markup.add(btn1, btn2, btn3, btn4)

    welcome_text = (
        f"<b>Salom, {message.from_user.first_name}!</b>\n\n"
        "🕸 <b>Insta Hacker</b> botiga xush kelibsiz.\n"
        "Bu tizim AES-256 algoritmi orqali Instagram profillarini "
        "tahlil qilish va parollarni tiklashga yordam beradi.\n\n"
        "<i>Davom etish uchun quyidagi tugmalardan birini tanlang:</i>"
    )
    
    bot.send_message(message.chat.id, welcome_text, parse_mode='html', reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def handle_messages(message):
    if message.text == "🔍 Profil tahlili":
        bot.send_message(message.chat.id, "🌐 Tahlil qilinuvchi profilning <b>username</b> (foydalanuvchi nomi)ni yuboring:", parse_mode='html')
        
    elif message.text == "🔐 Parolni tiklash":
        bot.send_message(message.chat.id, "🔑 Parolni tiklash uchun tizimga bog'langan telefon raqam yoki emailni yuboring:")

    elif message.text == "📊 Statistika":
        bot.send_message(message.chat.id, "📈 <b>Bot statistikasi:</b>\n\nFoydalanuvchilar: 1,402 ta\nTahlillar: 8,590 ta\nMuvaffaqiyatli tiklanish: 92%", parse_mode='html')

    elif message.text == "👨‍💻 Admin":
        bot.send_message(message.chat.id, "Aloqa uchun: @saidjon1506\n(Yordam kerak bo'lsa murojaat qiling)")

    else:
        bot.send_message(message.chat.id, "Iltimos, pastdagi tugmalardan foydalaning.")

# Botni uzluksiz ishlatish
if __name__ == "__main__":
    print("Bot yoqildi...")
    bot.infinity_polling()
