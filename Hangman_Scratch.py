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

misses = 0
charCount = 0

def clicked(r,c):
    global misses #count of incorrect guesses
    global charCount #total number of chars guessed and filled into the word (dd is 2)
    print(alphaBet[r][c]['text'])
    if alphaBet[r][c]['text'] in charList:
        alphaBet[r][c].config(state=DISABLED, 
                bg = "green"
                )

        for index in range(len(charList)):
            if alphaBet[r][c]['text'] == charList[index]:
                wordDisp[index] = charList[index]
                charCount += 1
        print(wordDisp)

    else:
        alphaBet[r][c].config(state=DISABLED, 
                bg = "red"
                )
        misses += 1
        if misses != 1:
            print(f"You have made {misses} incorrect guesses.")
        else:
            print(f"You have made {misses} incorrect guess.")
    checkWin()


def checkWin():
    if charCount == len(charList):
        print(f"You have guessed the word {secret_word}! You win!")
        for i in range(2): #disable all buttons
            for j in range(13):
                alphaBet[i][j].config(state=DISABLED
                )
    elif misses == 6:
        print("You lose!")
        print(f"The word was {secret_word}.")
        for i in range(2): #disable all buttons
            for j in range(13):
                alphaBet[i][j].config(state=DISABLED
                )
 
#Alphabet, 26 char-long string
alphaBet = [['a'],['b'],['c'],['d'],['e'],['f'],['g'],['h'],['i'],['j'],['k'],['l'],['m']],[['n'],['o'],['p'],['q'],['r'],['s'],['t'],['u'],['v'],['w'],['x'],['y'],['z']]

for i in range(2):
    for j in range(13):
                                        
        alphaBet[i][j] = Button(
                        height = 1, width = 2,
                        font = ("Helvetica","20"),
                        command = lambda r = i, c = j : clicked(r,c),
                        activebackground= 'blue',
                        text = alphaBet[i][j]
                        )
        alphaBet[i][j].grid(row = i, column = j)


secret_word = chooseWord(wordlist)
#hangman(secret_word)
charList = structWord(secret_word)
#print(secret_word)

#Display of secret word to player
wordDisp = []
for i in range(0,len(secret_word)):
    wordDisp.append("_")
print(wordDisp)
mainloop()           