import random
print("Enter 1 to customise lower and upper limit\nEnter 2 to go with default (1,100)")
n = int(input("Enter your choice: "))
if(n == 1):
    l, h = int(input("Enter lower limit: ")), int(
        input("Enter higher limit: "))
elif(n == 2):
    l = 1
    h = 100
randNumber = random.randint(l, h)

userGuess = None
guesses = 0

while(userGuess != randNumber):
    userGuess = int(input("Enter your guess: "))
    guesses += 1
    if(userGuess == randNumber):
        print("You guessed it right!")
    else:
        if(userGuess > randNumber):
            print("You guessed it wrong! Enter a smaller number")
            if(userGuess-randNumber > (l+h)/2):
                print("Difference is too large")
            else:
                print("It's nearby")
        else:
            print("You guessed it wrong! Enter a larger number")
            if(randNumber-userGuess > (l+h)/2):
                print("Difference is too large")
            else:
                print("It's nearby")

print(f"You guessed the number {randNumber} in {guesses} guesses")
with open("hiscore.txt", "r") as f:
    hiscore = int(f.read())
print(f"Your previous high score is {hiscore}")
if(guesses < hiscore):
    print("You have just broken the high score!")
    with open("hiscore.txt", "w") as f:
        f.write(str(guesses))
