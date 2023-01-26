#Hangman game
from tkinter import * 
from tkinter import messagebox
import random
import string



WORDLIST_FILENAME = "words.txt"


def load_words():
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist 

def chooseWord(wordlist):
    return random.choice(wordlist)

#Break word into list of chars
def structWord(word):
    global charList
    charList = []
    for i in range(0,len(word)):
        charList.append(word[i])
    #print(charList)
    return charList



# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()

secret_word = chooseWord(wordlist)
#hangman(secret_word)
charList = structWord(secret_word)
#print(secret_word)

#Display of secret word to player
wordDisp = []
for i in range(0,len(secret_word)):
    wordDisp.append("_")

misses = 0
charCount = 0

def clicked(r,c):
    global misses #count of incorrect guesses
    global charCount #total number of chars guessed and filled into the word (dd is 2)
    if alphaBet[r][c]['text'] in charList:
        alphaBet[r][c].config(state=DISABLED, 
                bg = "green"
                )
        buttText.config(text = f"Good guess, {alphaBet[r][c]['text']} is in the word")
        for index in range(len(charList)):
            if alphaBet[r][c]['text'] == charList[index]:
                wordDisp[index] = charList[index]
                charCount += 1

    else:
        alphaBet[r][c].config(state=DISABLED, 
                bg = "red"
                )
        misses += 1
        if misses != 5:
            buttText.config(text = f"You have {6 - misses} more tries ")
        else:
            buttText.config(text = f"You have {6 - misses} more try ")
    checkWin()
    checkMissed(misses)


def checkWin():
    #Update word shown to user on GUI
    buttWord.config(text = wordDisp)

    #CheckWin True condition, all letters account for
    if charCount == len(charList):
        buttWord.config(bg = "green")
        for i in range(2): #disable all buttons
            for j in range(13):
                alphaBet[i][j].config(state=DISABLED
                )
        buttText.config(text = "You win! You have guessed the secret word")
    #CheckWin False condition, 6 wrong guesses
    elif misses == 6:
        buttWord.config(bg = "red")
        for i in range(2): #disable all buttons
            for j in range(13):
                alphaBet[i][j].config(state=DISABLED
                )
        buttText.config(text = f"You lose! The secret word was {secret_word}")

#Check number of misses and draw man accordingly
def checkMissed(x):
    if x == 1:
        canvas.create_line(85, 10, 85, 20)
        canvas.create_oval(65,20,105,60)
    elif x == 2:      
        canvas.create_line(85, 60, 85, 120)
    elif x == 3:
        canvas.create_line(85, 120, 60, 180)
    elif x == 4:
        canvas.create_line(85, 120, 110, 180)
    elif x == 5:
        canvas.create_line(85, 60, 120, 100)
    elif x == 6:
        canvas.create_line(85, 60, 50, 100)
        # Left eye
        canvas.create_line(75,35,80,40)
        canvas.create_line(75,40,80,35)
        # Right eye
        canvas.create_line(95,35,100,40)
        canvas.create_line(95,40,100,35)
        # Frown
        canvas.create_line(80,50,95,50)

#Alphabet, 26 char-long string
alphaBet = [['a'],['b'],['c'],['d'],['e'],['f'],['g'],['h'],['i'],['j'],['k'],['l'],['m']],[['n'],['o'],['p'],['q'],['r'],['s'],['t'],['u'],['v'],['w'],['x'],['y'],['z']]

buttWord = Button(
                        font = ("Helvetica","30"),
                        activebackground= 'blue',
                        state=DISABLED,
                        text = wordDisp
                        )  
buttWord.grid(row = 0, columnspan = 13, sticky = SW, pady = 0)

buttText = Button(
                        font = ("Helvetica","12"),
                        activebackground= 'blue',
                        state=DISABLED,
                        text = "Welcome to HangMan! You have 6 guesses to guess the secret word"
                        )  
buttText.grid(row = 1, columnspan = 13, sticky = EW, pady = 0)

#Generate drawing window
canvas = Canvas(width=200, height=200)
canvas.grid(row=0, columnspan = 13, sticky = E, pady = 0)

#Draw Gallows
canvas.create_line(10, 10, 10, 200)
canvas.create_line(10, 10, 150, 10)
canvas.create_line(10, 200, 50, 200)

for i in range(2):
    for j in range(13):
                                        
        alphaBet[i][j] = Button(
                        height = 1, width = 2,
                        font = ("Helvetica","20"),
                        command = lambda r = i, c = j : clicked(r,c),
                        activebackground= 'blue',
                        text = alphaBet[i][j]
                        )
        alphaBet[i][j].grid(row = i+10, column = j)





mainloop()           