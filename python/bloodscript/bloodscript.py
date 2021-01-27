#import turtle graphics library
from turtle import *

#import math
from math import *

#draw to function
#   draws line to a coordinate

def side_length(x1, y1, x2, y2):
    u = 0 #smaller variable
    v = 0 #bigger variable
    x_length = 0 #the x length
    y_length = 0 #the y length

    #find length of side
    if x1 < x2: #x2 is the big boy
        v = x2 
        u = x1
    else: #x1 is big boy
        v = x1
        u = x2

    x_length = v - u

    if y1 < y2: #y2 is the big boy
        v = y2 
        u = y1
    else: #y1 is big boy
        v = y1
        u = y2

    y_length = v - u

    length = sqrt(x_length ** 2 + y_length ** 2)

    return length

#math function for determining the lication of the u and e lines
def calculate_angle(x1, y1, x2, y2, x3, y3):
    a = side_length(x1, y1, x2, y2)
    b = side_length(x1, y1, x3, y3)
    c = side_length(x2, y2, x3, y3)
    
    angle = degrees(acos((a ** 2 + b ** 2 - c ** 2)/(2 * a * b)))

    return angle

#get word
def get_word():
    word = input('all lower caes, and only won ward: ')
    return word

#check for and get letter co-ords
def check_letter(word, letter, unit):
    global x, y
    if letter == 'h':
        if unit > 0: #if not the first letter
            if word[unit - 1] != 'c' and word[unit - 1] != 's': #if the previous letter wasn't a c or s
                print(letter)
        else:
            print(letter)
    elif letter == 'c' or letter == 's': #if c or s
        try:
            if word[unit + 1] == 'h': #if next letter is h
                print(letter + 'h')
            else:
                print(letter)
        except IndexError: #happens when its the last letter
            print(letter)
    else: #prints the letter as normal
        print(letter)
    
    if letter == 'a':
        x = -100
        y = 0
    elif letter == 'b':
        x = -20
        y = 100
    elif letter == 'c':
        try:
            if word[unit + 1] == 'h': #if next letter is h
                x = 100
                y = 100
            else: #just c and not ch
                x = 100
                y = 100
        except IndexError: #just c is last letter
            x = 100
            y = 100
    elif letter == 'd':
        x = 50
        y = 20
    elif letter == 'e':
        x = -20
        y = 50
    elif letter == 'f':
        x = 0
        y = 0
    elif letter == 'g':
        x = 20
        y = -100
    elif letter == 'h':
        if unit > 0: #if not the first letter
            if word[unit - 1] != 'c' and word[unit - 1] != 's': #if previous letter wasn't c or s
                x = 100
                y = -100
        else: #if first letter
            x = 100
            y = -100
    elif letter == 'i':
        x = -20
        y = 50
    elif letter == 'j':
        x = -100
        y = 100
    elif letter == 'k':
        x = -20
        y = -100
    elif letter == 'l':
        x = 100
        y = 20
    elif letter == 'm':
        x = 20
        y = -50
    elif letter == 'n':
        x = -20
        y = -50
    elif letter == 'o':
        x = 20
        y = 50
    elif letter == 'p':
        x = 20
        y = 100
    elif letter == 'q':
        x = -20
        y = -100
    elif letter == 'r':
        x = 100
        y = -20
    elif letter == 's':
        try:
            if word[unit + 1] == 'h': #if sh
                x = -100
                y = -100
            else: #if s
                x = -50
                y = 20
        except IndexError: #if regular s and last letter
            x = -50
            y = 20
    elif letter == 't':
        x = 50
        y = -20
    elif letter == 'u':
        x = 20
        y = 50
    elif letter == 'v':
        x = 100
        y = 0
    elif letter == 'w':
        x = -100
        y = -20
    elif letter == 'x':
        x = -100
        y = -100
    elif letter == 'y':
        x = -100
        y = 20
    elif letter == 'z':
        x = -50
        y = -20
    else:
        print('hyey nerd dat is not a letter grrr')

#setup the canvis
def setup_canvis():
    setup(300, 300)
    penup()
    pencolor('black')
    width(4)
    hideturtle()

    penup()
    goto(-140, 0)
    pendown()
    goto(140, 0)
    penup()
    goto(0, 100)
    pendown()
    goto(0, -100)
    penup()

#reset the cavis if they want to enter a new word
def reset_canvis():
    global word
    reset()
    word = get_word()

    penup()
    pencolor('black')
    width(4)
    hideturtle()

    penup()
    goto(-140, 0)
    pendown()
    goto(140, 0)
    penup()
    goto(0, 100)
    pendown()
    goto(0, -100)
    penup()

#processes
def processes():
    global x, y, word
    print('heilo, moi name is Dmitri and iom your male order bride, Gimme youre social security number')
    word = get_word()

    setup_canvis()

    i = 1
    while i == 1:
        unit = 0
        x = 0
        y = 0
        for letter in word:
            check_letter(word, letter, unit)
            print(x)
            print(y)
            pendown()
            goto(x, y)
            #if letter u or i
            #   rotate to fit angle and draw line
            penup()
            unit = unit + 1

        r = input('To enter a new word press 1. To exit, close the drawing window: ')

        if r == '1':
            reset_canvis()
            
        else:
            break

#main code
processes()

done()