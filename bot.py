import os
import telebot

# Mengambil token dari Environment Variable Render
TOKEN = os.environ.get("TELEGRAM_TOKEN")

bot = telebot.TeleBot(TOKEN)

# Perintah /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Halo! Bot ini berjalan di Render gratis!")

# Balas semua pesan lain
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, f"Pesan diterima: {message.text}")

# Jalankan bot
print("Bot sedang berjalan...")
bot.infinity_polling()
