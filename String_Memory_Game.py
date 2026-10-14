import time
import random
import os

alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

def Get_Valid_string(user_input):
    while True:
        if user_input.isalpha:
            break
        else:
            print("Has to be a letter.")
            user_input = input("What is the string: ").strip().upper()
    return user_input

def update_string(Level, string):
    number = 0
    while True:
        new = random.choice(alphabet)
        string.append(new)
        number += 1
        if number == Level:
            return string



def win_or_loss(user_input, useable):
    return user_input == useable

def Play_again():
    while True:
        input1 = input("Would you like to play again? Y/N ").upper().strip()
        if input1.isalpha():
                if input1 == "Y":
                    Playagain = True
                    break
                elif input1 == "N":
                    Playagain = False
                    print(Playagain)
                    break
                else:
                    print("Give Y/N")
        else:
            print("Please input Y/N")
    return Playagain

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

while True:
    Level = 0
    string = []
    while True:
        Level = (Level + 1)
        print(f"Level: {Level}")
        update_string(Level, string)
        useable = "".join(string)
        print(useable)
        time.sleep(5)
        clear_terminal()
        user_input = input("What is the string: ").strip().upper()
        Get_Valid_string(user_input)
        if win_or_loss(user_input, useable):
            print("win")
        else:
            print("Lose")
            break

    if not Play_again():
        break

