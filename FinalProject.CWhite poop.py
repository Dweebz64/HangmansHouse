"""
Carrie White
Final Project - Hangman's House
This program plays hangman except removes parts from a house. User has 7 attempts at guessing letters in the word. 'Enter' starts a new game with a new word.
Due May 17, 2022
"""

import random
from tkinter import *

def keyPressed(event): #Command function for when user presses key on keyboard
    global tries, wordCompletion, missedLetters

    guess = event.char #get pressed key

    if not guess.isalpha():   #Checks for non-letters
        return

    if guess.isalpha():       #Converts all letters to uppercase for better comparision logic
        guess = guess.upper()


        if guess in missedLetters: #Checks if letter was already guessed
            return

        if guess in word: #If letter is in word, it replaces the * in the word.
            wordCompletion_list = list(wordCompletion.replace(" ","")) #Makes a list
            for i in range(0,len(word)):
                if word[i] == guess:
                    wordCompletion_list[i] = word[i]        #Matches indices, and replaces * with guessed letter
            wordCompletion = ''.join(wordCompletion_list)               
            text1 = "Guess a word: " +wordCompletion
            text2 = "Missed letters: " +missedLetters
        else:               #Incorrect guesses are added to list and tries deducted by 1
            missedLetters+=(guess + '')
            tries -= 1

            if tries > 0:   #Display text during active game
                text1 = "Guess a word: " +wordCompletion
                text2 = "Missed letters: " +missedLetters

            else:   #Display text for lost game
                text1 = "The word is: " +word
                text2 = "To play new game, press ENTER"

        if '*' not in wordCompletion:    #Display text when all letters have been guessed and game won
            text1 = "Congrats! The word is: " +word
            text2 = "To play new game, press ENTER"

        displayHouse(tries,text1,text2) #Displays and updates house
        return


def displayHouse(tries,text1,text2):     #Displays GUI House, each time tries decrease, it is draw with one less part
    canvas.delete('house') #Deletes the last version of the house
    s = 1     #S is my resize factor

    if tries >= 1:  #Creates walls
        canvas.create_rectangle(40*s,90*s,170*s,190*s, fill = 'light blue', tags = 'house')
    if tries >= 2:  #Creates roof
        canvas.create_polygon(30*s,90*s,90*s,30*s,120*s,30*s,180*s,90*s, fill = 'gray', tags = 'house')
    if tries >= 3:  #Creates door
        canvas.create_rectangle(90*s,140*s,120*s,190*s, fill = 'gray', tags = 'house')
    if tries >= 4:  #Creates window 1
        canvas.create_rectangle(50*s,110*s,80*s,140*s, fill = 'white', tags = 'house')
    if tries >= 5:  #Creates window 2
        canvas.create_rectangle(130*s,110*s,160*s,140*s, fill = 'white', tags = 'house')
    if tries >= 6:  #Creates window 3
        canvas.create_rectangle(90*s,50*s,120*s,80*s, fill = 'white', tags = 'house')
    if tries >= 7:  #Creates Chimney
        canvas.create_polygon(50*s,70*s,50*s,30*s,70*s,30*s,70*s,50*s, fill = 'black', tags = 'house')        

    canvas.create_text(150,300,text= text1,fill = 'black',font= (10),tags = 'house')    #Lines for gameplay text
    canvas.create_text(150,325,text= text2,fill = 'black',font= (10),tags = 'house')



def newGame():  #Starts new game, sets up new varible values
    global tries, wordCompletion, word, missedLetters

    word = (random.choice(open("wordBank.txt").readline().split())) #Picks a random word
    wordCompletion = "*" * len(word)                    #Display * for word
    tries = 7                                           #Number of incorrect guesses allowed
    missedLetters = ''                                  #Stores incorrect guesses
    text1 = "Guess a word: " +wordCompletion            #Sets up display text
    text2 = ""

    displayHouse(tries,text1,text2) #Creates the first game GUI


def replay(event): #Key function for restarting the game
    newGame()


window = Tk()                   #Creates GUI Window
window.title("Hangman's House") #Adds title to window

#Global Variables
word = wordCompletion = missedLetters = ''
tries = 7

canvas = Canvas(window, width = 325, height = 350, bg = 'white')    #Creates Canvas display, sets size and color
canvas.pack()


newGame() #Starts first game

canvas.focus_set() #Shifts focus to keyboard instead of mouse
canvas.bind('<Return>',replay)  #Binding ENTER to trigger replay function
canvas.bind('<Key>', keyPressed)#Binding key press to trigger keyPressed function

window.mainloop() #Loop for window



            
