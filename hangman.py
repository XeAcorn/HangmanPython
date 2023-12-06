#import random in order to randomly select
#a word from the words array
#import time in order to display an
#error message for a length of time
#before disappearing
import random
import time

#initializing global variables for use in multiple functions
leave = False
word = ""
guess = []
wrongs = []
strikes = 0
rnum = 0
strikeLimit = 5
words = ['ROCKET','SCIENCE','MATHEMATICS','PROGRAMMING','PYTHON','HALF-LIFE','CALIFORNIA','LEARN']
    
#init function easily resets global variables
#to restart the game without the need to
#close and reopen the python script
def init():
    global word
    global guess
    global strikes
    global leave
    global rnum
    leave = False
    strikes = 0
    guess.clear()
    wrongs.clear()
    #word = random.choice(words)
    rnum = random.randrange(0,len(words))
    word = words[rnum]
    for i in range(len(word)):
        if word[i] == "-":
            guess.append("-")
        else:
            guess.append("_")

#quit function allows for a neat way to say
#Goodbye to a user when they wish to close
#your program
def quit():
    global leave
    leave = True
    print("Goodbye!")
    print("Hangman made by Jacob Daniels")
    time.sleep(3)
    exit(0)

#win function is called when a player
#uncovers every letter of the word
#They are then asked if they would like
#to keep playing the game or to quit
def win():
    print ("Congratulations!!! You won the game!")
    print("Would you like to restart? (Y/n) ", end="")
    opt = input().upper()
    if opt == "Y":
        init()
        program()
    elif opt == "N":
        quit()
    else:
        print("That was not an option! Restarting...")
        time.sleep(1.5)
        init()
        program()

#lose function is called when a player
#surpasses 5 strikes, thus hanging the man
#Players are also asked if they would like
#to restart here
def lose():
    print ("Oh no! You lost the game!")
    print("\nThe word was " + word + "\n")
    print("Would you like to restart? (Y/n) ", end="")
    opt = input().upper()
    if opt == "Y":
        init()
        program()
    elif opt == "N":
        quit()
    else:
        print("That was not an option! Restarting...")
        time.sleep(1.5)
        init()
        program()
        
#having a program function allows for
#easily requesting user input repeatedly
#while also checking the status of the word
#and strikes to determine if the user has
#won or lost the game
def program():
    global leave
    global strikes
    global guess
    global word
    global wrongs
    global rnum
    found = False
    wordArray = [char for char in word]
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print("Word ID: " + str(rnum))
    if strikes == 0:
        print("\n|------|")
        print("|      |")
        print("|")
        print("|")
        print("|")
        print("---------")
    if strikes == 1:
        print("\n|------|")
        print("|      |")
        print("|      O")
        print("|")
        print("|")
        print("---------")
    if strikes == 2:
        print("\n|------|")
        print("|      |")
        print("|      O")
        print("|      |")
        print("|")
        print("---------")
    if strikes == 3:
        print("\n|------|")
        print("|      |")
        print("|      O")
        print("|     /|")
        print("|")
        print("---------")
    if strikes == 4:
        print("\n|------|")
        print("|      |")
        print("|      O")
        print("|     /|\\")
        print("|")
        print("---------")
    if strikes == 5:
        print("\n|------|")
        print("|      |")
        print("|      O")
        print("|     /|\\")
        print("|     /")
        print("---------")
    if strikes == 6:
        print("\n|------|")
        print("|      |")
        print("|      O")
        print("|     /|\\")
        print("|     / \\")
        print("---------")

    #displays guesses so far and
    #which letters were guessed
    #incorrectly along with how
    #many strikes the player has
    for g in range(len(guess)):
        print(guess[g], end=" ")

    print("\n\nIncorrect: ", end="")
    for r in range(len(wrongs)):
        print(wrongs[r], end=" ")
    print("\nStrikes: " + str(strikes) + "\n")

    #this checks to see if there are any
    #remaining letters to uncover
    #if there aren't, then the player has
    #won the game so we should call the
    #win function and return from the current
    #function in case the user wishes to restart
    w = "_"
    if w not in guess:
        leave = True
        win()
        return

    #this checks if a user has surpassed five
    #strikes and if so, call the lose function
    #and return from this function
    if strikes > strikeLimit:
        lose()
        return
    print("Please enter a letter: ", end="")
    letter = input().upper()

    #try except statements automatically check
    #whether the player has selected a correct
    #letter
    #this also allows for any word to be entered
    #by the developer/collaborators
    try:
        chi = 0
        while wordArray.index(letter) > -1:
            found = True
            guess[wordArray.index(letter) - chi] = letter
            wordArray.pop(wordArray.index(letter))
            print(wordArray)
            chi -= 1

    except ValueError:
        if not found:
            strikes += 1
            wrongs.append(letter)



init()

#continually calls the program until
#the user decides to leave the game
while leave is not True:
    program()