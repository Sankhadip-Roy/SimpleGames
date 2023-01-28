import random


def gameAssist():
    if (userGuess == randNumber):
        print("You guessed it right!")
    else:
        if (userGuess > randNumber):
            print("You guessed it wrong! You have to guess a smaller number")
            if (userGuess-randNumber > (l+h)//2):
                print("Difference is too large")
            elif (userGuess-randNumber < (l+h)//3):
                print("It's nearby")
            else:
                print("Try again")
        else:
            print("You guessed it wrong! You have to guess a greater number")
            if (randNumber-userGuess > (l+h)//2):
                print("Difference is too large")
            elif (randNumber-userGuess < (l+h)//3):
                print("It's nearby")
            else:
                print("Try again")


list1 = ["Enter 1 to customise lower and upper limit",
         "Enter 2 to go with default(1, 100)", "Enter 'q' to quit"]
WelcomeMsg = '''\n======== Welcome to the Number Guess Game ========
Game rule -> Firstly you have to select the limit in which you want to play.
             Secondly you have to guess the number within that limit, and 
             you will get assisted.
'''
if __name__ == "__main__":
    print(WelcomeMsg)
    while (True):
        for index, item in enumerate(list1):
            print(f"{index+1}: {item}")
        n = input("Enter your choice: ")
        if (n.lower() == 'q'):
            print("Ok, see you next time")
            exit()
        try:
            n = int(n)
            if (n == 1):
                l, h = int(input("Enter lower limit: ")), int(
                    input("Enter higher limit: "))
            elif (n == 2):
                l = 1
                h = 100
            randNumber = random.randint(l, h)

            userGuess = None
            guesses = 0

            while (userGuess != randNumber):
                userGuess = input("Enter your guess: ")
                try:
                    userGuess = int(userGuess)
                    gameAssist()
                    guesses += 1

                except ValueError as e:
                    print(
                        "Please, don't enter a string. Enter a number b/w {1} & {0}.".format(h, l))
                except Exception as e:
                    print(f"Your input resulted in an error: {e}")

            print(f"You guessed the number {randNumber} in {guesses} guesses")
            try:
                with open("hiscore.txt", "r") as f:
                    hiscore = int(f.read())
                print(f"Your previous high score is {hiscore}")
                if (guesses < hiscore):
                    print("You have just broken the high score!")
                    with open("hiscore.txt", "w") as f:
                        f.write(str(guesses))
            except FileNotFoundError as e:
                print(
                    f"Can't update new score. Change the directory in terminal as: {e}")
        except ValueError as e:
            print(
                "Please, don't enter a string. Enter 1 or 2 for choice and make sure upper limit > lower limit")
        except:
            raise ValueError(
                "hey, read properly")
        finally:
            print("Hope, you have enjoyed\n")
