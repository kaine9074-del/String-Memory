import time
import random
import os
import msvcrt 

alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

def Get_Valid_string(user_input):
    while True:
        if user_input.isalpha:
            break
        else:
            print("Has to be a letter.")
            user_input = input("What is the string: ").strip().upper()
    return user_input

def clear_keyboard_buffer(): 

    """Remove any pending keystrokes from the keyboard buffer.""" 

    while msvcrt.kbhit(): 

        msvcrt.getwch() 

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

def Count_Down():
    for i in range(5):
        print(".", end="", flush=True)
        time.sleep(1)
    print()

def Inistualize_string():
    new = random.choice(alphabet)
    string.append(new)
    new = random.choice(alphabet)
    string.append(new)
    new = random.choice(alphabet)
    string.append(new)

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

while True:
    Level = 0
    string = []
    Inistualize_string()

    user = input("Press anything to start playing, Q/q to quit: ").strip().upper()

    if user == "Q":
        clear_terminal()
        print("Goodbye")
        break
    while True:
        Level = (Level + 1)
        print(f"Level: {Level}")
        update_string(Level, string)
        useable = "".join(string)
        print(useable)
        Count_Down()
        clear_terminal()
        clear_keyboard_buffer()
        user_input = input("What is the string: ").strip().upper()
        Get_Valid_string(user_input)
        if win_or_loss(user_input, useable):
            print("Good Job!")
            time.sleep(3)
        else:
            print(f"This was the correct answer {useable}")
            print(f"This is what you said {user_input}")
            print(f"You made it to level {Level}")
            time.sleep(5)
            clear_terminal()
            break

    if not Play_again():
        break

