import random
import colorama
from colorama import Fore, Back, Style
from logics import gameAssitance, randomNumber, initialization

if __name__ == "__main__":
    initialization.welcomeMsg()
    while (True):
        initialization.choices()
        choice = input(Fore.YELLOW + "Enter your choice: ")
        print(Style.RESET_ALL)
        if (choice.lower() == 'q'):
            print("Ok, see you next time")
            exit()
        # Error handling for choice, low, high is int or not
        try:
            choice = int(choice)

            # numbers[0.no of guesses, 1.lower limit, 2.upper limit, 3.random number, 4.user guessed number, 5.previous best score]
            numbers = [0]
            randomNumber.randomNumber(
                choice=choice, numbersList=numbers)
            numbers.append(None)

            while (numbers[4] != numbers[3]):
                numbers[4] = input(Fore.YELLOW + "Enter your guess: ")
                print(Style.RESET_ALL)

                # Error handling for user guess is int or not
                try:
                    numbers[4] = int(numbers[4])
                    gameAssitance.gameAssist(
                        userGuess=numbers[4], randNumber=numbers[3], high=numbers[2], low=numbers[1])
                    numbers[0] += 1

                except ValueError as e:
                    print(Fore.RED +
                          "Please, don't enter a char. Enter a int b/w {1} & {0}.".format(numbers[2], numbers[1]))
                    print(Style.RESET_ALL)
                except Exception as e:
                    print(Fore.RED + f"Your input resulted in an error: {e}")
                    print(Style.RESET_ALL)

            print(
                f"You guessed the number {numbers[3]} in {numbers[0]} guesses")
            # Error handling for hiscore.txt file
            try:
                with open("hiscore.txt", "r") as f:
                    numbers.append(int(f.read()))
                if (numbers[5] == 100):
                    print("Previous best score got a reset")
                else:
                    print(f"Previous best score was {numbers[5]}")
                if (numbers[0] < numbers[5]):

                    print(Fore.CYAN + Style.BRIGHT +
                          "You have just broken the previous best score!")
                    print(Style.RESET_ALL)
                    with open("hiscore.txt", "w") as f:
                        f.write(str(numbers[0]))
                else:
                    print(
                        "Tip: you can beat previous best score may be by guessing in binary search method")

            except FileNotFoundError as e:
                print(Fore.RED +
                      f"Can't update new score. Change the directory in terminal as: {e}")
                print(Style.RESET_ALL)
        except ValueError as e:
            print(Fore.RED +
                  "Please, don't enter a string. Enter 1 or 2 for choice and make sure upper limit > lower limit")
            print(Style.RESET_ALL)
        except:
            raise ValueError(Fore.RED +
                             "hey, read properly")
            print(Style.RESET_ALL)
        finally:
            # Resetting the Best Score
            with open("hiscore.txt", "r") as f:
                if (int(f.read()) == 1):
                    with open("hiscore.txt", "w") as f:
                        f.write(str(100))
            print(Style.BRIGHT + "Hope, you have enjoyed\n")
            print(Style.RESET_ALL)
