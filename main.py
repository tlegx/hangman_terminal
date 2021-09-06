# Imports
import os
from termcolor import colored, cprint
import re
import readchar
import random
import sys

from hangman import DrawHangMan, HANGMAN_SEQ
from utils import utils


# Remove duplicates from a given string
def remDuplicates(str):
    return "".join(set(str))


# Prepares level 1 (easiest level)
class HangmanGame(DrawHangMan):
    def __init__(self) -> None:
        super().__init__()

    @staticmethod
    def get_word_choice():
        # Randomly select a file and shove it into a list
        rfile = random.choice(os.listdir("./database"))
        with open("./database/" + rfile, "r") as file:
            lines = []
            for line in file:
                lines.append(line)
        file.close()
        # Remove trailing new line from randomly selected element of list
        rlines = random.choice(lines)
        word_choice= rlines.rstrip("\n")
        subject = rfile.replace(".txt", "")
        print("The subject is: " + subject)
        return word_choice

    @staticmethod
    def single_letter_regex(string):
        return re.match("([a-zA-Z])\\1*", string)

    def setup(self):
        utils.clear_screen()
        self.tries_left = 6
        self.wordlen = 0
        self.guesses = ""
        self.start()
        self.allguess = []
        self.word_choice = self.get_word_choice()
        self.curr_word_stack = ['_'] * len(self.word_choice)
        noduplicates = remDuplicates(self.word_choice)
        self.noduplen = len(noduplicates)

    def print_word_choice(self, guess):
        idx = [ i for i, x in enumerate(self.word_choice) if x == guess]
        for i in idx:
            self.curr_word_stack[i] = guess

        print(','.join(self.curr_word_stack))

    def post_message(self, status='loss'):
        utils.clear_screen()
        if status == 'win':
            print(self.word_choice)
            print("\nCongratulations, you won!")
            print("Start another game? [y/n]")
        else:
            print("\nYou lose")
            print("The word is: " + self.word_choice)
            print("Start another game? [y/n]")

        anothergame = readchar.readkey()
        if anothergame == "y" or anothergame == "Y":
            utils.clear_screen()
            self.run()
        elif anothergame == "n" or anothergame == "N":
            sys.exit()
        else:
            sys.exit()

    def print_hanger(self, tries_left, part=True, status='loss', next = False):
        if tries_left== 6:
            self.start()
        elif tries_left < 6 and tries_left > 0:
            if next:
                self.next()
            else:
                self.draw_curr_hanger()

            if part:
                print('Oops hanging a body part!')
            else:
                print("Phew!")
        elif tries_left == 0:
            self.next()
            self.post_message(status)

    def check_guess_in_word(self, guess):
        if guess in self.allguess:
            utils.clear_screen()
            print("Character already chosen")
            return

        if guess in self.word_choice:
            self.wordlen += 1
            self.print_hanger(self.tries_left,part=False, status='win', next=False)
            self.print_word_choice(guess)
            self.guesses += guess
            self.allguess.append(guess)
        else:
            self.tries_left -= 1
            self.print_hanger(self.tries_left, status='loss', next=True)
            self.print_word_choice(guess)
            self.allguess.append(guess)

    
    def lvl1(self):
        while self.tries_left > 0:
            print("\nGuess a character: ", end="")
            guess = input("")

            if not self.single_letter_regex(guess):
                utils.clear_screen()
                print("Enter a valid character (one character at a time!)")
                continue

            self.check_guess_in_word(guess)

            print("Characters used: ")
            print(self.allguess)

            if self.wordlen == self.noduplen:
                self.post_message(status='win')

    # Prepares credits screen
    def credits(self):
        utils.clear_screen()
        print("======= Hangman Terminal v1.0 ======")
        print("Created by tlegx")
        print("Copyright (c) 2021 tlegx under GPL-3.0 license")
        print("For more information, please visit:")
        print("https://github.com/tlegx/hangman-terminal")
        print("or:")
        print("https://tlegx.rf.gd")
        cprint('========= PRESS ANY KEY =========', 'red', attrs=['blink'])
        readchar.readkey()
        utils.clear_screen()
        self.run()


    # Prepares level choosing screen
    def run(self):
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
            utils.clear_screen()
            super().__init__()
            self.setup()
            self.lvl1()
        elif l == "2":
            utils.clear_screen()
            self.credits()
        else:
            utils.clear_screen()
            print("Option does not exist")
            self.run()


    # Prepares welcome screen
    def start_game(self):
        utils.clear_screen()
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
        utils.clear_screen()
        self.run()

if __name__ == '__main__':
    hangman = HangmanGame()
    hangman.start_game()
