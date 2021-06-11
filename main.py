# Imports
import os
from termcolor import colored, cprint
import readchar
import random
import sys


# Draw the man accordingly to tries_left
def prepare_draw():
    os.system("cls")
    print("      _______ ")
    print("     |/       ")
    print("     |        ")
    print("     |        ")
    print("     |        ")
    print('     |        ')
    print("     |        ")
    print("    _|___     ")

def draw_head():
    os.system("cls")
    print("      _______")
    print("     |/      |")
    print("     |      (_)")
    print("     |      ")
    print("     |       ")
    print('     |      ')
    print("     |")
    print("    _|___")

def draw_left_arm():
    os.system("cls")
    print("      _______")
    print("     |/      |")
    print("     |      (_)")
    print("     |       |/")
    print("     |       ")
    print('     |      ')
    print("     |")
    print("    _|___")

def draw_right_arm():
    os.system("cls")
    print("      _______")
    print("     |/      |")
    print("     |      (_)")
    print("     |      \|/")
    print("     |       ")
    print('     |      ')
    print("     |")
    print("    _|___")

def draw_body():
    os.system("cls")
    print("      _______")
    print("     |/      |")
    print("     |      (_)")
    print("     |      \|/")
    print("     |       |")
    print('     |      ')
    print("     |")
    print("    _|___")
def draw_left_leg():
    os.system("cls")
    print("      _______")
    print("     |/      |")
    print("     |      (_)")
    print("     |      \|/")
    print("     |       |")
    print('     |      /')
    print("     |")
    print("    _|___")

def draw_right_leg():
    os.system("cls")
    print("      _______")
    print("     |/      |")
    print("     |      (_)")
    print("     |      \|/")
    print("     |       |")
    print('     |      / \ ')
    print("     |")
    print("    _|___")

# Remove duplicates from a given string
def remDuplicates(str):
    return "".join(set(str))

# Prepares level 1 (easiest level)
def lvl1():
    tries_left = 6
    wordlen = 0
    guesses = ""
    os.system("cls")
    # Randomly select a file and shove it into a list
    rfile = random.choice(os.listdir("\hangman_terminal\database"))
    with open("/hangman_terminal/database/" + rfile, "r") as file:
        lines = []
        for line in file:
            lines.append(line)
    file.close()
    # Remove trailing new line from randomly selected element of list
    rlines = random.choice(lines)
    rlines = rlines.rstrip("\n")
    noduplicates = remDuplicates(rlines)
    noduplen = len(noduplicates)
    subject = rfile.replace(".txt", "")
    prepare_draw()
    allguess = []
    print("The subject is: " + subject)
    while tries_left > 0:
        for char in rlines:
            if char in guesses:
                print(char, end="")
            else:
                print("_", end="")
        print("\nGuess a character: ", end="")
        guess = input("")
        if guess == "" or len(guess) > 1 or guess == " ":
            os.system("cls")
            print("Enter a valid character (one character at a time!)")
        elif guess in rlines:
            wordlen += 1
            if guess in allguess:
                os.system("cls")
                print("Character already chosen")
                wordlen -= 1
            else:
                allguess.append(guess)
                guesses = guesses + guess
                if tries_left == 6:
                    prepare_draw()
                elif tries_left == 5:
                    draw_head()
                    print("Phew!")
                elif tries_left == 4:
                    draw_left_arm()
                    print("Phew!")
                elif tries_left == 3:
                    draw_right_arm()
                    print("Phew!")
                elif tries_left == 2:
                    draw_body()
                    print("Phew!")
                elif tries_left == 1:
                    draw_left_leg()
                    print("Phew!")
                elif tries_left == 0:
                    break
                    failed == 1
                    draw_right_leg()
                    print("\nYou lose")
                    print("The word is: " + rlines)
                    print("Start another game? [y/n]")
                    anothergame = readchar.readkey()
                    if anothergame == "y" or anothergame == "Y":
                        os.system("cls")
                        level()
                    elif anothergame == "n" or anothergame == "N":
                        sys.exit()
                    else:
                        sys.exit()
            print("Characters used: ")
            print(allguess)
        elif guess not in rlines:
            if guess in allguess:
                os.system("cls")
                print("Character already chosen")
            else:
                tries_left -= 1
                allguess.append(guess)
                if tries_left == 5:
                    draw_head()
                    print("Head drawn")
                elif tries_left == 4:
                    draw_left_arm()
                    print("Left arm drawn")
                elif tries_left == 3:
                    draw_right_arm()
                    print("Right hand drawn")
                elif tries_left == 2:
                    draw_body()
                    print("Body drawn")
                elif tries_left == 1:
                    draw_left_leg()
                    print("Left leg drawn")
                elif tries_left == 0:
                    draw_right_leg()
                    print("\nYou lose")
                    print("The word is: " + rlines)
                    print("Start another game? [y/n]")
                    anothergame = readchar.readkey()
                    if anothergame == "y" or anothergame == "Y":
                        os.system("cls")
                        level()
                    elif anothergame == "n" or anothergame == "N":
                        sys.exit()
                    else:
                        sys.exit()
            print("Characters used: ")
            print(allguess)
        if wordlen == noduplen:
            os.system("cls")
            print(rlines)
            print("\nCongratulations, you won!")
            print("Start another game? [y/n]")
            anothergame = readchar.readkey()
            if anothergame == "y" or anothergame == "Y":
                os.system("cls")
                level()
            elif anothergame == "n" or anothergame == "N":
                sys.exit()
            else:
                sys.exit()

# Prepares credits screen
def credits():
    os.system("cls")
    print("======= Hangman Terminal v1.0 ======")
    print("Created by tlegx")
    print("Copyright (c) 2021 tlegx under GPL-3.0 license")
    print("For more information, please visit:")
    print("https://github.com/tlegx/hangman-terminal")
    print("or:")
    print("https://tlegx.rf.gd")
    cprint('========= PRESS ANY KEY =========', 'red', attrs=['blink'])
    readchar.readkey()
    os.system("cls")
    level()


# Prepares level choosing screen
def level():
    print("      _______")
    print("     |/      |")
    print("     |      (_)", end="")
    cprint("       1. New game", "green")
    print("     |      \|/", end="")
    cprint("       2. Credits", "blue")
    print("     |       |")
    print('     |      / \ ')
    print("     |")
    print("    _|___")
    print("Enter your choice: ")
    l = readchar.readkey()
    if l == "1":
        os.system("cls")
        lvl1()
    elif l == "2":
        os.system("cls")
        credits()
    else:
        os.system("cls")
        print("Option does not exist")
        level()


# Prepares welcome screen
def welcome():
    os.system("cls")
    print("========= Hangman Terminal v1.0 =========")
    print("      _______")
    print("     |/      |")
    print("     |      (_)")
    print("     |      \|/")
    print("     |       |")
    print('     |      / \ ')
    print("     |")
    print("    _|___")
    cprint('========= PRESS ANY KEY =========', 'red', attrs=['blink'])
    readchar.readkey()
    os.system("cls")
    level()


welcome()
