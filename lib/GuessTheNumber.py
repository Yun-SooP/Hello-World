import random

randomNumber = 0
userGuess = 0
finish = False
count = 1

def generateRandomNumber():
    global randomNumber
    randomNumber = random.randint(0,100)

def compare():
    if(randomNumber != int(userGuess)):
        if (int(userGuess) < randomNumber):
            print("Wrong! Try to go higher!")
        else:
            print("Wrong! Try to go lower!")
    else:
        print("Correct!")
        print("You tried %s times!" % count)
        global finish
        finish = True

print("Hello! Welcome to number guessing. Try to guess the number!")
generateRandomNumber()
while(not finish):
    try:
        userGuess = int(input("What is your guess? "))
    except:
        continue
    compare()
    count += 1



print("This is a change.")