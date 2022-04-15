import telebot
import requests
bot =telebot.TeleBot("5325270695:AAHHsG2D7MMHKk4Sgnr1gzAY-L0OCg9uR3Y")
@bot.message_handler(commands=["start","help"])
def start(message):
	while True:
		bot.send_message(message.chat.id,"@يا قائم ال محمد يا منصور@"*100)
bot.polling()
