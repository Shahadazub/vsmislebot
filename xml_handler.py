from lxml import etree

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
