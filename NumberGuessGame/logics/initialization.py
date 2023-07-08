import colorama
from colorama import Fore, Back, Style
choicesList = ["custom (lower, upper) -> 1",
               "default (1, 100) -> 2", "quit -> q"]
WelcomeMsg = '''\n======== Welcome to the Number Guess Game ========
Game rule -> Firstly you have to select the limit in which you want to play.
             Secondly you have to guess the number within that limit, and 
             you will get assisted.
'''


def welcomeMsg():
    print(Back.WHITE + Fore.BLACK + Style.BRIGHT + WelcomeMsg)
    print(Style.RESET_ALL)


def choices():
    for index, item in enumerate(choicesList):
        print(Style.BRIGHT + f"{index+1}: {item}")
        print(Style.RESET_ALL)
