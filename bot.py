import config

import telebot
import xml_handler
from time import sleep

wow_message = "Воу, ну что ты сразу начинаешь. Полегче. Что хотел то?"
message_to_send = 'Hi'

bot = telebot.TeleBot(config.token)




@bot.message_handler(commands=['go'])
def ask_everyone_to_go(message): # function that send offer to go overwatch
    bot.send_message('278645740','Уважаемый, тут братушенции в оверов заходят. Не соизволите затащить пару каток?')

@bot.message_handler(commands=['add_me'])
def add_gamer(message):
    print("add_me command recieved")
    if xml_handler.this_gamer_is_in_xml(message.chat.id):
        bot.send_message(message.chat.id,"Эээ, братишь, ты уже в системе")
    else:
        xml_handler.add_gamer_to_xml(message.chat.id)
        bot.send_message(message.chat.id,"You were added to the list")
        sleep(3)
        bot.send_message(message.chat.id,"bitch")

@bot.message_handler(commands=['delete_me'])
def remove_gamer(message):
    print("remove_me command recieved")
    if xml_handler.this_gamer_is_in_xml(message.chat.id):
        xml_handler.remove_gamer_from_xml(message.chat.id)
        bot.send_message(message.chat.id,"You were deleted from the list")
        sleep(3)
        bot.send_message(message.chat.id,"bitch")

    else:
        bot.send_message(message.chat.id,"А ты ваще откуда нарисовался? Тебя тут небыло.")

@bot.message_handler(content_types=["text"])
def answer_to_user(message): #function that send answer
    if message.text[:18] == 'В смысле, в смысле':
        message_to_send = wow_message
    else:
        message_to_send = "В смысле, " + message.text + "?"
    bot.send_message(message.chat.id, message_to_send)
    print(message.chat.id)

if __name__ == '__main__':
    bot.polling(none_stop=True)
    
