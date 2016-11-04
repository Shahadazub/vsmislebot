# -*- coding: utf-8 -*-
from lxml import etree

list_of_riddle_elements = ['name', 'picture', 'text', 'answer', 'solved']


def get_corrected_riddle_id(chat_id):
    root = etree.parse('gamers.xml')
    print('File parsed')
    string_to_find = "gamer[@chat_id='" + chat_id + "']"
    print('string_to_find created')
    gamer = root.find(string_to_find)
    return gamer.find("riddle_id").text
    


def create_new_riddle(riddle_id):
    doc = etree.parse('riddles.xml')
    print("riddles.xml parsed")
    riddles = doc.getroot()
    print("root element for riddles recieved")
    riddle = etree.SubElement(riddles,'riddle')
    print("Riddle subelement created")
    riddle.set('id', riddle_id)
    for subelement_name in list_of_riddle_elements: 
        subelement = etree.SubElement(riddle, subelement_name)
        subelement.text = '0'
        print(subelement_name + ' created')
    riddles.append(riddle)
    print("riddle addded")
    finaltext = riddles.getroottree()
    print("created final tree")
    finaltext.write('riddles.xml',encoding="utf-8",pretty_print=True)
    print("file saved")
    

def gamer_mode(chat_id): 
    print('gamer_mode started')
    root = etree.parse('gamers.xml')
    print('File parsed')
    string_to_find = "gamer[@chat_id='" + chat_id + "']"
    print('string_to_find created')
    gamer = root.find(string_to_find)
    print(gamer)
    gamer_mode = gamer.find("mode")
    print(gamer_mode)
    return gamer_mode.text

def set_gamer_mode(chat_id, mode_text, riddle_id):
    root = etree.parse('gamers.xml')
    print('File parsed')
    string_to_find = "gamer[@chat_id='" + chat_id + "']"
    print('string_to_find created')
    gamer = root.find(string_to_find)
    gamer_mode = gamer.find("mode")
    gamer_mode.text = mode_text
    riddle_number = gamer.find("riddle_id")
    riddle_number.text = riddle_id
    
 
def insert_param_to_riddle(riddle_id, param, text):
    root = etree.parse('riddles.xml')
    print('riddles.xml parsed')
    string_to_find = "riddle[@id='" + str(riddle_id) + "']"
    riddle = root.find(string_to_find)
    riddle.find(param).text = text 


def riddle_id_is_free(riddle_id):
    root = etree.parse('riddles.xml')
    print('riddles.xml parsed')
    string_to_find = "riddle[@id='" + str(riddle_id) + "']"
    riddles = len(root.findall(string_to_find))
    if riddles == 0:
        print('Id is unique')
        return True
    else:
        print('ID is in use')
        return False


def create_first_xml():
    gamers = etree.Element('gamers')
    gamer = etree.SubElement(gamers, 'gamer')
    gamer.set('chat_id','278645740')
    chat_id = etree.SubElement(gamer, 'chat_id')
    whant_to_play = etree.SubElement(gamer, 'whant_to_play')
    chat_id.text = '278645740'
    whant_to_play.text = 'YES'
    finaltext = gamers.getroottree()
    finaltext.write('gamers.xml',pretty_print=True)

def this_gamer_is_in_xml(this_chat_id): #this function check if gamer already exist in gamers.xml
    root = etree.parse('gamers.xml')
    print('File parsed')
    string_to_find = "gamer[@chat_id='"+str(this_chat_id)+"']"
    print('string_to_find created')
    gamers = len(root.findall(string_to_find))
    print(root.findall(string_to_find))
    if gamers == 0:
        print('gamer not found')
        print(gamers)
        return False
    else:
        print('gamers not found')
        print(gamers)
        return True

def add_gamer_to_xml(this_chat_id): #function adds elements about new user
    print("add_gamer func started")
    doc = etree.parse('gamers.xml')
    gamers = doc.getroot()
    print("root element for gamers recieved")
    print("gamers.xml parsed")
    gamer = etree.SubElement(gamers,'gamer')
    print("Gamer subelement created")
    gamer.set('chat_id', str(this_chat_id))
    whant_to_play = etree.SubElement(gamer, 'whant_to_play')
    whant_to_play.text = 'NO'
    gamer_mode = etree.SubElement(gamer, 'mode')
    gamer_mode.text = 'null'
    riddle_number = etree.SubElement(gamer, 'riddle_id')
    gamers.append(gamer)
    print("gamer addded")
    finaltext = gamers.getroottree()
    print("created final tree")
    finaltext.write('gamers.xml',pretty_print=True)
    print("file saved")
    

def remove_gamer_from_xml(this_chat_id): #function deletes gamer element
    doc = etree.parse('gamers.xml')
    string_to_find = "gamer[@chat_id='"+str(this_chat_id)+"']"
    gamer = doc.find(string_to_find)
    parent = gamer.getparent()
    parent.remove(gamer)
    finaltext = parent.getroottree()
    finaltext.write('gamers.xml',pretty_print=True)

def create_riddles_xml():
    riddles = etree.Element('riddles')
    riddle = etree.SubElement(riddles, 'riddle')
    riddle.set('id', '1')
    riddle_name = etree.SubElement(riddle, 'name')
    riddle_name.text = 'Палки и Галки'
    picture = etree.SubElement(riddle, 'picture')
    picture.text = 'NO'
    riddle_text = etree.SubElement(riddle, 'text')
    riddle_text.text = 'Летели галки, сели на палки. Сядут по одной — галка лишняя, сядут по две — палка лишняя. Сколько было галок?'
    answer = etree.SubElement(riddle, 'answer')
    answer.text = '4'
    answer = etree.SubElement(riddle, 'answer')
    answer.text = 'четыре'
    solved = etree.SubElement(riddle, 'solved')
    solved.text = '0'
    finaltext = riddles.getroottree()
    finaltext.write('riddles.xml',encoding="utf-8",pretty_print=True)
