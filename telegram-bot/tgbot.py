import telebot
import requests

token = """ваш токен"""


bot = telebot.TeleBot(token)


@bot.message_handler(content_types=["text"])
def content_messages(message):
    response = requests.post('http://127.0.0.1:5000/artem/', data=message.text)
    bot.send_message(message.from_user.id, response.text)


bot.polling()
