import time
import random


# Prints text, then wait for two seconds
def print_sleep(text):
    print(text)
    time.sleep(2)


# Describes the setting and start of the game
def intro():
    print_sleep("You wake up, in a cell, hearing a moaning.")
    print_sleep("When you turn yourself around...")
    print_sleep("...you see behind your cell gate...")
    print_sleep("...a skeleton!")
    print_sleep("looking right at you.")
    print_sleep("It tries to open the gate, but it is locked.")
    print_sleep("It slowly walks away, as you get to your feet")
