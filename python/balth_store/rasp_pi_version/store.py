# list of lists structured like this
# [[iteam_name, Rarity, source, price_gold, price_blood], [.........]........]
# colour the different rarities different colours
# or, display by rarity in seperate sections
# Use tkinter to make a GUI for it
# balth gets more funding and so he revamped his store
# seperate sections for each rarity type
# random number of iteams for each rarity
# 

from tkinter import *
from re import findall
from random import randint
from os import system

system ('cd ~/Desktop/project_files')

def common_collect():
    global common_items
    common_file = open('common.txt', 'r')
    common = common_file.read()
    common_file.close()

    common_content = findall('([A-Z].+), ([A-Z-a-z]+), (.+), ([NoYes]+)',
                             common)
    #print(len(common_content))

    common_items = []
    for item, source, type, attune in common_content:
        gold_price = str(randint(20, 70)) + ' gp'
        common_items.append((item, source, type, attune, gold_price))
    #for a in common_items:
    #    print(a)

def uncommon_collect():
    global uncommon_items
    uncommon_file = open('uncommon.txt', 'r')
    uncommon = uncommon_file.read()
    uncommon_file.close()

    uncommon_content = findall('([A-Z].+), ([A-Z-a-z]+), (.+), ([NoYes]+)',
                               uncommon)
    #print(len(uncommon_content))

    uncommon_items = []
    for item, source, type, attune in uncommon_content:
        gold_price = str(randint(100, 600)) + ' gp'
        uncommon_items.append((item, source, type, attune, gold_price))
    #for a in uncommon_items:
    #    print(a)

def rare_collect():
    global rare_items
    rare_file = open('rare.txt', 'r')
    rare = rare_file.read()
    rare_file.close()

    rare_content = findall('([A-Z].+), ([A-Z-a-z]+), (.+), ([NoYes]+)',
                               rare)
    #print(len(rare_content))

    rare_items = []
    for item, source, type, attune in rare_content:
        gold_price = str(randint(2000, 20000)) + ' gp'
        rare_items.append((item, source, type, attune, gold_price))
    #for a in rare_items:
    #    print(a)

def very_rare_collect():
    global very_rare_items
    very_rare_file = open('very_rare.txt', 'r')
    very_rare = very_rare_file.read()
    very_rare_file.close()

    very_rare_content = findall('([A-Z].+), ([A-Z-a-z]+), (.+), ([NoYes]+)',
                               very_rare)
    #print(len(very_rare_content))

    very_rare_items = []
    for item, source, type, attune in very_rare_content:
        gold_price = str(randint(20000, 50000)) + ' gp'
        very_rare_items.append((item, source, type, attune, gold_price))
    #for a in very_rare_items:
    #    print(a)

def legendary_collect():
    global legendary_items
    legendary_file = open('legendary.txt', 'r')
    legendary = legendary_file.read()
    legendary_file.close()

    legendary_content = findall('([A-Z].+), ([A-Z-a-z]+), (.+), ([NoYes]+)',
                               legendary)
    #print(len(legendary_content))

    legendary_items = []
    for item, source, type, attune in legendary_content:
        gold_price = str(randint(50000, 300000)) + ' gp'
        legendary_items.append((item, source, type, attune, gold_price))
    #for a in legendary_items:
    #    print(a)

common_collect()
uncommon_collect()
rare_collect()
very_rare_collect()
legendary_collect()


#############################################################################
#                        inventory window functions                         #
#############################################################################

def print_selected_func():
    item_options = [com_1_text, com_2_text, com_3_text, com_4_text, com_5_text,
                   com_6_text, com_7_text, com_8_text, com_9_text, unc_1_text,
                   unc_2_text, unc_3_text, unc_4_text, unc_5_text, unc_6_text,
                   unc_7_text, unc_8_text, unc_9_text, unc_10_text, unc_11_text,
                   rar_1_text, rar_2_text, rar_3_text, rar_4_text, rar_5_text,
                   ver_1_text, ver_2_text, ver_3_text, ver_4_text, leg_1_text,
                   leg_2_text, orb_text]

    selected = open('Selected_Items.txt', 'w')
    
    for item in item_options:
        selected.write(item)

    selected.close()

    #################drop box thingy goes here###################
    system ('./dropbox_uploader.sh upload Selected_Items.txt Selected_Items.txt')
    

def print_inventory_func():
    global common_inventory_items, uncommon_inventory_items
    global rare_inventory_items, very_rare_inventory_items
    global legendary_inventory_items, orb_info
    
    inventory = open('Inventory.txt', 'w')

    inventory.write('\n\n------------common------------\n\n')

    for item in common_inventory_items:
        inventory.write(item[0] + ', ' + item[1] + ', ' + item[2] + ', ' + item[3]
                         + ', ' + item[4] + '\n')

    inventory.write('\n\n------------uncommon------------\n\n')

    for item in uncommon_inventory_items:
        inventory.write(item[0] + ', ' + item[1] + ', ' + item[2] + ', ' + item[3]
                         + ', ' + item[4] + '\n')

    inventory.write('\n\n------------rare------------\n\n')

    for item in rare_inventory_items:
        inventory.write(item[0] + ', ' + item[1] + ', ' + item[2] + ', ' + item[3]
                         + ', ' + item[4] + '\n')

    inventory.write('\n\n------------very_rare------------\n\n')

    for item in very_rare_inventory_items:
        inventory.write(item[0] + ', ' + item[1] + ', ' + item[2] + ', ' + item[3]
                         + ', ' + item[4] + '\n')

    inventory.write('\n\n------------legendary------------\n\n')

    for item in legendary_inventory_items:
        inventory.write(item[0] + ', ' + item[1] + ', ' + item[2] + ', ' + item[3]
                         + ', ' + item[4] + '\n')

    inventory.write('\n\n------------orb------------\n\n')

    inventory.write(orb_info[0] + ', ' + orb_info[1] + ', ' + orb_info[2]
                    + ', ' + orb_info[3] + ', ' + orb_info[4])

    inventory.close()
    
    #################drop box thingy goes here###################
    system ('./dropbox_uploader.sh upload Inventory.txt Inventory.txt')
    
def restock_func():
    global inventory
    
    inventory.destroy()

    inventory_window_create()

    text_stores = [com_1_text, com_2_text, com_3_text, com_4_text, com_5_text,
                   com_6_text, com_7_text, com_8_text, com_9_text, unc_1_text,
                   unc_2_text, unc_3_text, unc_4_text, unc_5_text, unc_6_text,
                   unc_7_text, unc_8_text, unc_9_text, unc_10_text, unc_11_text,
                   rar_1_text, rar_2_text, rar_3_text, rar_4_text, rar_5_text,
                   ver_1_text, ver_2_text, ver_3_text, ver_4_text, leg_1_text,
                   leg_2_text, orb_text]

    for item in text_stores:
        item = ''

def close_inventory_func():
    global inventory

    inventory.destroy()


#############################################################################
#                           common item functions                           #
#############################################################################

com_1_text = ''
def com_1_func():
    global com_1_var, common_inventory_items, com_1_text
    if com_1_var.get() == 0:
        com_1_text = ''
        print('yeet')
    elif com_1_var.get() == 1:
        com_1_text = (common_inventory_items[0][0] + ', ' +
                      common_inventory_items[0][1] + ', ' +
                      common_inventory_items[0][2] + ', ' +
                      common_inventory_items[0][3] + ', ' +
                      common_inventory_items[0][4] + '\n')
    print(com_1_text)

com_2_text = ''
def com_2_func():
    global com_2_var, common_inventory_items, com_2_text
    if com_2_var.get() == 0:
        com_2_text = ''
        print('yeet')
    elif com_2_var.get() == 1:
        com_2_text = (common_inventory_items[1][0] + ', ' +
                      common_inventory_items[1][1] + ', ' +
                      common_inventory_items[1][2] + ', ' +
                      common_inventory_items[1][3] + ', ' +
                      common_inventory_items[1][4] + '\n')
    print(com_2_text)

com_3_text = ''
def com_3_func():
    global com_3_var, common_inventory_items, com_3_text
    if com_3_var.get() == 0:
        com_3_text = ''
        print('yeet')
    elif com_3_var.get() == 1:
        com_3_text = (common_inventory_items[2][0] + ', ' +
                      common_inventory_items[2][1] + ', ' +
                      common_inventory_items[2][2] + ', ' +
                      common_inventory_items[2][3] + ', ' +
                      common_inventory_items[2][4] + '\n')
    print(com_3_text)

com_4_text = ''
def com_4_func():
    global com_4_var, common_inventory_items, com_4_text
    if com_4_var.get() == 0:
        com_4_text = ''
        print('yeet')
    elif com_4_var.get() == 1:
        com_4_text = (common_inventory_items[3][0] + ', ' +
                      common_inventory_items[3][1] + ', ' +
                      common_inventory_items[3][2] + ', ' +
                      common_inventory_items[3][3] + ', ' +
                      common_inventory_items[3][4] + '\n')
    print(com_4_text)

com_5_text = ''
def com_5_func():
    global com_5_var, common_inventory_items, com_5_text
    if com_5_var.get() == 0:
        com_5_text = ''
        print('yeet')
    elif com_5_var.get() == 1:
        com_5_text = (common_inventory_items[4][0] + ', ' +
                      common_inventory_items[4][1] + ', ' +
                      common_inventory_items[4][2] + ', ' +
                      common_inventory_items[4][3] + ', ' +
                      common_inventory_items[4][4] + '\n')
    print(com_5_text)

com_6_text = ''
def com_6_func():
    global com_6_var, common_inventory_items, com_6_text
    if com_6_var.get() == 0:
        com_6_text = ''
        print('yeet')
    elif com_6_var.get() == 1:
        com_6_text = (common_inventory_items[5][0] + ', ' +
                      common_inventory_items[5][1] + ', ' +
                      common_inventory_items[5][2] + ', ' +
                      common_inventory_items[5][3] + ', ' +
                      common_inventory_items[5][4] + '\n')
    print(com_6_text)

com_7_text = ''
def com_7_func():
    global com_7_var, common_inventory_items, com_7_text
    if com_7_var.get() == 0:
        com_7_text = ''
        print('yeet')
    elif com_7_var.get() == 1:
        com_7_text = (common_inventory_items[6][0] + ', ' +
                      common_inventory_items[6][1] + ', ' +
                      common_inventory_items[6][2] + ', ' +
                      common_inventory_items[6][3] + ', ' +
                      common_inventory_items[6][4] + '\n')
    print(com_7_text)

com_8_text = ''
def com_8_func():
    global com_8_var, common_inventory_items, com_8_text
    if com_8_var.get() == 0:
        com_8_text = ''
        print('yeet')
    elif com_8_var.get() == 1:
        com_8_text = (common_inventory_items[7][0] + ', ' +
                      common_inventory_items[7][1] + ', ' +
                      common_inventory_items[7][2] + ', ' +
                      common_inventory_items[7][3] + ', ' +
                      common_inventory_items[7][4] + '\n')
    print(com_8_text)

com_9_text = ''
def com_9_func():
    global com_9_var, common_inventory_items, com_9_text
    if com_9_var.get() == 0:
        com_9_text = ''
        print('yeet')
    elif com_9_var.get() == 1:
        com_9_text = (common_inventory_items[8][0] + ', ' +
                      common_inventory_items[8][1] + ', ' +
                      common_inventory_items[8][2] + ', ' +
                      common_inventory_items[8][3] + ', ' +
                      common_inventory_items[8][4] + '\n')
    print(com_9_text)


#############################################################################
#                          uncommon item functions                          #
#############################################################################

unc_1_text = ''
def unc_1_func():
    global unc_1_var, uncommon_inventory_items, unc_1_text
    if unc_1_var.get() == 0:
        unc_1_text = ''
        print('yeet')
    elif unc_1_var.get() == 1:
        unc_1_text = (uncommon_inventory_items[0][0] + ', ' +
                      uncommon_inventory_items[0][1] + ', ' +
                      uncommon_inventory_items[0][2] + ', ' +
                      uncommon_inventory_items[0][3] + ', ' +
                      uncommon_inventory_items[0][4] + '\n')
    print(unc_1_text)

unc_2_text = ''
def unc_2_func():
    global unc_2_var, uncommon_inventory_items, unc_2_text
    if unc_2_var.get() == 0:
        unc_2_text = ''
        print('yeet')
    elif unc_2_var.get() == 1:
        unc_2_text = (uncommon_inventory_items[1][0] + ', ' +
                      uncommon_inventory_items[1][1] + ', ' +
                      uncommon_inventory_items[1][2] + ', ' +
                      uncommon_inventory_items[1][3] + ', ' +
                      uncommon_inventory_items[1][4] + '\n')
    print(unc_2_text)

unc_3_text = ''
def unc_3_func():
    global unc_3_var, uncommon_inventory_items, unc_3_text
    if unc_3_var.get() == 0:
        unc_3_text = ''
        print('yeet')
    elif unc_3_var.get() == 1:
        unc_3_text = (uncommon_inventory_items[2][0] + ', ' +
                      uncommon_inventory_items[2][1] + ', ' +
                      uncommon_inventory_items[2][2] + ', ' +
                      uncommon_inventory_items[2][3] + ', ' +
                      uncommon_inventory_items[2][4] + '\n')
    print(unc_3_text)

unc_4_text = ''
def unc_4_func():
    global unc_4_var, uncommon_inventory_items, unc_4_text
    if unc_4_var.get() == 0:
        unc_4_text = ''
        print('yeet')
    elif unc_4_var.get() == 1:
        unc_4_text = (uncommon_inventory_items[3][0] + ', ' +
                      uncommon_inventory_items[3][1] + ', ' +
                      uncommon_inventory_items[3][2] + ', ' +
                      uncommon_inventory_items[3][3] + ', ' +
                      uncommon_inventory_items[3][4] + '\n')
    print(unc_4_text)

unc_5_text = ''
def unc_5_func():
    global unc_5_var, uncommon_inventory_items, unc_5_text
    if unc_5_var.get() == 0:
        unc_5_text = ''
        print('yeet')
    elif unc_5_var.get() == 1:
        unc_5_text = (uncommon_inventory_items[4][0] + ', ' +
                      uncommon_inventory_items[4][1] + ', ' +
                      uncommon_inventory_items[4][2] + ', ' +
                      uncommon_inventory_items[4][3] + ', ' +
                      uncommon_inventory_items[4][4] + '\n')
    print(unc_5_text)

unc_6_text = ''
def unc_6_func():
    global unc_6_var, uncommon_inventory_items, unc_6_text
    if unc_6_var.get() == 0:
        unc_6_text = ''
        print('yeet')
    elif unc_6_var.get() == 1:
        unc_6_text = (uncommon_inventory_items[5][0] + ', ' +
                      uncommon_inventory_items[5][1] + ', ' +
                      uncommon_inventory_items[5][2] + ', ' +
                      uncommon_inventory_items[5][3] + ', ' +
                      uncommon_inventory_items[5][4] + '\n')
    print(unc_6_text)

unc_7_text = ''
def unc_7_func():
    global unc_7_var, uncommon_inventory_items, unc_7_text
    if unc_7_var.get() == 0:
        unc_7_text = ''
        print('yeet')
    elif unc_7_var.get() == 1:
        unc_7_text = (uncommon_inventory_items[6][0] + ', ' +
                      uncommon_inventory_items[6][1] + ', ' +
                      uncommon_inventory_items[6][2] + ', ' +
                      uncommon_inventory_items[6][3] + ', ' +
                      uncommon_inventory_items[6][4] + '\n')
    print(unc_7_text)

unc_8_text = ''
def unc_8_func():
    global unc_8_var, uncommon_inventory_items, unc_8_text
    if unc_8_var.get() == 0:
        unc_8_text = ''
        print('yeet')
    elif unc_8_var.get() == 1:
        unc_8_text = (uncommon_inventory_items[7][0] + ', ' +
                      uncommon_inventory_items[7][1] + ', ' +
                      uncommon_inventory_items[7][2] + ', ' +
                      uncommon_inventory_items[7][3] + ', ' +
                      uncommon_inventory_items[7][4] + '\n')
    print(unc_8_text)

unc_9_text = ''
def unc_9_func():
    global unc_9_var, uncommon_inventory_items, unc_9_text
    if unc_9_var.get() == 0:
        unc_9_text = ''
        print('yeet')
    elif unc_9_var.get() == 1:
        unc_9_text = (uncommon_inventory_items[8][0] + ', ' +
                      uncommon_inventory_items[8][1] + ', ' +
                      uncommon_inventory_items[8][2] + ', ' +
                      uncommon_inventory_items[8][3] + ', ' +
                      uncommon_inventory_items[8][4] + '\n')
    print(unc_9_text)

unc_10_text = ''
def unc_10_func():
    global unc_10_var, uncommon_inventory_items, unc_10_text
    if unc_10_var.get() == 0:
        unc_10_text = ''
        print('yeet')
    elif unc_10_var.get() == 1:
        unc_10_text = (uncommon_inventory_items[9][0] + ', ' +
                      uncommon_inventory_items[9][1] + ', ' +
                      uncommon_inventory_items[9][2] + ', ' +
                      uncommon_inventory_items[9][3] + ', ' +
                      uncommon_inventory_items[9][4] + '\n')
    print(unc_10_text)

unc_11_text = ''
def unc_11_func():
    global unc_11_var, uncommon_inventory_items, unc_11_text
    if unc_11_var.get() == 0:
        unc_11_text = ''
        print('yeet')
    elif unc_11_var.get() == 1:
        unc_11_text = (uncommon_inventory_items[10][0] + ', ' +
                      uncommon_inventory_items[10][1] + ', ' +
                      uncommon_inventory_items[10][2] + ', ' +
                      uncommon_inventory_items[10][3] + ', ' +
                      uncommon_inventory_items[10][4] + '\n')
    print(unc_11_text)


#############################################################################
#                            rare item functions                            #
#############################################################################

rar_1_text = ''
def rar_1_func():
    global rar_1_var, rare_inventory_items, rar_1_text
    if rar_1_var.get() == 0:
        rar_1_text = ''
        print('yeet')
    elif rar_1_var.get() == 1:
        rar_1_text = (rare_inventory_items[0][0] + ', ' +
                      rare_inventory_items[0][1] + ', ' +
                      rare_inventory_items[0][2] + ', ' +
                      rare_inventory_items[0][3] + ', ' +
                      rare_inventory_items[0][4] + '\n')
    print(rar_1_text)

rar_2_text = ''
def rar_2_func():
    global rar_2_var, rare_inventory_items, rar_2_text
    if rar_2_var.get() == 0:
        rar_2_text = ''
        print('yeet')
    elif rar_2_var.get() == 1:
        rar_2_text = (rare_inventory_items[1][0] + ', ' +
                      rare_inventory_items[1][1] + ', ' +
                      rare_inventory_items[1][2] + ', ' +
                      rare_inventory_items[1][3] + ', ' +
                      rare_inventory_items[1][4] + '\n')
    print(rar_2_text)

rar_3_text = ''
def rar_3_func():
    global rar_3_var, rare_inventory_items, rar_3_text
    if rar_3_var.get() == 0:
        rar_3_text = ''
        print('yeet')
    elif rar_3_var.get() == 1:
        rar_3_text = (rare_inventory_items[2][0] + ', ' +
                      rare_inventory_items[2][1] + ', ' +
                      rare_inventory_items[2][2] + ', ' +
                      rare_inventory_items[2][3] + ', ' +
                      rare_inventory_items[2][4] + '\n')
    print(rar_3_text)

rar_4_text = ''
def rar_4_func():
    global rar_4_var, rare_inventory_items, rar_4_text
    if rar_4_var.get() == 0:
        rar_4_text = ''
        print('yeet')
    elif rar_4_var.get() == 1:
        rar_4_text = (rare_inventory_items[3][0] + ', ' +
                      rare_inventory_items[3][1] + ', ' +
                      rare_inventory_items[3][2] + ', ' +
                      rare_inventory_items[3][3] + ', ' +
                      rare_inventory_items[3][4] + '\n')
    print(rar_4_text)

rar_5_text = ''
def rar_5_func():
    global rar_5_var, rare_inventory_items, rar_5_text
    if rar_5_var.get() == 0:
        rar_5_text = ''
        print('yeet')
    elif rar_5_var.get() == 1:
        rar_5_text = (rare_inventory_items[4][0] + ', ' +
                      rare_inventory_items[4][1] + ', ' +
                      rare_inventory_items[4][2] + ', ' +
                      rare_inventory_items[4][3] + ', ' +
                      rare_inventory_items[4][4] + '\n')
    print(rar_5_text)


#############################################################################
#                        very_rare item functions                           #
#############################################################################

ver_1_text = ''
def ver_1_func():
    global ver_1_var, very_rare_inventory_items, ver_1_text
    if ver_1_var.get() == 0:
        ver_1_text = ''
        print('yeet')
    elif ver_1_var.get() == 1:
        ver_1_text = (very_rare_inventory_items[0][0] + ', ' +
                      very_rare_inventory_items[0][1] + ', ' +
                      very_rare_inventory_items[0][2] + ', ' +
                      very_rare_inventory_items[0][3] + ', ' +
                      very_rare_inventory_items[0][4] + '\n')
    print(ver_1_text)

ver_2_text = ''
def ver_2_func():
    global ver_2_var, very_rare_inventory_items, ver_2_text
    if ver_2_var.get() == 0:
        ver_2_text = ''
        print('yeet')
    elif ver_2_var.get() == 1:
        ver_2_text = (very_rare_inventory_items[1][0] + ', ' +
                      very_rare_inventory_items[1][1] + ', ' +
                      very_rare_inventory_items[1][2] + ', ' +
                      very_rare_inventory_items[1][3] + ', ' +
                      very_rare_inventory_items[1][4] + '\n')
    print(ver_2_text)

ver_3_text = ''
def ver_3_func():
    global ver_3_var, very_rare_inventory_items, ver_3_text
    if ver_3_var.get() == 0:
        ver_3_text = ''
        print('yeet')
    elif ver_3_var.get() == 1:
        ver_3_text = (very_rare_inventory_items[2][0] + ', ' +
                      very_rare_inventory_items[2][1] + ', ' +
                      very_rare_inventory_items[2][2] + ', ' +
                      very_rare_inventory_items[2][3] + ', ' +
                      very_rare_inventory_items[2][4] + '\n')
    print(ver_3_text)

ver_4_text = ''
def ver_4_func():
    global ver_4_var, very_rare_inventory_items, ver_4_text
    if ver_4_var.get() == 0:
        ver_4_text = ''
        print('yeet')
    elif ver_4_var.get() == 1:
        ver_4_text = (very_rare_inventory_items[3][0] + ', ' +
                      very_rare_inventory_items[3][1] + ', ' +
                      very_rare_inventory_items[3][2] + ', ' +
                      very_rare_inventory_items[3][3] + ', ' +
                      very_rare_inventory_items[3][4] + '\n')
    print(ver_4_text)

    
#############################################################################
#                         legendary item functions                          #
#############################################################################

leg_1_text = ''
def leg_1_func():
    global leg_1_var, legendary_inventory_items, leg_1_text
    if leg_1_var.get() == 0:
        leg_1_text = ''
        print('yeet')
    elif leg_1_var.get() == 1:
        leg_1_text = (legendary_inventory_items[0][0] + ', ' +
                      legendary_inventory_items[0][1] + ', ' +
                      legendary_inventory_items[0][2] + ', ' +
                      legendary_inventory_items[0][3] + ', ' +
                      legendary_inventory_items[0][4] + '\n')
    print(leg_1_text)

leg_2_text = ''
def leg_2_func():
    global leg_2_var, legendary_inventory_items, leg_2_text
    if leg_2_var.get() == 0:
        leg_2_text = ''
        print('yeet')
    elif leg_2_var.get() == 1:
        leg_2_text = (legendary_inventory_items[1][0] + ', ' +
                      legendary_inventory_items[1][1] + ', ' +
                      legendary_inventory_items[1][2] + ', ' +
                      legendary_inventory_items[1][3] + ', ' +
                      legendary_inventory_items[1][4] + '\n')
    print(leg_2_text)


#############################################################################
#                              orb functions                                #
#############################################################################

orb_text = ''
def orb_func():
    global lorb_var, orb_info, orb_text
    if orb_var.get() == 0:
        orb_text = ''
        print('yeet')
    elif orb_var.get() == 1:
        orb_text = (orb_info[0] + ', ' + orb_info[1] + ', ' +
                    orb_info[2] + ', ' + orb_info[3] + ', ' +
                    orb_info[4] + '\n')
    print(orb_text)

    
#############################################################################
#                        create the inventory window                        #
#############################################################################

def inventory_functions():
    global commands_label

    print_selected = Button(commands_label, text = 'Save Receipt',
                            font = ('Arial', 14), width = 16,
                            command = print_selected_func, cursor = 'hand2')
    print_inventory = Button(commands_label, text = 'Upload Inventory',
                             font = ('Arial', 14), width = 16,
                             command = print_inventory_func, cursor = 'hand2')
    restock = Button(commands_label, text = 'Restock', font = ('Arial', 14),
                     width = 16, command = restock_func, cursor = 'hand2')
    close_inventory = Button(commands_label, text = 'Close',
                             font = ('Arial', 14), width = 16,
                             command = close_inventory_func, cursor = 'hand2')

    print_selected.grid(row = 0, column = 0, padx = 3, pady = 3)
    print_inventory.grid(row = 1, column = 0, padx = 3, pady = 3)
    restock.grid(row = 0, column = 1, padx = 3, pady = 3)
    close_inventory.grid(row = 1, column = 1, padx = 3, pady = 3)

def common_inventory():
    global common_inventory_items, common_label
    global com_1_var, com_2_var, com_3_var, com_4_var, com_5_var, com_6_var
    global com_7_var, com_8_var, com_9_var
    labels = ['common_1', 'common_2', 'common_3', 'common_4', 'common_5',
              'common_6', 'common_7', 'common_8', 'common_9']
    common_inventory_items = []
    num_items = 9
    for label in range(num_items):
        item = randint(0, (len(common_items) - 1))
        
        item_labels = [labels[label] + 'name', labels[label] + 'source',
                       labels[label] + 'type', labels[label] + 'attune',
                       labels[label] + 'price']

        item_labels[0] = Label(common_label, text = common_items[item][0],
                               font = ('Arial', 12)).grid(row = label,
                                                          column = 1, padx = 3,
                                                          pady = 3,
                                                          sticky = 'w')

        item_labels[1] = Label(common_label, text = common_items[item][1],
                               font = ('Arial', 12)).grid(row = label,
                                                          column = 2, padx = 3,
                                                          pady = 3,
                                                          sticky = 'w')

        item_labels[2] = Label(common_label, text = common_items[item][2],
                               font = ('Arial', 12)).grid(row = label,
                                                          column = 3, padx = 3,
                                                          pady = 3,
                                                          sticky = 'w')

        item_labels[3] = Label(common_label, text = common_items[item][3],
                               font = ('Arial', 12)).grid(row = label,
                                                          column = 4, padx = 3,
                                                          pady = 3,
                                                          sticky = 'w')

        item_labels[4] = Label(common_label, text = common_items[item][4],
                               font = ('Arial', 12)).grid(row = label,
                                                          column = 5, padx = 3,
                                                          pady = 3,
                                                          sticky = 'w')
        
        common_inventory_items.append(common_items[item])

    com_1_var = IntVar()
    com_check_1 = Checkbutton(common_label, variable = com_1_var,
                              command = com_1_func).grid(row = 0, column = 0,
                                                         padx = 3, pady = 3)

    com_2_var = IntVar()
    com_check_2 = Checkbutton(common_label, variable = com_2_var,
                              command = com_2_func).grid(row = 1, column = 0,
                                                         padx = 3, pady = 3)

    com_3_var = IntVar()
    com_check_3 = Checkbutton(common_label, variable = com_3_var,
                              command = com_3_func).grid(row = 2, column = 0,
                                                         padx = 3, pady = 3)

    com_4_var = IntVar()
    com_check_4 = Checkbutton(common_label, variable = com_4_var,
                              command = com_4_func).grid(row = 3, column = 0,
                                                         padx = 3, pady = 3)

    com_5_var = IntVar()
    com_check_5 = Checkbutton(common_label, variable = com_5_var,
                              command = com_5_func).grid(row = 4, column = 0,
                                                         padx = 3, pady = 3)

    com_6_var = IntVar()
    com_check_6 = Checkbutton(common_label, variable = com_6_var,
                              command = com_6_func).grid(row = 5, column = 0,
                                                         padx = 3, pady = 3)

    com_7_var = IntVar()
    com_check_7 = Checkbutton(common_label, variable = com_7_var,
                              command = com_7_func).grid(row = 6, column = 0,
                                                         padx = 3, pady = 3)

    com_8_var = IntVar()
    com_check_8 = Checkbutton(common_label, variable = com_8_var,
                              command = com_8_func).grid(row = 7, column = 0,
                                                         padx = 3, pady = 3)

    com_9_var = IntVar()
    com_check_9 = Checkbutton(common_label, variable = com_9_var,
                              command = com_9_func).grid(row = 8, column = 0,
                                                         padx = 3, pady = 3)

def uncommon_inventory():
    global uncommon_inventory_items, uncommon_label
    global unc_1_var, unc_2_var, unc_3_var, unc_4_var, unc_5_var, unc_6_var
    global unc_7_var, unc_8_var, unc_9_var, unc_10_var, unc_11_var
    labels = ['uncommon_1', 'uncommon_2', 'uncommon_3', 'uncommon_4',
              'uncommon_5', 'uncommon_6', 'uncommon_7', 'uncommon_8',
              'uncommon_9', 'uncommon_10', 'uncommon_11']
    uncommon_inventory_items = []
    num_items = 11
    for label in range(num_items):
        
        item = randint(0, (len(uncommon_items) - 1))
        
        item_labels = [labels[label] + 'name', labels[label] + 'source',
                       labels[label] + 'type', labels[label] + 'attune',
                       labels[label] + 'price']
        
        item_labels[0] = Label(uncommon_label, text = uncommon_items[item][0],
                               font = ('Arial', 12)).grid(row = label,
                                                          column = 1, padx = 3,
                                                          pady = 3,
                                                          sticky = 'w')
        item_labels[1] = Label(uncommon_label, text = uncommon_items[item][1],
                               font = ('Arial', 12)).grid(row = label,
                                                          column = 2, padx = 3,
                                                          pady = 3,
                                                          sticky = 'w')
        item_labels[2] = Label(uncommon_label, text = uncommon_items[item][2],
                               font = ('Arial', 12)).grid(row = label,
                                                          column = 3, padx = 3,
                                                          pady = 3,
                                                          sticky = 'w')
        item_labels[3] = Label(uncommon_label, text = uncommon_items[item][3],
                               font = ('Arial', 12)).grid(row = label,
                                                          column = 4, padx = 3,
                                                          pady = 3,
                                                          sticky = 'w')
        item_labels[4] = Label(uncommon_label, text = uncommon_items[item][4],
                               font = ('Arial', 12)).grid(row = label,
                                                          column = 5, padx = 3,
                                                          pady = 3,
                                                          sticky = 'w')
        
        uncommon_inventory_items.append(uncommon_items[item])

    unc_1_var = IntVar()
    unc_check_1 = Checkbutton(uncommon_label, variable = unc_1_var,
                              command = unc_1_func).grid(row = 0, column = 0,
                                                         padx = 3, pady = 3)

    unc_2_var = IntVar()
    unc_check_2 = Checkbutton(uncommon_label, variable = unc_2_var,
                              command = unc_2_func).grid(row = 1, column = 0,
                                                         padx = 3, pady = 3)

    unc_3_var = IntVar()
    unc_check_3 = Checkbutton(uncommon_label, variable = unc_3_var,
                              command = unc_3_func).grid(row = 2, column = 0,
                                                         padx = 3, pady = 3)

    unc_4_var = IntVar()
    unc_check_4 = Checkbutton(uncommon_label, variable = unc_4_var,
                              command = unc_4_func).grid(row = 3, column = 0,
                                                         padx = 3, pady = 3)

    unc_5_var = IntVar()
    unc_check_5 = Checkbutton(uncommon_label, variable = unc_5_var,
                              command = unc_5_func).grid(row = 4, column = 0,
                                                         padx = 3, pady = 3)

    unc_6_var = IntVar()
    unc_check_6 = Checkbutton(uncommon_label, variable = unc_6_var,
                              command = unc_6_func).grid(row = 5, column = 0,
                                                         padx = 3, pady = 3)

    unc_7_var = IntVar()
    unc_check_7 = Checkbutton(uncommon_label, variable = unc_7_var,
                              command = unc_7_func).grid(row = 6, column = 0,
                                                         padx = 3, pady = 3)

    unc_8_var = IntVar()
    unc_check_8 = Checkbutton(uncommon_label, variable = unc_8_var,
                              command = unc_8_func).grid(row = 7, column = 0,
                                                         padx = 3, pady = 3)

    unc_9_var = IntVar()
    unc_check_9 = Checkbutton(uncommon_label, variable = unc_9_var,
                              command = unc_9_func).grid(row = 8, column = 0,
                                                         padx = 3, pady = 3)

    unc_10_var = IntVar()
    unc_check_10 = Checkbutton(uncommon_label, variable = unc_10_var,
                              command = unc_10_func).grid(row = 9, column = 0,
                                                         padx = 3, pady = 3)

    unc_11_var = IntVar()
    unc_check_11 = Checkbutton(uncommon_label, variable = unc_11_var,
                              command = unc_11_func).grid(row = 10, column = 0,
                                                         padx = 3, pady = 3)

def rare_inventory():
    global rare_inventory_items, rare_label
    global rar_1_var, rar_2_var, rar_3_var, rar_4_var, rar_5_var
    labels = ['rare_1', 'rare_2', 'rare_3', 'rare_4', 'rare_5']
    rare_inventory_items = []
    num_items = 5
    for label in range(num_items):
        item = randint(0, (len(rare_items) - 1))

        item_labels = [labels[label] + 'name', labels[label] + 'source',
                       labels[label] + 'type', labels[label] + 'attune',
                       labels[label] + 'price']

        item_labels[0] = Label(rare_label, text = rare_items[item][0],
                               font = ('Arial', 12)).grid(row = label,
                                                          column = 1, padx = 3,
                                                          pady = 3,
                                                          sticky = 'w')

        item_labels[1] = Label(rare_label, text = rare_items[item][1],
                               font = ('Arial', 12)).grid(row = label,
                                                          column = 2, padx = 3,
                                                          pady = 3,
                                                          sticky = 'w')

        item_labels[2] = Label(rare_label, text = rare_items[item][2],
                               font = ('Arial', 12)).grid(row = label,
                                                          column = 3, padx = 3,
                                                          pady = 3,
                                                          sticky = 'w')

        item_labels[3] = Label(rare_label, text = rare_items[item][3],
                               font = ('Arial', 12)).grid(row = label,
                                                          column = 4, padx = 3,
                                                          pady = 3,
                                                          sticky = 'w')

        item_labels[4] = Label(rare_label, text = rare_items[item][4],
                               font = ('Arial', 12)).grid(row = label,
                                                          column = 5, padx = 3,
                                                          pady = 3,
                                                          sticky = 'w')
        
        rare_inventory_items.append(rare_items[item])

    rar_1_var = IntVar()
    rar_check_1 = Checkbutton(rare_label, variable = rar_1_var,
                              command = rar_1_func).grid(row = 0, column = 0,
                                                         padx = 3, pady = 3)

    rar_2_var = IntVar()
    rar_check_1 = Checkbutton(rare_label, variable = rar_2_var,
                              command = rar_2_func).grid(row = 1, column = 0,
                                                         padx = 3, pady = 3)

    rar_3_var = IntVar()
    rar_check_3 = Checkbutton(rare_label, variable = rar_3_var,
                              command = rar_3_func).grid(row = 2, column = 0,
                                                         padx = 3, pady = 3)

    rar_4_var = IntVar()
    rar_check_4 = Checkbutton(rare_label, variable = rar_4_var,
                              command = rar_4_func).grid(row = 3, column = 0,
                                                         padx = 3, pady = 3)

    rar_5_var = IntVar()
    rar_check_5 = Checkbutton(rare_label, variable = rar_5_var,
                              command = rar_5_func).grid(row = 4, column = 0,
                                                         padx = 3, pady = 3)

def very_rare_inventory():
    global very_rare_inventory_items, very_rare_label
    global ver_1_var, ver_2_var, ver_3_var, ver_4_var
    labels = ['very_rare_1', 'very_rare_2', 'very_rare_3', 'very_rare_4']
    very_rare_inventory_items = []
    num_items = 4
    for label in range(num_items):
        item = randint(0, (len(very_rare_items) - 1))

        item_labels = [labels[label] + 'name', labels[label] + 'source',
                       labels[label] + 'type', labels[label] + 'attune',
                       labels[label] + 'price']

        item_labels[0] = Label(very_rare_label, text = very_rare_items[item][0],
                               font = ('Arial', 12)).grid(row = label,
                                                          column = 1, padx = 3,
                                                          pady = 3,
                                                          sticky = 'w')

        item_labels[1] = Label(very_rare_label, text = very_rare_items[item][1],
                               font = ('Arial', 12)).grid(row = label,
                                                          column = 2, padx = 3,
                                                          pady = 3,
                                                          sticky = 'w')

        item_labels[2] = Label(very_rare_label, text = very_rare_items[item][2],
                               font = ('Arial', 12)).grid(row = label,
                                                          column = 3, padx = 3,
                                                          pady = 3,
                                                          sticky = 'w')

        item_labels[3] = Label(very_rare_label, text = very_rare_items[item][3],
                               font = ('Arial', 12)).grid(row = label,
                                                          column = 4, padx = 3,
                                                          pady = 3,
                                                          sticky = 'w')

        item_labels[4] = Label(very_rare_label, text = very_rare_items[item][4],
                               font = ('Arial', 12)).grid(row = label,
                                                          column = 5, padx = 3,
                                                          pady = 3,
                                                          sticky = 'w')
        
        very_rare_inventory_items.append(very_rare_items[item])

    ver_1_var = IntVar()
    ver_check_1 = Checkbutton(very_rare_label, variable = ver_1_var,
                              command = ver_1_func).grid(row = 0, column = 0,
                                                         padx = 3, pady = 3)

    ver_2_var = IntVar()
    ver_check_1 = Checkbutton(very_rare_label, variable = ver_2_var,
                              command = ver_2_func).grid(row = 1, column = 0,
                                                         padx = 3, pady = 3)

    ver_3_var = IntVar()
    ver_check_3 = Checkbutton(very_rare_label, variable = ver_3_var,
                              command = ver_3_func).grid(row = 2, column = 0,
                                                         padx = 3, pady = 3)

    ver_4_var = IntVar()
    ver_check_4 = Checkbutton(very_rare_label, variable = ver_4_var,
                              command = ver_4_func).grid(row = 3, column = 0,
                                                         padx = 3, pady = 3)

def legendary_inventory():
    global legendary_inventory_items, legendary_label, leg_1_var, leg_2_var
    labels = ['legendary_1', 'legendary_2']
    legendary_inventory_items = []
    num_items = 2
    for label in range(num_items):
        item = randint(0, (len(legendary_items) - 1))
        
        item_labels = [labels[label] + 'name', labels[label] + 'source',
                       labels[label] + 'type', labels[label] + 'attune',
                       labels[label] + 'price']

        item_labels[0] = Label(legendary_label, text = legendary_items[item][0],
                               font = ('Arial', 12)).grid(row = label,
                                                          column = 1, padx = 3,
                                                          pady = 3,
                                                          sticky = 'w')

        item_labels[1] = Label(legendary_label, text = legendary_items[item][1],
                               font = ('Arial', 12)).grid(row = label,
                                                          column = 2, padx = 3,
                                                          pady = 3,
                                                          sticky = 'w')

        item_labels[2] = Label(legendary_label, text = legendary_items[item][2],
                               font = ('Arial', 12)).grid(row = label,
                                                          column = 3, padx = 3,
                                                          pady = 3,
                                                          sticky = 'w')

        item_labels[3] = Label(legendary_label, text = legendary_items[item][3],
                               font = ('Arial', 12)).grid(row = label,
                                                          column = 4, padx = 3,
                                                          pady = 3,
                                                          sticky = 'w')

        item_labels[4] = Label(legendary_label, text = legendary_items[item][4],
                               font = ('Arial', 12)).grid(row = label,
                                                          column = 5, padx = 3,
                                                          pady = 3,
                                                          sticky = 'w')
               
        legendary_inventory_items.append(legendary_items[item])
        
    leg_1_var = IntVar()
    leg_check_1 = Checkbutton(legendary_label, variable = leg_1_var,
                              command = leg_1_func).grid(row = 0, column = 0,
                                                         padx = 3, pady = 3)

    leg_2_var = IntVar()
    leg_check_2 = Checkbutton(legendary_label, variable = leg_2_var,
                              command = leg_2_func).grid(row = 1, column = 0,
                                                         padx = 3, pady = 3)

def orb_inventory():
    global orb_label, orb_info, orb_var
    orb_info = ['Gold Orb of Dragonkind', 'DMG', 'Wondrous Item', 'Yes',
                '1000000 gp']

    orb_name = Label(orb_label, text = orb_info[0], font = ('Arial', 12)).grid(
        row = 0, column = 1, padx = 3, pady = 3, sticky = 'w')

    orb_source = Label(orb_label, text = orb_info[1], font = ('Arial', 12)).grid(
        row = 0, column = 2, padx = 3, pady = 3, sticky = 'w')

    orb_type = Label(orb_label, text = orb_info[2], font = ('Arial', 12)).grid(
        row = 0, column = 3, padx = 3, pady = 3, sticky = 'w')

    orb_attune = Label(orb_label, text = orb_info[3], font = ('Arial', 12)).grid(
        row = 0, column = 4, padx = 3, pady = 3, sticky = 'w')

    orb_price = Label(orb_label, text = orb_info[4], font = ('Arial', 12)).grid(
        row = 0, column = 5, padx = 3, pady = 3, sticky = 'w')

    orb_var = IntVar()
    orb_check = Checkbutton(orb_label, variable = orb_var, command = orb_func
                            ).grid(row = 0, column = 0, padx = 3, pady = 3)

def inventory_items():
    common_inventory()
    uncommon_inventory()
    rare_inventory()
    very_rare_inventory()
    legendary_inventory()
    orb_inventory()

def inventory_window_create():
    global common_label, uncommon_label, rare_label, very_rare_label
    global legendary_label, orb_label, commands_label, inventory
    inventory = Toplevel()

    inventory.title("Balthazar's Magical House for Witches and Wizards")

    common_label = LabelFrame(inventory, text = 'Common Items',
                              font = ('Arial', 12))
    uncommon_label = LabelFrame(inventory, text = 'Uncommon Items',
                              font = ('Arial', 12))
    rare_label = LabelFrame(inventory, text = 'Rare Items',
                              font = ('Arial', 12))
    very_rare_label = LabelFrame(inventory, text = 'Very Rare Items',
                              font = ('Arial', 12))
    legendary_label = LabelFrame(inventory, text = 'Legendary Items',
                              font = ('Arial', 12))
    orb_label = LabelFrame(inventory, text = '$$ Orb of Dragonkind $$',
                           font = ('Arial', 12))
    commands_label = LabelFrame(inventory, text = 'Commands',
                                font = ('Arial', 12))

    common_label.grid(row = 0, column = 0, padx = 3, pady = 3, sticky = 'nw')
    uncommon_label.grid(row = 0, column = 1, padx = 3, pady = 3, sticky = 'nw')
    rare_label.grid(row = 1, column = 0, padx = 3, pady = 3, sticky = 'nw')
    very_rare_label.grid(row = 1, column = 1, padx = 3, pady = 3, sticky = 'nw')
    legendary_label.grid(row = 2, column = 0, padx = 3, pady = 3, sticky = 'nw')
    orb_label.grid(row = 3, column = 0, padx = 3, pady = 3, sticky = 'nw')
    commands_label.grid(row = 2, column = 1, padx = 3, pady = 3, rowspan = 2,
                        sticky = 'nw')

    inventory_items()
    inventory_functions()
    
    inventory.mainloop()


#############################################################################
#                           activates the store                             #
#############################################################################

def store_activate():
    global login, generate, create_user, password_text, user_text, sign_in

    #decrypting
    system ('gpg --batch --passphrase="Appl3M3Th1s" --pinentry-mode loopback -o Passwords.txt -d Passwords.txt.gpg')
    system ('rm Passwords.txt.gpg')
    
    passwords_file = open('Passwords.txt', 'r')
    passwords = passwords_file.read()
    passwords_file.close()

    #encrypting
    system ('gpg -e -r Daniel Passwords.txt')
    system ('rm Passwords.txt')

    passwords_list = findall('(.+), (.+).', passwords)

    passwords = []

    attempts = []

    sign_in['bg'] = 'lightgrey'
        
    for counter in range(len(passwords_list)):
            try:
                    user = passwords_list[counter].index(user_text.get())
                    assert user == 0
                    attempts.append('success')
                    success_point = counter
            except ValueError:
                    attempts.append('error')
            except AssertionError:
                    attempts.append('error')
    try:
            attempts.index('success')
            if password_text.get() == passwords_list[success_point][1]:
                    login.destroy()
                    generate['state'] = NORMAL
                    create_user['state'] = NORMAL
                    close_program['state'] = NORMAL
            else:
                    sign_in['bg'] = 'orangered'
                    password_text.delete(0, END)
    except ValueError:
            sign_in['bg'] = 'orangered'
            user_text.delete(0, END)
            password_text.delete(0, END)

    passwords_list = []


#############################################################################
#                        create the tkinter login window                    #
#############################################################################

def login_create():
    global login, user_text, password_text, sign_in
    login = Toplevel()

    login.title("Balthazar's Magical House for Witches and Wizards")

    user_label = Label(login, text = 'Username:', font = ('Arial', 14))
    user_text = Entry(login, font = ('Arial', 14), width = 12)

    password_label = Label(login, text = 'Password:', font = ('Arial', 14))
    password_text = Entry(login, font = ('Arial', 14), width = 12, show = '*')

    sign_in = Button(login, text = 'Sign In', font = ('Arial', 14),
                     cursor = 'hand2', command = store_activate,
                     bg = 'lightgrey')

    user_label.grid(row = 1, column = 1, padx = 3, sticky = 'w')
    user_text.grid(row = 2, column = 1, padx = 3)
    password_label.grid(row = 3, column = 1, padx = 3, sticky = 'w')
    password_text.grid(row = 4, column = 1, padx = 3)
    sign_in.grid(row = 5, column = 1, padx = 3, pady = 3)

    login.mainloop()


#############################################################################
#                       function to close the program                       #
#############################################################################

def close_program_func():
    global store

    store.destroy()


#############################################################################
#                            create user function                           #
#############################################################################

def create_user_func():

    global create_password_text1, create_password_text2, create_user_text
    global create_user_button, create_user_window

    #decrypting
    system ('gpg --batch --passphrase="Appl3M3Th1s" --pinentry-mode loopback -o Passwords.txt -d Passwords.txt.gpg')
    system ('rm Passwords.txt.gpg')
    
    passwords_file = open('Passwords.txt', 'r')
    passwords = passwords_file.read()
    passwords_file.close()

    #encrypting
    system ('gpg -e -r Daniel Passwords.txt')
    system ('rm Passwords.txt')

    passwords_list = findall('(.+), (.+).', passwords)

    passwords = []

    attempts = []

    create_user_button['bg'] = 'lightgrey'

    enter_user = create_user_text.get()
    password1 = create_password_text1.get()
    password2 = create_password_text2.get()
        
    for counter in range(len(passwords_list)):
            try:
                    user = passwords_list[counter].index(enter_user)
                    assert user == 0
                    attempts.append('in_use')
            except ValueError:
                    attempts.append('not_used')
            except AssertionError:
                    attempts.append('not_used')
    try:
            attempts.index('in_use')
            create_user_button['bg'] = 'orangered'
            create_user_text.delete(0, END)
            create_password_text1.delete(0, END)
            create_password_text2.delete(0, END)
    except ValueError:
            if password1 != password2:
                    create_user_button['bg'] = 'orangered'
                    create_password_text1.delete(0, END)
                    create_password_text2.delete(0, END)
            else:
                    ######decryption######
                    system ('gpg --batch --passphrase="Appl3M3Th1s" --pinentry-mode loopback -o Passwords.txt -d Passwords.txt.gpg')
                    system ('rm Passwords.txt.gpg')
                
                    passwords_file = open('Passwords.txt', 'r')
                    passwords = passwords_file.read()
                    passwords_file.close()
                    passwords_file = open('Passwords.txt', 'w')
                    passwords_file.write(str(passwords) + '\n' +
                                         enter_user + ', ' +
                                         password1 + '.')
                    passwords_file.close()

                    ######encryption######
                    system ('gpg -e -r Daniel Passwords.txt')
                    system ('rm Passwords.txt') 

                    passwords = []
                    
                    create_user_window.destroy()


#############################################################################
#                             create user window                            #
#############################################################################

def create_user_window_create():
    global create_user_text, create_password_text1, create_password_text2
    global create_user_button, create_user_window

    create_user_window = Toplevel()

    create_user_window.title("Balthazar's Magical House for Witches and Wizards")

    create_user_label = Label(create_user_window, text = 'Username:',
                              font = ('Arial', 14))
    create_user_text = Entry(create_user_window, font = ('Arial', 14),
                             width = 12)

    create_password_label = Label(create_user_window,
                                  text = 'Password (enter twice):',
                                  font = ('Arial', 14))
    create_password_text1 = Entry(create_user_window, font = ('Arial', 14),
                                  width = 12, show = '*')
    create_password_text2 = Entry(create_user_window, font = ('Arial', 14),
                                  width = 12, show = '*')

    create_user_button = Button(create_user_window, text = 'Create User', font = ('Arial', 14),
                         cursor = 'hand2', command = create_user_func,
                         bg = 'lightgrey')

    create_user_label.grid(row = 1, column = 1, padx = 3, sticky = 'w')
    create_user_text.grid(row = 2, column = 1, padx = 3, sticky = 'w')
    create_password_label.grid(row = 3, column = 1, padx = 3, sticky = 'w')
    create_password_text1.grid(row = 4, column = 1, padx = 3, sticky = 'w')
    create_password_text2.grid(row = 5, column = 1, padx = 3, sticky = 'w')
    create_user_button.grid(row = 6, column = 1, padx = 3, pady = 3)

    create_user_window.mainloop()
    

#############################################################################
#                         create the generate window                        #
#############################################################################

store = Tk()

store.title("Balthazar's Magical House for Witches and Wizards")

generate = Button(store, text = 'Generate Store', width = 14,
              font = ('Arial', 14), cursor = 'hand2',
              command = inventory_window_create, state = DISABLED)

create_user = Button(store, text = 'Create User', font = ('Arial', 14),
                     cursor = 'hand2', state = DISABLED, width = 14,
                     command = create_user_window_create)

close_program = Button(store, text = 'Close', font = ('Arial', 14),
                       cursor = 'hand2', state = DISABLED, width = 14,
                       command = close_program_func)

generate.grid(row = 1, column = 0, padx = 3, pady = 3)
create_user.grid(row = 2, column = 0, padx = 3, pady = 3)
close_program.grid(row = 3, column = 0, padx = 3, pady = 3)

login_create()
store.mainloop()
