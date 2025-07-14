import telebot

# Replace with your actual Telegram bot token
TOKEN = '7801001027:AAGyimggZcZmGWRweWDuk3JU5OZ2vzPppks'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Welcome! This is the Sarkari Alert Bot. Use /notify to get exam alerts.")

@bot.message_handler(commands=['notify'])
def send_alert(message):
    bot.reply_to(message, "📢 Sarkari Exam Notification:\nUPSC NDA II Exam Date: 01 Sep 2025\nOfficial Link: https://upsc.gov.in")

print("Bot is running...")
bot.polling()
