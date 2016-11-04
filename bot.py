#-*- coding: utf-8 -*-
import config



import telebot
import xml_handler
from time import sleep
import random

wow_message = "Воу, ну что ты сразу начинаешь. Полегче. Что хотел то?"


bot = telebot.TeleBot(config.token)

def get_new_riddle_id():
    print('get_new_riddle_id started')
    new_riddle_id = random.randrange(0,10000)
    print('new riddle id = ' + str(new_riddle_id))
    if xml_handler.riddle_id_is_free(str(new_riddle_id)):
        print('riddle id is unique')
        return str(new_riddle_id)
    else:
        print('riddle id already exist')
        get_new_riddle_id()

    




@bot.message_handler(commands=['go'])
def ask_everyone_to_go(message): # function that send offer to go overwatch
    bot.send_message('278645740','Уважаемый, тут братушенции в оверов заходят. Не соизволите затащить пару каток?')

@bot.message_handler(commands=['add_me'])
def add_gamer(message):
    print("add_me command recieved")
    if xml_handler.this_gamer_is_in_xml(message.chat.id):
        bot.send_message(message.chat.id,"Привет, братишь, а я тебя знаю")
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


@bot.message_handler(commands=['add_riddle'])
def add_riddle_to_xml(message):
    if xml_handler.this_gamer_is_in_xml(message.chat.id):
        bot.send_message(message.chat.id,"Привет, братишь, а я тебя знаю")
    else:
        xml_handler.add_gamer_to_xml(message.chat.id)
        bot.send_message(message.chat.id,"You were added to the list")
        sleep(3)
        bot.send_message(message.chat.id,"bitch")
    print(str(message.chat.id) + ' sent request to add riddle')
    if message.chat.id != 278645740:
        bot.send_message(message.chat.id,'В смысле, add_riddle?')
    else:        
        print('command add_riddle_to_xml recieved')
        adding_riddle = True
        param = 'name'
        riddle_id = get_new_riddle_id()
        xml_handler.create_new_riddle(riddle_id)
        bot.send_message(message.chat.id,'Какое будет имя у загадки?')
        xml_handler.set_gamer_mode(str(message.chat.id), 'name', str(riddle_id))
        


@bot.message_handler(content_types=["text"])
def answer_to_user(message): #function that send answer
    param = xml_handler.gamer_mode(str(message.chat.id))
    if xml_handler.this_gamer_is_in_xml(message.chat.id):
        bot.send_message(message.chat.id,"Привет, братишь, а я тебя знаю")
    else:
        xml_handler.add_gamer_to_xml(message.chat.id)
        bot.send_message(message.chat.id,"You were added to the list")
        sleep(3)
        bot.send_message(message.chat.id,"bitch")
    if param == 'null':
        if message.text[:18] == 'В смысле, в смысле':
            message_to_send = wow_message
            bot.send_message(message.chat.id, message_to_send)
        else:
            message_to_send = "В смысле, " + message.text + "?"
            bot.send_message(message.chat.id, message_to_send)
            print(message.chat.id)
    else:
        riddle_id = get_corrected_riddle_id(str(message.chat.id))
        print('adding printed text to riddle')
        if param == 'name':
            xml_handler.insert_param_to_riddle(str(riddle_id), param, message.text)
            xml_handler.set_gamer_mode(str(message.chat.id),'text', str(riddle_id))
            bot.send_message(str(message.chat.id), 'Какой текст задачи?')
        elif  param == 'text':
            xml_handler.insert_param_to_riddle(str(riddle_id), param, message.text)
            xml_handler.set_gamer_mode(str(message.chat.id),'answer')
            bot.send_message(str(message.chat.id), 'Какой правильный ответ?')
        elif param == 'answer':
            xml_handler.insert_param_to_riddle(str(riddle_id), param, message.text)
            xml_handler.set_gamer_mode(str(message.chat.id),'another answer')
            bot.send_message(str(message.chat.id), 'Еще один ответ?')
        elif param == 'another answer':
            if message.text == 'Да':
                xml_handler.set_gamer_mode(str(message.chat.id),'answer')
                bot.send_message(message.chat.id, 'Какой правильный ответ?')
            else:
                xml_handler.set_gamer_mode(str(message.chat.id),'null')
                bot.send_message(message.chat.id, 'Новая загадка сохранена')
                #show_riddle(riddle_id)
                

if __name__ == '__main__':
    bot.polling(none_stop=True)
    
