# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 08:15:57 2019

@author: Travis
"""

import numpy as np
import pandas as pd

from tkinter import *
import os

placeholder_text = " "*28
mainFont = ("Times New Roman", "12", "bold")
subFont = ("Helvetica","12")


def gen_randint(number=1,minim=1,maxum=10,rep=True,return_dummy=False):
    '''Generates 'number' amount of random integers between the values of 'minim' and 'maxum'; these default to 1, 1, and 10 
    respectively. By default, repetition is accepted, but one can specify to return only unique integers by changing 'rep'. If 
    returning unique integers, one can indicated if they want to also return the actual list of generated integers that included 
    repeat values.'''
    
    #Check that number, minim, and maxum are integers:
    chk_list = [number,minim,maxum]
    compare2str = ['number','minim','maxum'] ### For referring back to in feedback
    chk_type = [type(item) for item in chk_list]
    if all(item == int for item in chk_type) == False:
        bool_chk = [item != int for item in chk_type]
        invalids = [compare2str[i] for i in range(0,3) if bool_chk[i]]
        feedback = "Your input(s) for '{}' are invalid. 'number', 'minim', and 'maxum' must be integers.".format(invalids)
        return(feedback)
    else:
        #Check that number, minim, and maxum are positive:
        pos_chk = [x > 0 for x in chk_list]
        if all(pos_chk) == False:
            invalids2 = [compare2str[i] for i in range(0,3) if pos_chk[i]]
            feedback2 = "Your input(s) for '{}' are invalid. 'number', 'minim', and 'maxum' must be \
greater than zero.".format(invalids2)
            return(feedback2)
    #Check that rep and return_dummy are booleans:
    chk_list2 = [rep,return_dummy]
    compare2str2 = ['rep','return_dummy']
    chk_type2 = [type(item) for item in chk_list2]
    if all(item == bool for item in chk_type2) == False:
        bool_chk2 = [item != bool for item in chk_type2]
        invalids3 = [compare2str2[i] for i in range(0,2) if bool_chk2[i]]
        feedback3 = "Your input(s) for '{}' are invalid. 'rep' and 'return_dummy' must be booleans.".format(invalids3)
        return(feedback3)
    if rep==True:
        rand_vect = list(np.random.randint(minim,maxum+1,number))
        return(rand_vect)
    else:
        #Check that requested data are valid:
        if number > 1 + maxum - minim:
            return("You cannot have more unique results than available numbers to choose from.")
        thresh = 1
        first = list(np.random.randint(minim,maxum+1,1))
        build_vect = [first]
        dummy_vect = [first]
        while thresh < number:
            next_num = list(np.random.randint(minim,maxum+1,1))
            dummy_vect.append(next_num)
            if next_num not in build_vect:
                build_vect.append(next_num)
                thresh += 1
        retrn = {}
        retrn['return_vector'] = build_vect
        if return_dummy == True:
            retrn['dummy_vector'] = dummy_vect
        return(retrn)
        



def generate_team():
    chars = ["Terra","Locke","Edgar","Sabin","Celes","Shadow","Cyan","Gau","Setzer","Mog","Strago","Relm","Umaro","Gogo"]
    chars_ser = pd.Series(data=chars,index=range(1,len(chars)+1))
    raw_team = gen_randint(number=4, minim=1, maxum=len(chars), rep=False, return_dummy=False)['return_vector']
    raw_team2 = [raw_team[i][0] for i in range(0,len(raw_team))]
    team = list(chars_ser[raw_team2])
    
    
    #First, the background:
    L0 = Label(root,text= "Your Team", bg = 'gold', relief = 'ridge', padx=74, pady=5, font = ("Helvetica", "14", "bold"))
    L0.grid(row=1,column=1,columnspan=2)
    
    L1 = Label(root, text=placeholder_text, bg = 'dark grey', relief = 'groove')
    L1.grid(row=4,column=0,columnspan=2)
    L2 = Label(root, text=placeholder_text, bg = 'dark grey', relief = 'groove')
    L2.grid(row=4,column=2,columnspan=2)
    L3 = Label(root, text=placeholder_text, bg = 'dark grey', relief = 'groove')
    L3.grid(row=7,column=0,columnspan=2)
    L4 = Label(root, text=placeholder_text, bg = 'dark grey', relief = 'groove')
    L4.grid(row=7,column=2,columnspan=2)
    
    #Next, the names:
    L5 = Label(root, text=' {} '.format(team[0]), bg = 'light blue', relief = 'sunken', padx=3, font = subFont)
    L5.grid(row=4,column=0,columnspan=2)
    L6 = Label(root, text=' {} '.format(team[1]), bg = 'light blue', relief = 'sunken', padx=3, font = subFont)
    L6.grid(row=4,column=2,columnspan=2)
    L7 = Label(root, text=' {} '.format(team[2]), bg = 'light blue', relief = 'sunken', padx=3, font = subFont)
    L7.grid(row=7,column=0,columnspan=2)
    L8 = Label(root, text=' {} '.format(team[3]), bg = 'light blue', relief = 'sunken', padx=3, font = subFont)
    L8.grid(row=7,column=2,columnspan=2)
    
    
    #Finally, the portraits:
    image1 = PhotoImage(file='Portraits\\terra.png')
    image2 = PhotoImage(file='Portraits\\locke.png')
    image3 = PhotoImage(file='Portraits\\edgar.png')
    image4 = PhotoImage(file='Portraits\\sabin.png')
    image5 = PhotoImage(file='Portraits\\celes.png')
    image6 = PhotoImage(file='Portraits\\shadow.png')
    image7 = PhotoImage(file='Portraits\\cyan.png')
    image8 = PhotoImage(file='Portraits\\gau.png')
    image9 = PhotoImage(file='Portraits\\setzer.png')
    image10 = PhotoImage(file='Portraits\\mog.png')
    image11 = PhotoImage(file='Portraits\\strago.png')
    image12 = PhotoImage(file='Portraits\\relm.png')
    image13 = PhotoImage(file='Portraits\\umaro.png')
    image14 = PhotoImage(file='Portraits\\gogo.png')
    image_vector = [image1,image2,image3,image4,image5,image6,image7,image8,image9,image10,image11,image12,image13,image14]
    
    L9 = Label(image = image_vector[raw_team2[0]-1], takefocus = True, bg = 'white', bd = 2)
    L9.image = image_vector[raw_team2[0]-1]
    L9.grid(row=2, column=0, columnspan=2, rowspan=2)
    
    L10 = Label(image = image_vector[raw_team2[1]-1], takefocus = True, bg = 'white', bd = 2)
    L10.image = image_vector[raw_team2[1]-1]
    L10.grid(row=2, column=2, columnspan=2, rowspan=2)
    
    L11= Label(image = image_vector[raw_team2[2]-1], takefocus = True, bg = 'white', bd = 2)
    L11.image = image_vector[raw_team2[2]-1]
    L11.grid(row=5, column=0, columnspan=2, rowspan=2)
    
    L12 = Label(image = image_vector[raw_team2[3]-1], takefocus = True, bg = 'white', bd = 2)
    L12.image = image_vector[raw_team2[3]-1]
    L12.grid(row=5, column=2, columnspan=2, rowspan=2)


    #We alter the text of the generation button to be more relevant:
    b2 = Button(root, text = "Not satisfied? Try again!", command = generate_team, font = mainFont, bg = 'green', fg = 'white',
                relief = 'raised')
    b2.grid(row=0,column=0,columnspan=4)



#This is where we activate the GUI:
        
root = Tk()

#frame = Frame(root,height=6,width=4)
#frame.grid(row=0,column=0,columnspan=4,rowspan=6)


b1 = Button(root, text = "Generate Team!", command = generate_team, font = mainFont, relief = 'raised')
b1.grid(row=0,column=0,columnspan=4)


root.mainloop()
