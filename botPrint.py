import telebot

bot = telebot.TeleBot("1049064524:AAH3ULP_mIzviHZjrS-1rNsKyDVwwrrm4Mc")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    global chat
    chat = message.chat.id
    print(chat)
    bot.stop_polling()

@bot.message_handler(content_types=["text"])
def answer(message):
    print(message.text,flush=True)       

bot.polling()
