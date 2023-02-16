import colorama
from colorama import Fore, Back, Style


def gameAssist(userGuess, randNumber, high, low):
    if (userGuess == randNumber):
        print(Fore.GREEN + "You guessed it right!")
        print(Style.RESET_ALL)
    else:
        if (userGuess > randNumber):
            print(Fore.RED +
                  "You guessed it wrong! You have to guess a smaller number")
            print(Style.RESET_ALL)
            if (userGuess-randNumber > (low + high)//2):
                print(Fore.RED + "Difference is too large")
                print(Style.RESET_ALL)
            elif (userGuess-randNumber < (low + high)//3):
                print(Fore.GREEN + "It's nearby")
                print(Style.RESET_ALL)
            else:
                print(Style.DIM + "Try again")
                print(Style.RESET_ALL)
        else:
            print(Fore.RED + "You guessed it wrong! You have to guess a greater number")
            print(Style.RESET_ALL)
            if (randNumber-userGuess > (low + high)//2):
                print(Fore.RED + "Difference is too large")
                print(Style.RESET_ALL)
            elif (randNumber-userGuess < (low + high)//3):
                print(Fore.GREEN + "It's nearby")
                print(Style.RESET_ALL)
            else:
                print(Style.DIM + "Try again")
                print(Style.RESET_ALL)
