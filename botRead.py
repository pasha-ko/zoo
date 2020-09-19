import telebot

bot = telebot.TeleBot("1049064524:AAH3ULP_mIzviHZjrS-1rNsKyDVwwrrm4Mc")


 

while True:
    str = input()
    bot.send_message(205011385,str)
