#TKinter GUI for BloodScript

#Import Tkinter library
from tkinter import Tk, Text, Button, Entry, END, DISABLED, NORMAL

#Import Turtle Graphics library
from turtle import *

#create window
window = Tk()
window.title('Bloodscript')

#######################################################################
#                            Functionality                            #
#######################################################################

#setup the canvis
def setup_canvis():
    setup(300, 300)
    penup()
    pencolor('black')
    width(4)
    hideturtle()

    penup()
    goto(-100, 0)
    pendown()
    goto(100, 0)
    penup()
    goto(0, 100)
    pendown()
    goto(0, -100)
    penup()

#reset the cavis if they want to enter a new word
def reset_canvis():
    global display_box, word_box
    display_box.delete(1.0, END)
    word_box.delete(0, END)
    reset()
    hideturtle()

#check for and get letter co-ords
def check_letter(word, letter, unit):
    global x, y, display_box
    if letter == 'h':
        if unit > 0: #if not the first letter
            if word[unit - 1] != 'c' and word[unit - 1] != 's': #if the previous letter wasn't a c or s
                display_box.insert(END, '\n' + letter)
        else:
            display_box.insert(END, '\n' + letter)
    elif letter == 'c' or letter == 's': #if c or s
        try:
            if word[unit + 1] == 'h': #if next letter is h
                display_box.insert(END, '\n' + letter + 'h')
            else:
                display_box.insert(END, '\n' + letter)
        except IndexError: #happens when its the last letter
            display_box.insert(END, '\n' + letter)
    else: #prints the letter as normal
        display_box.insert(END, '\n' + letter)
    
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
    elif letter == '.':
        x = 0
        y = 100
    else:
        display_box.insert(END, '\n hyey nerd dat is not a letter grrr')

#processes
def processes():
    global x, y, word, word_box, ref_button
    
    ref_button['state'] = NORMAL

    word = word_box.get()

    setup_canvis()

    unit = 0
    x = 0
    y = 0
    for letter in word:
        check_letter(word, letter, unit)
        
        display_box.insert(END, '\n' + str(x))
        display_box.insert(END, '\n' + str(y))
        pendown()
        goto(x, y)
        penup()
        unit = unit + 1

#close the windows
def close_all():
    bye()
    window.destroy()

#######################################################################
#                               Widgets                               #
#######################################################################

#word entry box
word_box = Entry(window, width = 15, font = ('Arial', 14), borderwidth = 2)

#display box
display_box = Text(window, width = 15, height = 15, 
                   font = ('Arial', 14), borderwidth = 2)

#Translate button
trans_button = Button(window, text = 'Translate', font = ('Arial', 14), 
                      bg = 'lawn green', fg = 'black', cursor = 'hand2',
                      command= processes)

#refresh button
ref_button = Button(window, text = 'Refresh', font = ('Arial', 14), 
                    bg = 'red', fg = 'white', cursor = 'hand2', 
                    command = reset_canvis, state = DISABLED)

#close button
close_button = Button(window, text = 'Close', font = ('Arial', 14),
                      command = close_all, cursor = 'hand2')

#place in window
margin_x = 5
margin_y = 4
word_box.grid(row = 0, column = 0, columnspan = 2, padx = margin_x, pady = margin_y)
trans_button.grid(row = 1, column = 0, padx = margin_x, pady = margin_y)
ref_button.grid(row = 1, column = 1, padx = margin_x, pady = margin_y)
display_box.grid(row = 2, column = 0, columnspan = 2, padx = margin_x, pady = margin_y)
close_button.grid(row = 3, column = 0, columnspan = 2, padx = margin_x, pady = margin_y)

word_box.delete(0, END)
word_box.insert(0, "word")

#start mainloop
window.mainloop()