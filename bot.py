import config

import telebot

wow_message = "Воу, ну что ты сразу начинаешь. Полегче. Что хотел то?"
message_to_send = 'Hi'

bot = telebot.TeleBot(config.token)

@bot.message_handler(content_types=["text"])


def answer_to_user(message): #function that send answer
    if message.text[:18] == 'В смысле, в смысле':
        message_to_send = wow_message
    else:
        message_to_send = "В смысле, " + message.text + "?"
    bot.send_message(message.chat.id, message_to_send)

if __name__ == '__main__':
    bot.polling(none_stop=True)
    
