import random
import colorama
from colorama import Fore, Back, Style


def randomNumber(choice, numbersList):
    if (choice == 1):
        low, high = int(input(Fore.BLACK + Back.LIGHTCYAN_EX + "Enter lower limit: ")), int(
            input(Fore.BLACK + Back.LIGHTYELLOW_EX + "Enter higher limit: "))
        print(Style.RESET_ALL)
    else:
        low, high = 1, 100
    numbersList.append(low)
    numbersList.append(high)
    numbersList.append(random.randint(low, high))
    # return numbers
