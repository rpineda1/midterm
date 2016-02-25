# This is a very simple game of sticks. There are 21 sticks, first the user picks number of sticks between 1-4, then the computer picks sticks(1-4). Who ever will pick the last stick will lose.
# Look for the TODO blocks as an indication of when you have to add your own code.

import random
sticks = 21

def playGame():
    # you do not need to modify code in this function
    print('There are 21 sticks. You can pick from 1 to 4 sticks at a time, and the computer will then pick from 1 to 4 sticks at a time. Whoever picks the last stick loses!')
    while True:
        print('Current sticks: ' + str(sticks))
        userChoice = askUserChoice()
        if subtractSticks( userChoice ):
            print('You lost!')
            break
        
        computerChoice = determineComputerChoice()
        print('Computer picked: ' + str(computerChoice) )
        if subtractSticks( computerChoice ):
            print('Computer lost!')
            break
        

def askUserChoice():
    print('How many sticks do you want to pick up? (1-4)')# this line tells the user that they have between 1-4 sticks to pick up 
    userChoise = int(input()) # this is the users input
    if userChoise in range(1,5):# this if statment tells the program that if the the input chosen by the user is between 1-4 then to contine the game.
        return userChoise
    else:# this else statment in the other hand tells the program that if the user did not choose a number between 1-4 then an error statment will display.
        print('sorry your answer is invalid, please choose an number between 1-4 and try again!')
    # TODO: write code in this functiont that:
    # 1. Asks the user to enter their input (between 1 and 4)
    # 2. Checks that the user's input is valid. If it's not valid (if it's not between 1 and 4), then ask the user to re-enter their input.
    # 3. Once the user enters a valid input, return that input as an integer.


def subtractSticks( number ):
    global sticks # this puts sticks not only in subtractSticks when called but also in the global scopes to be used throught the game.
    sticks -= number

    if sticks <= 0: # this if statment tells the program that if the sticks picked up are less than or equal to zero then it will return as a True statment or else as a False.
        return True
    else:
        return False
    
    # TODO: write code inside this function that:
    # 1. subtracts the parameter `number` from the global variable `sticks`
    # 2. checks if the number subtracted resulted in the last stick, if so, return True
    # 3. if there are still sticks left, return False
    
def determineComputerChoice():
    # TODO: write code inside this function that returns an integer between 1 and 4, random chosen by the computer
    r = random.randint(1,4) # this tells the program that the computer will pick a random number between 1-4 and then returns.
    return r
