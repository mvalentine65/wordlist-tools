#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created on Fri May 29 00:24:03 2020

@author: domu
"""

import argparse

#TODO: allow users to change wordlits. Maybe make it seperate file.
#Thought: If they can make the list in a serperate file they can probably do it here.

#I use the tuple to define the tuples
#The first letter in each tuple is the letter to be pulled from the word
#The following letters are the substitutions
#If you want to add something, remeber the commas tp seperate the values.
#Python needs to see the character between apostrophes to know its a letter and not a variable name 
leet = (
    ('a','@','4'),
    ('A','@','4'),
   # ('b','8'),
   # ('B','8','13'),
   # ('c','<','{','('),
   # ('C','<','{','('),
    ('e','3'),
    ('E','3'),
    #('g','6'),
   # ('G','6'),
    ('i','1','!'),
    ('I','1','!'),
   # ('l','1','!'),
   # ('L','1','!'),
    ('o','0'),
    ('O','0'),
   # ('q','9'),
   # ('Q','9'),
   # ('s','5','$'),
   # ('S','5','$'),
   # ('t','7','+'),
   # ('T','7','+'),
   # ('x','%'),
   # ('X','%'),
   # ('z','2'),
   # ('Z','2')
)
#Turns out tuples are faster than lists, so lets use tuples. We aren't going to change these values anyway.


#defines -h message
def helpmessage():
    message = "[python3] leetify.py (OPTIONS)"
    warning = "This programs takes a wordlist as input and outputs a leet haxor wordlist."
    hline = "-h,    display help text"
    wline = "-w,    specify the wordlist file to use as input"
    oline = "-o,    set the output location"
    vline = "-v,    display created permutations in terminal"
    output = [message,warning,hline,wline,oline,vline]
    for phrase in output:
        print(phrase)


#creates a jagged array the contains the letters of the input with all of their possible substitutions afterwards      
def gears(word):
    gearbox = []
    i = 0
    for letter in word:
        done = False
        for match in leet:
            if letter == match[0]:
                gearbox.append(match)
                done = True
        if done == False:
            gearbox.append([word[i]])
        i = i + 1
   # print(gearbox)
    return gearbox


#creates jagged array with pointer values for iterating through substituions
def timings(gearbox):
    controller = []
    for cog in gearbox:
        controller.append([0,len(cog)])
    controller.append([0])
   # print(controller)
    return controller


#outputs permutations of wordlist
def press(gearbox, controller, outFile, verbose):
    done = 0
    #iterate stops the output on the first loop
    #this is the only way I could stop duplicating the base word
    #I am not a smart man
    iterate = 0
    max_gear = len(gearbox)
    #iterate over gearbox and concanente the needed value
    while done == 0:
        inked = ""
        for gear in range(max_gear):
            #TODO: research if \f or .join would be faster
            inked = inked + gearbox[gear][controller[gear][0]]
            gear = gear + 1

        with open(outFile,'a+') as output:
            if iterate > 0:
                output.write(inked+"\n")
                if verbose == 2:
                    print(inked)
            else:
                iterate = iterate + 1
            #feedback is nice I guess

        done = rotate(controller,0)


#increments integers to use as pointer to undexes in gear array
def rotate(controller,i):
    done = 0
    #increments index bby one to point to the next character in list
    controller[i][0] = controller[i][0] + 1
    #checks to see if sentinel value tripped
    if controller[-1][0] == 1:
        done = 1
    #if current index is euqal to max index, increment next gear
    elif controller[i][0] == controller[i][1]:
        controller[i][0] = 0
        #be careful with recursive functions
        rotate(controller,i+1)
    return done


#TODO dig up old recursive version and use it selectively based on word length
def Main(inFile=None, outFile=None, verbose=1):
    if verbose > 0:
        print("**** Keep in mind, this program doesn't check available space.")
        print("**** The output file can easily be 20 times the size of the input.")
        print("**** If that seems like a problem, quit the program with 'Ctrl+C'.")
        print("**** If the program finished working before you could read this, \n**** you're probably fine.")
    if inFile == None:
      inFile = input("What is the name of the wordlist you want to modify? ")
    if outFile == None:
      outFile = input("\nWhat is the name of the destination file? ")
    with open(inFile,'r') as start:
        for line in start: 
            word = line.strip()
            if len(word) > 0 and len(word) < 25:
                if verbose==1:
                    print(word)
                gearbox = gears(word)
                controller = timings(gearbox)
                press(gearbox,controller, outFile, verbose)
#TODO: add code to determine if argv value is a switch or not
#TODO: (maybe) add command line support for input and output files


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 'Takes a wordlist as input and uses a predefined leetspeak dictionary to create all possible permutations of the wordlist.')
    parser.add_argument('-v','--verbose-mode' ,type=int, default=2, choices=[0,1,2], help='Set level of verbose mode to be used. 0 will display no feedback. -v 1 will display base words from the input list as they are used. -v 2 will display all possible permutations of the base word as they are generated. This is the default setting.')
    parser.add_argument('input', nargs='?',default=None)
    parser.add_argument('output', nargs='?',default=None)
    args = (parser.parse_args())    
    Main(args.input,args.output,args.verbose_mode)


#----------EOF----------#
#Leftover debugging code
#print (gearbox,"\n")
#print (alignment,"\n")
